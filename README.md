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
├── data_preprocessing.py          # Data cleaning and preprocessing scripts
├── model_training.py             # Model training and evaluation
├── notebooks/                    # Jupyter notebooks for each step
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_selection.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_evaluation.ipynb
├── app.py                        # Streamlit web application
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

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 🚀 Deployment with Ngrok

### 1. Install Ngrok

Download and install Ngrok from [ngrok.com](https://ngrok.com/)

### 2. Create Ngrok Account

1. Sign up for a free Ngrok account
2. Get your authtoken from the dashboard
3. Configure Ngrok with your authtoken:

```bash
ngrok config add-authtoken YOUR_AUTHTOKEN
```

### 3. Deploy the Application

1. Start your Streamlit app:
```bash
streamlit run app.py
```

2. In a new terminal, expose your app using Ngrok:
```bash
ngrok http 8501
```

3. Ngrok will provide a public URL (e.g., `https://abc123.ngrok.io`) that you can share with others.

### 4. Access Your Deployed App

- Use the public URL provided by Ngrok to access your application from anywhere
- The URL will remain active as long as your Ngrok session is running

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

## 🎯 Usage

1. **Web Interface**: 
   - Enter patient health data in the input fields
   - Click "Predict Heart Disease" for instant results
   - View data visualizations and trends

2. **API Usage**:
   ```python
   import joblib
   import pandas as pd
   
   # Load trained model
   pipeline = joblib.load('model_pipeline.pkl')
   
   # Prepare input data
   input_data = pd.DataFrame([{
       'age': 50,
       'trestbps': 120,
       'chol': 200,
       'thalach': 150,
       'oldpeak': 1.5
   }])
   
   # Make prediction
   prediction = pipeline.predict(input_data)
   ```

## 🔧 Development

### Adding New Features

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Commit changes: `git commit -m 'Add new feature'`
5. Push to branch: `git push origin feature-name`
6. Submit a pull request

### Running Tests

```bash
# Run model training script
python model_training.py

# Run data preprocessing
python data_preprocessing.py
```

## 📝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the dataset
- Streamlit team for the amazing web framework
- Scikit-learn contributors for the ML library
- Ngrok for easy deployment solution

## 📞 Support

If you have any questions or need help, please:
1. Check the [Issues](https://github.com/yourusername/heart-disease-prediction/issues) page
2. Create a new issue if your problem isn't already addressed
3. Contact the maintainers

---

⭐ **Star this repository if you found it helpful!**
