from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys, os
from cellSegmentation.pipeline.training_pipeline import TrainPipeline




obj = TrainPipeline()
obj.run_pipeline()
print("Training Done")