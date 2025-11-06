
from src.data_ingestion import Dataingestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
from utils.common_function import read_yaml
from config.path_config import *


if __name__ == "__main__":
    ## data ingestion
    config = read_yaml(CONFIG_PATH)
    data_ingestion = Dataingestion(config)
    data_ingestion.run()

    #data processing

    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()  

    #model training

    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    trainer.run()


