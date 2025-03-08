import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

class TrainModel:
    def __init__(self, x_train : pd.DataFrame, y_train : pd.DataFrame) -> None:
        self.x_train = x_train
        self.y_train = y_train

        # Bagging Model
        rf = RandomForestClassifier(
            n_estimators=50,
            max_depth=12
        )

        # Boosting Model
        dt = DecisionTreeClassifier(
            criterion = "gini",
            splitter = "best",
            max_depth= None,
            min_samples_split= 2,
            min_samples_leaf = 1,
            min_weight_fraction_leaf = 0,
            random_state = 42
        )
        ad = AdaBoostClassifier(dt, n_estimators=50, learning_rate=1.0, random_state=42)

        # Probabilistic Model
        gnb = GaussianNB()

        # Voting Model
        self.main_model = VotingClassifier([
            ("rf", rf),
            ("ad", ad),
            ("gn", gnb)
        ], voting="soft")

    def train(self) -> VotingClassifier:
        logging.info('Training the model...')
        self.main_model.fit(self.x_train, self.y_train)
        logging.info("Model has been trained perfectly")
        return self.main_model

def train_model(x_train : pd.DataFrame, y_train : pd.DataFrame) -> VotingClassifier:
    """
    Training the model with proper ensemble network

    Args:
        x_train : preprocessed training input columns
        y_train : preprocessed training output column
    """
    instance = TrainModel(x_train=x_train, y_train=y_train)
    output_model = instance.train()

    return output_model