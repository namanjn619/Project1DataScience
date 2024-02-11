from src.project1ml.logger import logging
from src.project1ml.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("The excecution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)