import logging
import mlflow
from pipelines.training_pipeline import trainer_pipeline
from pipelines.testing_pipeline import tester_pipeline
import os

# starting the mlflow experiment
class MlFlowInstantiator:
    def __init__(self, port : str, experiment : str, path : str, test_path : str, model_path : str) -> None:
        self.port : str = port
        self.experiment : str = experiment
        self.path = path
        self.test_path = test_path
        self.model_path = model_path

    def starter(self):
        mlflow.set_experiment(self.experiment)
        mlflow.set_tracking_uri(self.port)

        trainer_results = trainer_pipeline(dataset_path=self.path)
        if trainer_results is None:
            logging.error("Could not get results training Failed")

        params, model = trainer_results

        tester_results = tester_pipeline(dataset_path=self.test_path, model_path=self.model_path)

        with mlflow.start_run():
            mlflow.log_params(params)
            mlflow.log_metrics(tester_results)
            mlflow.sklearn.load_model(model)

def ml_pipeline(port, experiment_name, train_path, test_path, model_path):
    instance = MlFlowInstantiator(port=port, experiment=experiment_name, path=train_path, test_path=test_path, model_path=model_path)
    instance.starter()

if __name__ == "__main__":
    port = "http://127.0.0.1:5000"
    experiment_name = "av_healthcare_analysis"
    train_dataset_path = os.path.join(os.getcwd(), "data", "train_data.csv")
    test_dataset_path = os.path.join(os.getcwd(), "data", "test_data.csv")
    model_path = os.path.join(os.getcwd(), "models", "ensemble_model_voting_hard_compressed.joblib")
    
    ml_pipeline(port, experiment_name, train_dataset_path, test_dataset_path, model_path)