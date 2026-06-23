# Human Pose Estimation using COCO and MPII Datasets

## Overview

This project focuses on **human pose estimation and keypoint detection** using publicly available datasets such as **COCO** and **MPII**. The repository contains a collection of Jupyter notebooks covering the complete pipeline from dataset acquisition and preprocessing to model development, training, and visualization of predicted keypoints.

The primary objective is to build and train deep learning models capable of accurately detecting human body keypoints, with special emphasis on **leg keypoint localization** and custom keypoint extraction workflows.

---

## Features

* Download and prepare COCO and MPII datasets.
* Generate custom annotations for leg keypoint detection.
* Create datasets containing leg keypoints along with other body keypoints.
* Image preprocessing and augmentation pipeline.
* Deep learning model development for pose estimation.
* Model training and evaluation.
* Visualization utilities for drawing detected keypoints.
* Modular utility functions for configuration management and annotation conversion.

---

## Project Structure

```text
pose-estimation/
│
├── LICENSE
├── README.md
│
├── notebooks/
│   ├── COCO Set Preparation for Legs Keypoints Along with Other Classes.ipynb
│   ├── COCO Set Preparation for Legs Keypoints Detection.ipynb
│   ├── Creating Model.ipynb
│   ├── Downloading COCO DataSet.ipynb
│   ├── Download MPII DataSet.ipynb
│   ├── Draw KeyPoints.ipynb
│   ├── Model Training.ipynb
│   └── Preprocess Images.ipynb
│
└── utils/
    ├── __init__.py
    ├── configs.py
    ├── conversions.py
    └── draw.py
```

---

## Workflow

### 1. Dataset Download

Download the required datasets:

* **COCO Dataset**

  * `Downloading COCO DataSet.ipynb`

* **MPII Human Pose Dataset**

  * `Download MPII DataSet.ipynb`

### 2. Dataset Preparation

Prepare and customize annotations for training:

* `COCO Set Preparation for Legs Keypoints Detection.ipynb`
* `COCO Set Preparation for Legs Keypoints Along with Other Classes.ipynb`

These notebooks create training-ready datasets focused on leg keypoints and full-body keypoint configurations.

### 3. Image Preprocessing

Perform image cleaning, resizing, normalization, and annotation transformations:

* `Preprocess Images.ipynb`

### 4. Model Development

Design and configure the pose estimation architecture:

* `Creating Model.ipynb`

### 5. Model Training

Train the pose estimation model on prepared datasets:

* `Model Training.ipynb`

### 6. Visualization

Visualize annotations and model predictions:

* `Draw KeyPoints.ipynb`

---

## Utilities

### `utils/configs.py`

Contains project-wide configuration settings such as:

* Dataset paths
* Image dimensions
* Training parameters
* Keypoint definitions

### `utils/conversions.py`

Utility functions for:

* Annotation conversion
* Coordinate transformations
* Dataset format adaptation

### `utils/draw.py`

Visualization utilities for:

* Drawing keypoints
* Skeleton rendering
* Prediction inspection

---

## Datasets

### COCO Dataset

The Common Objects in Context (COCO) dataset provides large-scale object detection, segmentation, and human keypoint annotations.

Key features:

* Thousands of annotated human instances
* Standard benchmark for pose estimation
* Multiple body keypoints per person

### MPII Human Pose Dataset

The MPII dataset contains images of humans performing diverse activities with detailed body joint annotations.

Key features:

* Real-world activities
* Challenging poses
* Widely used pose estimation benchmark

---

## Requirements

Recommended environment:

```bash
Python 3.8+
Jupyter Notebook
TensorFlow / Keras
NumPy
OpenCV
Matplotlib
Pandas
Scikit-learn
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Recommended execution order:

1. Downloading COCO DataSet.ipynb
2. Download MPII DataSet.ipynb
3. COCO Set Preparation for Legs Keypoints Detection.ipynb
4. COCO Set Preparation for Legs Keypoints Along with Other Classes.ipynb
5. Preprocess Images.ipynb
6. Creating Model.ipynb
7. Model Training.ipynb
8. Draw KeyPoints.ipynb

---

## Applications

This project can be extended for:

* Human activity recognition
* Sports analytics
* Gait analysis
* Motion tracking
* Healthcare and rehabilitation systems
* Human-computer interaction
* Surveillance and safety monitoring

---

## Future Improvements

* Real-time inference support
* Multi-person pose estimation
* Lightweight deployment models
* Transfer learning with state-of-the-art architectures
* Integration with video-based pose tracking
* Deployment using TensorFlow Lite or ONNX

---

## License

This project is distributed under the terms specified in the LICENSE file.

