import logging
from pipelines.training_pipeline import trainer_pipeline

class ModelDev:
    def __init__(self, path : str) -> None:
        self.path = path

    def trainer(self) -> bool:
        logging.info("Training the Model")
        result = trainer_pipeline(dataset_path=self.path)
        return result
    
def train_model(path : str) -> None:
    instance = ModelDev(path=path)

    result = instance.trainer()
    if result == True:
        logging.info("Model trained successfully")
    else:
        logging.info("There has been some problems training the model")