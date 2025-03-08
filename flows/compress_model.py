import logging
import joblib
from sklearn.ensemble import VotingClassifier
from typing_extensions import Tuple

class Compressor:
    def __init__(self, model : VotingClassifier, path : str) -> None:
        self.model = model
        self.path = path

    def compress(self):
        logging.info("Compressing the Model....")

        try:
            for estimators in self.model.estimators_:
                if hasattr(estimators, "n_estimators") and estimators.n_estimators > 100:
                    estimators.n_estimators = 100

            for estimators in self.model.estimators_:
                if hasattr(estimators, "max_depth") and estimators.max_depth is None:
                    estimators.max_depth = 10

            for estimators in self.model.estimators_:
                if hasattr(estimators, "oob_decision_function_"):
                    del estimators.oob_decision_function_ 

            for estimators in self.model.estimators_:
                if hasattr(estimators, "feature_importance_"):
                    del estimators.feature_importance_
        except Exception as e:
            logging.error(f"Error occured while pruning, {e}")

        try:
            joblib.dump(
                self.model, 
                self.path,
                compress=9
            )
            return self.model.get_params(), self.model
        except Exception as e:
            logging.error("Error Occured during exporting the model: {0}".format(e))

def compress_model(model : VotingClassifier, path : str) -> Tuple[dict, VotingClassifier] | None:
    instance = Compressor(model=model, path=path)
    is_saved_model = instance.compress()

    return is_saved_model