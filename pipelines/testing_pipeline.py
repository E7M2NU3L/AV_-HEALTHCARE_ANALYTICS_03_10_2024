from flows.clean_data import clean_data
from flows.ingest_data import ingester
from flows.evaluate_model import evaluate_model

import joblib
from sklearn.ensemble import VotingClassifier

class TestingPipeline:
    def __init__(self, data_path : str, model_path : str) -> None:
        """
        Initialize training pipeline

        Args:
            data_path : path of the input dataset
            model_path : path of the model
        """
        self.data_path = data_path
        self.model_path = model_path

    def evaluator(self) -> dict:
        """
        Trainer Pipeline
        Args:
            self instance from the class
        """
        df = ingester(data_path=self.data_path)
        x_test, y_test = clean_data(df=df)
        model : VotingClassifier = joblib.load(self.model_path)
        reports = evaluate_model(x_test=x_test, y_test=y_test, main_model=model)
        return reports
    
def tester_pipeline(dataset_path : str, model_path : str):
    """
    Pipelines for importing the test data, cleaning it, Evaluating the model.

    Args:
        dataset_path : input path to the dataset
        model_path : input path to the model
    """
    instance = TestingPipeline(data_path=dataset_path, model_path=model_path)
    results = instance.evaluator()
    return results