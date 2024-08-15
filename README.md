---

# Disease Prediction Using Machine Learning

Welcome to the Disease Prediction repository! This project involves training five different machine learning models, each designed to predict a specific disease. The models use various machine learning algorithms to achieve high accuracy in predicting conditions like brain tumors, heart health, diabetes, lung health, and chest health.

## Project Overview

### Objectives

- **Brain Tumor Prediction:** Using Convolutional Neural Networks (CNNs) to predict the presence of brain tumors from MRI scans.
- **Heart Health Prediction:** Applying Logistic Regression to assess heart health based on clinical data.
- **Diabetic Prediction:** Utilizing Random Forest for predicting diabetes based on patient information.
- **Lung Health Prediction:** Implementing K-Nearest Neighbors (KNN) to detect lung cancer.
- **Chest Health Prediction:** Employing CNNs to predict chest health issues using X-ray images.

### Algorithms and Accuracies

- **K-Nearest Neighbors (KNN):**  
  - **Disease:** Lung Cancer  
  - **Accuracy:** 100%

- **Convolutional Neural Networks (CNN):**  
  - **Disease:** Brain Tumor  
  - **Accuracy:** 93%  
  - **Disease:** Chest Health (X-Ray)  
  - **Accuracy:** 95%

- **Random Forest:**  
  - **Disease:** Diabetic Prediction  
  - **Accuracy:** 96%

- **Logistic Regression:**  
  - **Disease:** Heart Health Prediction  
  - **Accuracy:** 92%

## Installation

### Requirements

Ensure you have Python 3.x installed, along with the following packages:

```bash
pip install numpy pandas scikit-learn tensorflow keras opencv-python matplotlib seaborn
```

### Repository Setup

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/mahataummadi/VITA_SCAN.git
cd VITA_SCAN
```

## Usage

### 1. Data Preparation

Before training the models, ensure that you have your datasets organized. The datasets should be preprocessed and split into training and testing sets.

### 2. Model Training

You can train each model separately by running the corresponding scripts:

- **KNN for Lung Cancer Prediction:**
  ```bash
  python train_knn_lung_cancer.py
  ```

- **CNN for Brain Tumor Prediction:**
  ```bash
  python train_cnn_brain_tumor.py
  ```

- **CNN for Chest X-Ray Prediction:**
  ```bash
  python train_cnn_chest_xray.py
  ```

- **Random Forest for Diabetic Prediction:**
  ```bash
  python train_rf_diabetic.py
  ```

- **Logistic Regression for Heart Health Prediction:**
  ```bash
  python train_lr_heart_health.py
  ```

### 3. Model Evaluation

After training, evaluate the models using the provided evaluation scripts:

- **KNN for Lung Cancer Prediction:**
  ```bash
  python evaluate_knn_lung_cancer.py
  ```

- **CNN for Brain Tumor Prediction:**
  ```bash
  python evaluate_cnn_brain_tumor.py
  ```

- **CNN for Chest X-Ray Prediction:**
  ```bash
  python evaluate_cnn_chest_xray.py
  ```

- **Random Forest for Diabetic Prediction:**
  ```bash
  python evaluate_rf_diabetic.py
  ```

- **Logistic Regression for Heart Health Prediction:**
  ```bash
  python evaluate_lr_heart_health.py
  ```

### 4. Predictions

Once the models are trained and evaluated, you can use them to make predictions on new data:

```python
from models import load_trained_model

model = load_trained_model('path_to_model.h5')
predictions = model.predict(new_data)
```

## Results

### Accuracies:

- **KNN for Lung Cancer:** 100%
- **CNN for Brain Tumor:** 93%
- **CNN for Chest X-Ray:** 95%
- **Random Forest for Diabetic Prediction:** 96%
- **Logistic Regression for Heart Health:** 92%

Include visualizations such as confusion matrices, ROC curves, and example predictions in this section.

## Contributions

Feel free to fork this repository, submit issues, or make pull requests. Contributions are welcome!


## Contact

For any questions or feedback, please reach out at mahata2657@gmail.com.


Link for the website: https://mellifluous-hamster-da427b.netlify.app/
Overviwe of the project: https://drive.google.com/file/d/1dzahJkshf2mK2N7tPwVRxJbL2EbdCNki/view?usp=sharing
