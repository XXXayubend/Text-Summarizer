from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from textSummarizer.pipeline.stage_02_datavalidation import DataValidationTrainingPipline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} <<<<<<")
    data_ingestion = DataIngestionTrainingPipline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  




STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} <<<<<<")
    data_validation = DataValidationTrainingPipline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 