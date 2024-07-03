# check these with config.yaml   data_ingestion: 
# to read yaml file open constant folder and in  __init__.py there we read all .yaml file path 


from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 

# now update configration manager  in src config   -- > config -> configuration.py  



# ----- > data_validation 

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict 
    
# now update configration manager  in src config  -- > config -> configuration.py  



# ----- > data_transformation 
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path 
    
# same  


# -- --- > model training 

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str  
    
# update configration manager  in src config  -- > config -> configuration.py      




@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    # mlflow_uri: str

    
    
    