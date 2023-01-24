# from us_visa.configuration.mongo_db_connection import MongoDBClient

# ins = MongoDBClient()

# from us_visa.configuration.aws_connection import S3Client

# ins = S3Client()

from us_visa.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig

from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation
from us_visa.components.data_transformation import DataTransformation
from us_visa.components.model_trainer import ModelTrainer
from us_visa.components.model_evaluation import ModelEvaluation
from us_visa.components.model_pusher import ModelPusher

di_ins = DataIngestion(DataIngestionConfig)

di_art = di_ins.initiate_data_ingestion()

dv_ins = DataValidation(data_ingestion_artifact=di_art, data_validation_config=DataValidationConfig)

dv_art = dv_ins.initiate_data_validation()

dt_ins = DataTransformation(data_ingestion_artifact=di_art, data_transformation_config=DataTransformationConfig, data_validation_artifact=dv_art)

dt_art = dt_ins.initiate_data_transformation()

mt_ins = ModelTrainer(data_transformation_artifact=dt_art, model_trainer_config=ModelTrainerConfig)

mt_art = mt_ins.initiate_model_trainer()

me_ins = ModelEvaluation(model_eval_config=ModelEvaluationConfig, data_ingestion_artifact=di_art, model_trainer_artifact=mt_art)

me_art = me_ins.initiate_model_evaluation()

mp_ins = ModelPusher(me_art, ModelPusherConfig)

mp_art = mp_ins.initiate_model_pusher()