# system dependencies
import os


def read_only_properties(*attrs):
    """
    Make attributes of a class readonly.
    """

    def class_rebuilder(cls):
        """
        The class decorator example
        """

        class NewClass(cls):
            """
            This is the overwritten class
            """
            def __setattr__(self, name, value):

                if name not in attrs:
                    pass
                elif name not in self.__dict__:
                    pass
                else:
                    raise AttributeError("Can't touch {}".format(name))

                super().__setattr__(name, value)
        return NewClass

    return class_rebuilder


@read_only_properties(
    "ROOT_DIR",
    "DATASET_DIR",
    "TRAINING_SET",
    "TEST_SET"
)
class Constants:
    """
    All global constant parameters 
    """

    def __init__(self):
        """
        Constructor
        """

        # config files and important folders
        self.ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
        self.DATASET_DIR = self.ROOT_DIR + "/dataset"
        self.TRAINING_SET = self.DATASET_DIR + "/Training Set.xlsx"
        self.TEST_SET = self.DATASET_DIR + "/Test Set.xlsx"
