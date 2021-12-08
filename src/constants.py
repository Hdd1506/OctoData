from pathlib import Path

PARENT_PATH = Path(__file__).parent.parent

INPUT_PATH = PARENT_PATH / "input/"
DATASET_PATH = INPUT_PATH / "creditcard.csv"

OUTPUT_PATH = PARENT_PATH / "output/"
DECISION_TREE_MODEL_PATH = OUTPUT_PATH / "models/decisiontree.joblib"
SVC_MODEL_PATH = OUTPUT_PATH / "models/svc.joblib"
AGGREGATOR_MODEL_PATH = OUTPUT_PATH / "models/aggregator_model.joblib"
CM_PLOT_PATH = OUTPUT_PATH / "plots/cm_plot.png"


INFERENCE_EXAMPLE = [
    -7.334,  4.960, -8.451,  8.174, -7.237, -2.382, -11.508,  4.635,
    -6.557, -11.519,  6.455, -13.380, 0.545, -13.026, -0.453, -13.251,
    -22.883, -9.287,  4.038,  0.723, 2.153,  0.033, -0.014,  0.625,
    -0.053,  0.164,  1.411,  0.315, 11.380
]