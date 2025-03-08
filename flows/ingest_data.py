import logging
import pandas as pd

# 1. Ingesting the Data into the pipeline
class IngestData:
    def __init__(self, data_path : str) -> None:
        """
        Instantiating the method

        Args:
            path of the csv file
        """
        self.path = data_path

    def get_data(self):
        """
        Getting the data as a dataFrame

        Args:
            self from the class
        Returns:
            getting the data as a dataFrame
        """
        logging.info(f'Ingesting data from {self.path}')
        data = pd.read_csv(self.path)
        return data
    
def ingester(data_path : str) -> pd.DataFrame:
    """
    To Read the Dataset
    
    Args:
        path of the file
    Returns:
        A pandas DataFrame
    """
    instance = IngestData(data_path=data_path)
    df = instance.get_data()
    return df