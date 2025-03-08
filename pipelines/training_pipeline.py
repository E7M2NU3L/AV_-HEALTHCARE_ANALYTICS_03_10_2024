from flows.clean_data import clean_data
from flows.ingest_data import ingester
from flows.train_model import train_model
from flows.compress_model import compress_model

import os

class TrainingPipeline:
    def __init__(self, data_path : str) -> None:
        """
        Initialize training pipeline

        Args:
            path : path of the input dataset
        """
        self.data_path = data_path

    def trainer(self):
        """
        Trainer Pipeline
        Args:
            self instance from the class
        """
        df = ingester(data_path=self.data_path)
        x_train, y_train = clean_data(df=df)
        model = train_model(x_train=x_train, y_train=y_train)
        
        path = os.path.join(
            os.getcwd(), "models"
        )

        result = compress_model(model=model, path=path)
        return result

def trainer_pipeline(dataset_path):
    """
    Pipelines for importing the data, cleaning it, traning the model, compressing it and saving it.

    Args:
        dataset_path : input path to the dataset
    """
    instance = TrainingPipeline(dataset_path)
    results = instance.trainer()

    return results