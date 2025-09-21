# Heart Disease Prediction App

A machine learning application that predicts heart disease using patient health data. The project includes data preprocessing, model training, and a Streamlit web interface for real-time predictions.

## 🏥 Project Overview

This project uses the UCI Heart Disease dataset to build and deploy a machine learning model that can predict whether a patient has heart disease based on various health indicators such as age, blood pressure, cholesterol levels, and other medical measurements.

## 🚀 Features

- **Data Preprocessing**: Comprehensive data cleaning, encoding, and feature selection
- **Machine Learning Models**: Multiple algorithms including Logistic Regression, Decision Tree, Random Forest, and SVM
- **Feature Selection**: Advanced feature selection techniques (Random Forest importance, RFE)
- **Interactive Web App**: Streamlit-based user interface for real-time predictions
- **Data Visualization**: Exploratory data analysis with interactive plots
- **Model Deployment**: Easy deployment using Ngrok for public access

## 📁 Project Structure

```
heart-disease-prediction/
├── heart-disease-model          # Jupyter notebooks for each step
├── app.py                       # Streamlit web application
├── model_pipeline.pkl           # Trained model pipeline
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Deployment with Ngrok
 Ngrok provide a public URL "https://d4177aeda661.ngrok-free.app" that you can explore the app.

## 📊 Dataset

The project uses the Heart Disease dataset from UCI Machine Learning Repository:
- **Dataset ID**: 45
- **Features**: 13 medical attributes
- **Target**: Binary classification (presence/absence of heart disease)

### Key Features:
- `age`: Age in years
- `trestbps`: Resting blood pressure
- `chol`: Serum cholesterol
- `thalach`: Maximum heart rate achieved
- `oldpeak`: ST depression induced by exercise

## 🤖 Machine Learning Pipeline

1. **Data Loading**: Fetch data from UCI repository
2. **Data Cleaning**: Handle missing values and data types
3. **Feature Encoding**: Label encoding for categorical variables
4. **Feature Scaling**: Standardization of numerical features
5. **Feature Selection**: RFE and Random Forest importance
6. **Model Training**: Multiple algorithms comparison
7. **Model Evaluation**: Cross-validation and metrics
8. **Model Persistence**: Save trained pipeline

## 📈 Model Performance

The Random Forest classifier achieved the best performance with:
- **Accuracy**: ~85%
- **Precision**: ~84%
- **Recall**: ~85%
- **F1-Score**: ~84%

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

- **Basmala Hesham** -

