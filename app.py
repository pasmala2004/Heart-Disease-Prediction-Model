import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load trained model pipeline
pipeline = joblib.load('model_pipeline.pkl')


from ucimlrepo import fetch_ucirepo
heart_disease = fetch_ucirepo(id=45)
X_viz = heart_disease.data.features
y_viz = heart_disease.data.targets

# Handle missing values by fill null
X_viz = X_viz.ffill()
y_viz = y_viz.ffill()

# Perform data encoding and standardization for visualization data
from sklearn.preprocessing import LabelEncoder, StandardScaler
le_viz = LabelEncoder()
X_viz_encoded = X_viz.apply(le_viz.fit_transform)
st_viz = StandardScaler()
X_viz_scaled = pd.DataFrame(st_viz.fit_transform(X_viz_encoded), columns=X_viz_encoded.columns)

# Add the target variable to the visualization dataframe
X_viz_scaled['target'] = y_viz.values.ravel()


st.title('Heart Disease Prediction App')
st.write('Input your health data to get a real-time prediction!')


# User input for prediction
st.header('Enter Your Health Data')
feature_names = {
    'age': 'Age',
    'trestbps': 'Resting Blood Pressure (trestbps)',
    'chol': 'Cholesterol (chol)',
    'thalach': 'Maximum Heart Rate Achieved (thalach)',
    'oldpeak': 'ST depression induced by exercise relative to rest (oldpeak)'
}
user_input = {}
for feature_key, feature_label in feature_names.items():
    user_input[feature_key] = st.number_input(f'Enter {feature_label}', value=0.0)

if st.button('Predict Heart Disease'):
    input_df = pd.DataFrame([user_input])
    prediction = pipeline.predict(input_df)[0]
    st.success(f'Prediction: {"Heart Disease" if prediction == 1 else "No Heart Disease"}')

st.write('---')
st.header('Explore Heart Disease Trends')

st.write('### Feature Distributions')
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(20, 15))
axes = axes.flatten()
for i, col in enumerate(X_viz_scaled.columns):
    if col != 'target':
        sns.histplot(data=X_viz_scaled, x=col, kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
plt.tight_layout()
st.pyplot(fig)


st.write('### Heart Disease Distribution')
if 'target' in X_viz_scaled.columns:
    st.bar_chart(X_viz_scaled['target'].value_counts())
else:
    st.info('No target column found for distribution plot.')