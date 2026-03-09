import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.mlproject.utils import read_sql_data
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException


# ---------------------------
# Data Ingestion Configuration
# ---------------------------
@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


# ---------------------------
# Data Ingestion Class
# ---------------------------
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")

        try:
            # 1️⃣ Fetch data from MySQL using utils
            df = read_sql_data()
            logging.info("Data fetched from database successfully")

            # 2️⃣ Create artifacts folder if not exists
            os.makedirs("artifacts", exist_ok=True)

            # 3️⃣ Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")

            # 4️⃣ Split into train and test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # 5️⃣ Save train and test datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"Train data saved at: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at: {self.ingestion_config.test_data_path}")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Error occurred in Data Ingestion")
            raise CustomException(e, sys)