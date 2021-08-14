# system dependencies
import pandas as pd

# local dependencies
from constants import Constants


class Dataset:
    """
    Data Access Object to Load & Parse dataset files -- DAO
    """
    def __init__(self):
        """
        Constructor
        """

        self.constants = Constants()

    def loader(self, data_type: str):
        if data_type.lower() == "train":
            dataset_file = self.constants.TRAINING_SET
        elif data_type.lower() == "test":
            dataset_file = self.constants.TEST_SET
        else:
            raise Exception("Please enter proper dataset file name!")

        return pd.read_excel(dataset_file)
