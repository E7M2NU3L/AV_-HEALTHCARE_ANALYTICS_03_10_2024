import logging
from sklearn.ensemble import VotingClassifier
import pandas as pd
from sklearn.metrics import classification_report

class Evaluation:
    def __init__(self, x_test : pd.DataFrame, y_test : pd.DataFrame, main_model : VotingClassifier) -> None:
        """
        Initialization of the class

        Args:
            x_test : input columns of testing dataset
            y_test : target column of testing dataset
            main_model : model to be evaluated
        """
        
        self.x_test = x_test
        self.y_test = y_test
        self.main_model = main_model

    def evaluate(self) -> dict:
        """
        Evaluates the model and returns the classification report

        Args:
            self instance of the class
        Returns:
            report dictionary
        """
        logging.info("Evaluating the model....")
        y_pred = self.main_model.predict(self.x_train)
        report = classification_report(self.y_test, y_pred, output_dict=True)

        return report
    
def evaluate_model(x_test : pd.DataFrame, y_test : pd.DataFrame, main_model : VotingClassifier) -> dict:
    """
    Evaluation of the model 

    Args:
        x_test : input columns of testing dataset
        y_test : target column of testing dataset
        main_model : model to be evaluated
    Returns:
        classification report as a dict
    """
    results = evaluate_model(x_test=x_test, y_test=y_test, main_model=main_model)
    return results