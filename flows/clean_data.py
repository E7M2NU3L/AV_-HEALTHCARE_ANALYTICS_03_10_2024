import logging
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, Normalizer, LabelEncoder
from sklearn.impute import SimpleImputer

class CleanData:
    def __init__(self, df : pd.DataFrame) -> None:
        self.df = df
        self.input_columns = ['Hospital_code', 'Hospital_type_code', 'City_Code_Hospital',
       'Hospital_region_code', 'Available Extra Rooms in Hospital',
       'Department', 'Ward_Type', 'Ward_Facility_Code', 'City_Code_Patient', 'Type of Admission',
       'Bed Grade', 'Visitors with Patient', 'Age',
       'Admission_Deposit']
        self.target_column = "Severity of Illness"
        self.categorical_column = ["Department", "Type of Admission", "Hospital_type_code", "Age", "Hospital_region_code", "Ward_Facility_Code", "Ward_Type"]

    def clean_data(self):
        """
        Cleans the Dataset with proper sklearn pipelines

        Args:
            class instance
        Returns:
            preprocessed x_train and y_train Dataframes
        """
        logging.info("Cleaning data...")
        
        # segregating the training dataset
        x_train = self.df[self.input_columns]
        y_train = self.df[self.target_column]

        le = LabelEncoder()

        # label encoder
        for column in self.input_columns:
            try:
                x_train[column] = le.fit_transform(x_train[column])
            except Exception as e:
                logging.error(f"Error occurred while label encoding {column}: {e}")
        
        try:
            y_train = le.fit_transform(pd.DataFrame(y_train))
        except Exception as e:
            logging.error(f"Error occurred while label encoding y: {e}")

        # preprocessor pipelines
        pre_processor_inputs = Pipeline([
            ("imputer", SimpleImputer(strategy="mean")),
            ("scaler", StandardScaler()),
            ("normalizer", Normalizer(norm="l1"))
        ])

        # preprocess the input and outputs
        x_preprocessed = pre_processor_inputs.fit_transform(x_train)
        y_preprocessed = y_train

        return pd.DataFrame(x_preprocessed), pd.DataFrame(y_preprocessed)

def clean_data(df : pd.DataFrame):
    """
    Cleaning and Data Wrangling Process

    Args:
        input dataframe
    Returns:
        preprocessed x_train and y_train Dataframes
    """
    instance = CleanData(df=df)
    preprocessed_outputs = instance.clean_data()
    return preprocessed_outputs