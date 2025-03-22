from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys

logging.info("Hello World")



try:
    a = 1/0
except Exception as e:
    raise AppException(e, sys)