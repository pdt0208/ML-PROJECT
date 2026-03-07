import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_ingestion import DataIngestionConfig


if __name__ == "__main__":
    logging.info("The Execution has started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e, sys)
    