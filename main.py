import yaml
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_to_db
from src.validate import validate_data
from src.logger import setup_logger

def run_pipeline():
    # Load config
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    logger = setup_logger(config["logging"]["log_file"])

    try:
        logger.info("Pipeline started")

        df = extract_data(config["data"]["input_path"])
        logger.info("Data extracted")

        df = transform_data(df)
        logger.info("Data transformed")

        validate_data(df)
        logger.info("Data validated")

        load_to_db(df, config["database"]["db_path"], config["database"]["table_name"])
        logger.info("Data loaded into database")

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
