import os
import urllib.request as request                 # to download data from url 
import zipfile                                   # unzip data 
from mlProject import logger                     # for logging 
from mlProject.utils.common import get_size      # to see the file size  
from pathlib import Path 
from mlProject.entity.config_entity import DataIngestionConfig




class DataIngestion:
    def __init__(self, config: DataIngestionConfig):   # it will get these from  def get_data_ingestion_config(self)
        self.config = config


    
    def download_file(self):                             #<- this method is responsible for downloading data from url 
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,                                # read url 
                filename = self.config.local_data_file                          # take file fro local_data_file 
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
  
  
  


# update pipeline 
# in pipeline folder  create stage_01_data_ingestion.py 