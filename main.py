# system dependencies
import logging
logger = logging.getLogger("main")

# local dependencies
from dataset import Dataset


if __name__ == "__main__":
    try:
        # instantiate data access object
        dao = Dataset()

        # load train and test datasets
        train_set = dao.loader("train")
        test_set = dao.loader("test")

    except Exception as e:
        logger.error("Analyzer did not start properly!")
        logger.error(e, exc_info=True)
