# 📊 Cell Segmentation using YOLOv8

## 📝 **Project Description**

This project performs **cell segmentation** using the **YOLOv8** model. It identifies and segments cells from microscopy images, producing labeled outputs with bounding boxes and masks. The project includes training, inference, and evaluation functionalities with configurable parameters.

---

![cellseg](https://github.com/user-attachments/assets/8d0e8169-0088-4ef8-b493-2f5f11f2aea9)


## 🚀 **Features**

- **Training:** Uses YOLOv8 for training the model on cell images.
- **Inference:** Segments cells and outputs labeled images.
- **Metrics:** Includes evaluation metrics for model performance.
- **Visualization:** Displays and saves segmentation results.

---

## 🔥 **Project Structure**

```
Cell_Segmentation-main/
├── data/
│   ├── train/                  # Training images
│   ├── test/                   # Testing images
│   └── labels/                 # Labels for segmentation
├── models/                     # YOLOv8 pre-trained models
├── outputs/                    # Output results of segmentation
├── utils/                      # Helper scripts
│   ├── dataset_utils.py        # Dataset handling functions
│   ├── visualization.py        # Visualization helpers
│   └── metrics.py              # Evaluation metrics
├── app.py                      # Main application script
├── requirements.txt            # Dependencies
├── config.yaml                 # YOLO model configuration
└── main.py                     # Training and inference script
```

---

## ⚙️ **Installation and Setup**

### **1. Clone the repository:**

```bash
git clone <repository_link>
cd Cell_Segmentation-main
```

### **2. Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # For Linux
venv\Scripts\activate     # For Windows
```

### **3. Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🛠️ **Usage**

### **1. Train the Model:**

```bash
python main.py --mode train --config config.yaml
```

### **2. Perform Inference:**

```bash
python main.py --mode inference --config config.yaml
```

### **3. Run the Application:**

```bash
python app.py
```

---

## 🧪 **Configuration**

The project uses a `config.yaml` file to manage the model settings. You can modify the following parameters:

```yaml
model: 'yolov8n-seg.pt'          # YOLOv8 model
image_size: 640                   # Input image size
batch_size: 16                    # Batch size
epochs: 50                        # Number of training epochs
```

---

## 📊 **Evaluation Metrics**

The project calculates the following metrics:

- **mAP** (Mean Average Precision)
- **IoU** (Intersection over Union)
- **Recall & Precision**

---

## 🖼️ **Visualization**

Segmented images are saved in the `outputs/` folder. You can visualize the results by running:

```bash
python utils/visualization.py
```

---

## 🛠️ **Troubleshooting**

- Ensure all dependencies in `requirements.txt` are installed.
- Adjust the `config.yaml` parameters if performance is low.
- Check the `outputs/` folder for results after inference.

---

## 📚 **References**

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [OpenCV](https://opencv.org/)
- [Python](https://www.python.org/)

---

## 👩‍💻 **Contributing**

Feel free to contribute to this project by submitting pull requests or reporting issues.

---

## ⚖️ **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 📬 **Contact**

For any inquiries or issues, please contact: **Viplove Thakran**

