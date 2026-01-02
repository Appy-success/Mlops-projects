import os
import sys
# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        # Ensure the artifacts directory exists
        os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            import pandas as pd
            # Ensure the source data file exists
            source_file = 'src/notebook/data/stud.csv'
            if not os.path.exists(source_file):
                logging.error(f"Source data file not found: {source_file}")
                raise FileNotFoundError(f"Source data file not found: {source_file}")

            logging.info(f"Source data file found: {source_file}")
            df = pd.read_csv(source_file)
            logging.info('Read the dataset as dataframe')

            # Save the raw data
            logging.info(f"Saving raw data to: {self.ingestion_config.raw_data_path}")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved successfully")

            # Split the data into train and test sets
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train and test datasets
            logging.info(f"Saving train data to: {self.ingestion_config.train_data_path}")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info(f"Saving test data to: {self.ingestion_config.test_data_path}")
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error(f"Error in data ingestion: {e}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    print(f"Data ingestion completed successfully!")
    print(f"Train data path: {train_data}")
    print(f"Test data path: {test_data}")