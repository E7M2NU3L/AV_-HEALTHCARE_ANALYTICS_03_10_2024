import logging
from pipelines.testing_pipeline import tester_pipeline

class ModelEval:
    def __init__(self, path : str, model : str) -> None:
        self.path = path
        self.model = model

    def trainer(self) -> dict:
        logging.info("Training the Model")
        result = tester_pipeline(dataset_path=self.path, model_path=self.model)
        return result
    
def train_model(path : str, model : str) -> dict:
    instance = ModelEval(path=path, model=model)

    result : dict = instance.trainer()
    return result