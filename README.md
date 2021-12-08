# Python Data Assignment 

## Requirements
- Python 3.7 or higher.
#### - Install pipenv on your global python setup
```Python
    pip install pipenv 
```
Or follow [documentation](https://pipenv.pypa.io/en/latest/install/) to install it properly on your system
#### - Install requirements
```sh
    cd python-data-assignement
```
```Python
    pipenv install
```
```Python
    pipenv shell
```
#### - Start the application
```sh
    sh run.sh
```
- API : http://localhost:5000
- Streamlit Dashboard : http://localhost:8000

P.S You can check the log files for any improbable issues with your execution.
## Before we begin
- In this assignement, you will be asked to write, refactor, and test code. 
- Make sure you respect clean code guidelines.
- Some parts of the already existing code are bad. Your job is to refactor them.
- Read the assignement carefully.
- Read the code thoroughly before you begin coding.

## Description
This mini project is a data app that revolves around credit card fraud detection.

You are given a `dataset` that contains a number of transactions.

Each row of the dataset contains:
- Features that were extracted using dimensionality reduction with `PCA` 
- The transaction amount
- A flag `[0,1]` that tells you whether a transaction is clear or fraudulent.

The project contains by default:
- A baseline `decision tree model` trained on the aforementioned dataset
- An `API` that exposes an `inference endpoint` for predictions using the baseline model
- A streamlit dashboard divided on three parts `(Exploratory Data Analysis, Training, Inference)`

## Assignment
### 1 - Code Refactoring
`Streamlit` is a component-based data app creator that allows you to create interactive dashboards using Python. 

While Streamlit is easy to use by "non frontenders", it can easily turn into a complicated piece of code.

As mentioned previously, the streamlit dashboard you have at hand is divided into 3 sections:
- Exploratory Data Analysis
- Training
- Inference

The code for the dashboard is written into one long Python (`dashboard.py`) script which makes it long, unoptimized, hard to read, hard to maintain, and hard to upgrade.

Your job is to:
- Rewrite the code while respecting `clean code` guidelines.
- `Refactor` the script and dissociate the components.
- Create the appropriate `abstraction` to make it easy to add components on top of the existing code.

`Bonus points`: if you pinpoint any other code anomalies across the whole project and correct them. 
### 2 - Exploratory Data Analysis
In this section, you are asked to explore the dataset you are provided and derive insights from it:
- Statistical Descriptions
- Charts
- Correlations
- Features

Your EDA must be added to the first section of the streamlit dashboard.

![](./input/static/eda.png)

Hints: Please refer to the [documentation](https://docs.streamlit.io/library/api-reference) to learn more on how to use Streamlit `widgets` in order to display: `pandas dataframes`, `charts`, `tables`, etc, as well as interactive components: `text inputs`, `buttons`, `sliders`, etc.

### 3 - Training 
In this section, you are asked to `beat` the baseline model. 

The goal is to capitalize on what you have discovered during the `EDA phase` and use the `features` and insights you derived in order to create a model that performs `better` than the baseline you were provided.

The higher the `F1 score` the better.

You can `trigger` the baseline model `training` in the `second` section of the `dashboard`.

Choose the `name` of the model and whether you want to `serialize` it.

![](./input/static/training.png)

Click `Train model` and wait until the training is done...

![](./input/static/training_current.png)

Once done, you will be able to see the F1 score as well as the confusion matrix.

P.S: If you chose the `save option` at the beginning of the training, you will be able to see the serialized model under `output/models/model_name`

![](./input/static/training_results.png)

Hints: 
- Make sure to change the training pipeline before you can trigger the training of your own model from the dashboard. 
- Your model must respect the abstraction used to build the baseline
- You can use multiple models (`ensembling`) using the `AggregatorModel` class

### 4 - Inference

`Inference` is just a fancy word to say `prediction`.

In the third section of the dashboard, you can `tweak` the different `features` and run the serialized model against them.

P.S The original dataset has `29` features. But for the sake of simplification, we froze most of the features and only left `4` (`feature11`, `feature13`, `feature15`, `amount`) for you to tinker with.

The first example shows a configuration that renders a non fraudulent prediction:

![](./input/static/inference_clear.png)

The second example shows a configuration that renders a fraudulent prediction:

![](./input/static/inference_fraudulent.png)

In this section, you are asked to: 
- Create an `endpoint` that allows you to `save` the prediction results into a `SQlite table`.
- Display the `contents` of the SQlite table after each inference run.

Hints: Think about using `SQLALchemy` as well as its integration with `Flask`

### 5 - Unit testing

As mentioned previously, your code should be unit tested. 

Hints: Use `pytest` for your unit tests as well as `mocks` for external services.
