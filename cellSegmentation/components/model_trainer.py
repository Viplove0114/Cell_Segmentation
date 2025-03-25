import os
import sys
import shutil
import zipfile
import subprocess
import torch
from cellSegmentation.utils.main_utils import read_yaml_file
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.config_entity import ModelTrainerConfig
from cellSegmentation.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def extract_zip(self, zip_path, dest_folder):
        """Extracts ZIP file to the specified folder."""
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dest_folder)
        os.remove(zip_path)

    def load_model_with_safe_globals(self, model_path):
        """Loads YOLO model with safe globals to bypass PyTorch 2.6 restrictions."""
        try:
            # Set weights_only=False explicitly
            with torch.serialization.safe_globals(['ultralytics.nn.tasks.SegmentationModel']):
                model = torch.load(model_path, map_location='cpu', weights_only=False)
            return model
        except Exception as e:
            raise AppException(f"Error loading model: {e}", sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            # Extract data.zip using Python zip module
            logging.info("Unzipping data.zip")
            self.extract_zip("data.zip", "./")

            # YOLO model training
            logging.info("Running YOLO training...")
            yolo_command = (
                f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} "
                f"data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true"
            )
            subprocess.run(yolo_command, shell=True, check=True)

            # Ensure model trainer directory exists
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

            # Copy the best model file
            src = os.path.join("runs", "segment", "train", "weights", "best.pt")
            dst = os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt")
            shutil.copy(src, dst)

            # Removing unnecessary files/folders
            for folder in ["yolov8s-seg.pt", "train", "valid", "test", "data.yaml", "runs"]:
                folder_path = os.path.join(os.getcwd(), folder)
                if os.path.isfile(folder_path):
                    os.remove(folder_path)
                elif os.path.isdir(folder_path):
                    shutil.rmtree(folder_path)

            # Model Trainer Artifact
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="artifacts/model_trainer/best.pt"
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)
