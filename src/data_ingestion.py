import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
from utils.common_function import read_yaml
import sys

logger = get_logger(__name__)

class Dataingestion:
    def __init__(self, config):
        # ✅ Fix: assign the provided config properly
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data ingestion initialized with bucket: {self.bucket_name}, file: {self.file_name}")

    def download_csv_from_gcp(self):
        """Download the CSV file from GCP bucket"""
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"CSV file downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error("Error while downloading data from GCP")
            raise CustomException("Failed to download CSV from GCP", e)

    def split_data(self):
        """Split data into train and test sets"""
        try:
            logger.info("Starting data splitting process...")
            data = pd.read_csv(RAW_FILE_PATH)

            train_data, test_data = train_test_split(
                data, test_size=1 - self.train_test_ratio, random_state=42
            )

            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")

        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split CSV data", e)

    def run(self):
        """Run the ingestion workflow"""
        try:
            logger.info("Starting data ingestion process...")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("Data ingestion completed successfully!")
        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")
        finally:
            logger.info("Data ingestion process finished.")


if __name__ == "__main__":
    # ✅ Read config YAML and run the process
    config = read_yaml(CONFIG_PATH)
    data_ingestion = Dataingestion(config)
    data_ingestion.run()
