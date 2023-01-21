# from us_visa.configuration.mongo_db_connection import MongoDBClient

# ins = MongoDBClient()

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact

from us_visa.components.data_ingestion import DataIngestion

di_ins = DataIngestion(DataIngestionConfig)

di_art = di_ins.initiate_data_ingestion()