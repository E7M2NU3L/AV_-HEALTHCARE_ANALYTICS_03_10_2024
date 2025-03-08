import joblib
import mlflow
from sklearn.ensemble import VotingClassifier
import os
import warnings

warnings.filterwarnings("module")

metrics = {'0': {'precision': 0.6577391304347826, 'recall': 0.15454396861719516, 'f1-score': 0.2502812520680299, 'support': 24472.0}, '1': {'precision': 0.5272993555946104, 'recall': 0.2441743753899574, 'f1-score': 0.3337845104110656, 'support': 36863.0}, '2': {'precision': 0.5876554881518247, 'recall': 0.8865587279786588, 'f1-score': 0.7068051526908438, 'support': 75722.0}, 'accuracy': 0.5830785731483981, 'macro avg': {'precision': 0.5908979913937392, 'recall': 0.4284256906619371, 'f1-score': 0.43029030505664645, 'support': 137057.0}, 'weighted avg': {'precision': 0.5839357130180625, 'recall': 0.5830785731483981, 'f1-score': 0.5249631976473147, 'support': 137057.0}}

model : VotingClassifier = joblib.load(os.path.join(os.getcwd(), "models") + "/ensemble_model_voting_hard_compressed.joblib")
print("Model has been loaded")

params = model_params = {
    "estimators": [
        ("rf", "RandomForestClassifier"),
        ("ad", "AdaBoostClassifier"),
        ("gn", "GaussianNB")
    ],
    "flatten_transform": True,
    "n_jobs": None,
    "verbose": False,
    "voting": "hard",
    "weights": None,
    "rf": {
        "criterion": "entropy",
        "max_depth": 12,
        "n_estimators": 50,
        "bootstrap": True,
        "ccp_alpha": 0.0,
        "class_weight": None,
        "max_features": "sqrt",
        "max_leaf_nodes": None,
        "max_samples": None,
        "min_impurity_decrease": 0.0,
        "min_samples_leaf": 1,
        "min_samples_split": 2,
        "min_weight_fraction_leaf": 0.0,
        "monotonic_cst": None,
        "n_jobs": None,
        "oob_score": False,
        "random_state": None,
        "verbose": 0,
        "warm_start": False
    },
    "ad": {
        "algorithm": "SAMME.R",
        "learning_rate": 1.0,
        "n_estimators": 50,
        "random_state": 42,
        "estimator": {
            "model": "DecisionTreeClassifier",
            "ccp_alpha": 0.0,
            "class_weight": None,
            "criterion": "gini",
            "max_depth": None,
            "max_features": "sqrt",
            "max_leaf_nodes": None,
            "min_impurity_decrease": 0.0,
            "min_samples_leaf": 1,
            "min_samples_split": 2,
            "min_weight_fraction_leaf": 0,
            "monotonic_cst": None,
            "random_state": 42,
            "splitter": "best"
        }
    },
    "gn": {
        "priors": None,
        "var_smoothing": 1e-09
    }
}


with mlflow.start_run():
    mlflow.set_experiment("Av Healthcare Patient Severity Classifications")
    mlflow.set_tracking_uri("http://127.0.0.1:5000/")

    mlflow.log_metrics({
        "accuracy": metrics["accuracy"],
        "0_precision": metrics["0"]["precision"],
        "0_recall": metrics["0"]["recall"],
        "0_f1_score": metrics["0"]["f1-score"],
        "0_support": metrics["0"]["support"],
        "macro_avg_precision": metrics["macro avg"]["precision"],
        "macro_avg_recall": metrics["macro avg"]["recall"],
        "macro_avg_f1_score": metrics["macro avg"]["f1-score"],
        "weighted_avg_precision": metrics["weighted avg"]["precision"],
        "weighted_avg_recall": metrics["weighted avg"]["recall"],
        "weighted_avg_f1_score": metrics["weighted avg"]["f1-score"]
    })
    print("Metrics has been logged successfully")

    mlflow.log_params(params)
    print("Params has been logged successfully")

    mlflow.sklearn.log_model(model, "Ensemble Model - Patient Severity Classifier")
    print("Model has been logged successfully")