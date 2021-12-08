import time
import streamlit as st
import requests
from PIL import Image
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from src.constants import INFERENCE_EXAMPLE, CM_PLOT_PATH
from src.training.train_pipeline import TrainingPipeline

data=pd.read_csv(r'C:\Users\setze\Desktop\python-data-assignment-main\input\creditcard.csv')
st.title("Card Fraud Detection Dashboard")
st.sidebar.title("Data Themes")

sidebar_options = st.sidebar.selectbox(
    "Options",
    ("EDA", "Training", "Inference")
)

if sidebar_options == "EDA":
    st.header("Exploratory Data Analysis")
    st.info("In this section, you are invited to create insightful graphs "
            "about the card fraud dataset that you were provided.")

    #st.title("Data desciption")
    #sata=data.info
    #st.table(sata)
    
    st.title("Correlation between features")
    corr = data.corr()

    st.table(corr.style.background_gradient())

    
    #st.line_chart(data.head())

    st.title("Features information")
    st.table(data.describe())

    
    st.title("Graphes")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.text('Target repartition')
    sns.countplot('Class', data=data)
    st.pyplot()
    
    
    sns.set_theme(style="whitegrid")
    
    for i in list(data.columns):
        st.write(i)
        ax=sns.boxplot(x=data[i])
        st.pyplot()
     
    #ax = sns.boxplot(x="Amount", y="Class", data=data)

    #ax = sns.swarmplot(x="Amount", y="Class", data=data, color=".25")
    #st.pyplot()
     

elif sidebar_options == "Training":
    st.header("Model Training")
    st.info("Before you proceed to training your model. Make sure you "
            "have checked your training pipeline code and that it is set properly.")

    name = st.text_input('Model name', placeholder='KNN(n=2)')
    print("ll", name)
    serialize = st.checkbox('Save model')
    train = st.button('Train Model')
    train2=st.button('test')

    if train:
        with st.spinner('Training model, please wait...'):
            time.sleep(1)
            try:
                tp = TrainingPipeline()
                tp.train(serialize=serialize, model_name=name)
                tp.render_confusion_matrix(plot_name=name)
                accuracy, f1 = tp.get_model_perfomance()
                col1, col2 = st.columns(2)
    
                col1.metric(label="Accuracy score", value=str(round(accuracy, 4)))
                col2.metric(label="F1 score", value=str(round(f1, 4)))

                st.image(Image.open(CM_PLOT_PATH))

            except Exception as e:
                st.error('Failed to train model!')
                st.exception(e)
    

elif sidebar_options == "Inference":
    st.header("Fraud Inference")
    st.info("This section simplifies the inference process. "
            "You can tweak the values of feature 1, 2, 19, "
            "and the transaction amount and observe how your model reacts to these changes.")
    feature_11 = st.slider('Transaction Feature 11', -10.0, 10.0, step=0.001, value=-4.075)
    feature_13 = st.slider('Transaction Feature 13', -10.0, 10.0, step=0.001, value=0.963)
    feature_15 = st.slider('Transaction Feature 15', -10.0, 10.0, step=0.001, value=2.630)
    amount = st.number_input('Transaction Amount', value=1000, min_value=0, max_value=int(1e10), step=100)
    infer = st.button('Run Fraud Inference')

    INFERENCE_EXAMPLE[11] = feature_11
    INFERENCE_EXAMPLE[13] = feature_13
    INFERENCE_EXAMPLE[15] = feature_15
    INFERENCE_EXAMPLE[28] = amount

    if infer:
        with st.spinner('Running inference...'):
            time.sleep(1)
            try:
                result = requests.post(
                    'http://localhost:3333/api/inference',
                    json=INFERENCE_EXAMPLE
                )
                if int(int(result.text) == 1):
                    st.success('Done!')
                    st.metric(label="Status", value="Transaction: Fraudulent")
                else:
                    st.success('Done!')
                    st.metric(label="Status", value="Transaction: Clear")
            except Exception as e:
                st.error('Failed to call Inference API!')
                st.exception(e)

