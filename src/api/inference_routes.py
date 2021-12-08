from flask import Blueprint, request
from src.constants import AGGREGATOR_MODEL_PATH
from src.models.aggregator_model import AggregatorModel
import numpy as np

model = AggregatorModel()
model.load(AGGREGATOR_MODEL_PATH)
blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return "CARD FRAUD DETECTION API - INFERENCE BLUEPRINT"


@blueprint.route('/inference', methods=['POST'])
def run_inference():
    if request.method == 'POST':
        features = np.array(request.json).reshape(1, -1)
        prediction = model.predict(features)
        return str(prediction[0])
