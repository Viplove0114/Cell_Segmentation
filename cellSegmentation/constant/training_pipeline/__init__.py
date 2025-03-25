ARTIFACTS_DIR: str = 'artifacts'

'''
data ingestion related constant start with data _ingestion var name
'''

DATA_INGESTION_DIR_NAME: str = 'data_ingestion'

DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'

DATA_DOWNLOAD_URL: str = 'https://drive.google.com/file/d/1psu2nKDKnOC7k_PPn5fkTCFF0tCl7lju/view?usp=sharing'


'''
Data Validation realted contant start with Data_Validation VAR name
'''

DATA_VALIDATION_DIR_NAME:str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES= ['train', 'valid', 'test', 'data.yaml']



'''
MODEL TRAINER related constant start with MODEL_TRAINER var name
'''

MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov8s-seg.pt"

MODEL_TAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16