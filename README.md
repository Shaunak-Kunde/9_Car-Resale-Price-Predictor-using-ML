# 🚗 Car Resale Price Predictor – Machine Learning Project

I built this project to explore how machine learning can be applied to a practical problem – predicting the resale price of used cars. The project demonstrates the complete workflow from data cleaning and preprocessing to model training and deployment in an interactive **Streamlit** web app.

The app is deployed online on **Streamlit Cloud** so that anyone can try it directly in the browser.

---

## 🌐 Live App

The app is publicly accessible here:  
[Car Resale Price Predictor on Streamlit](https://car-resale-value.streamlit.app/)

---

## 📂 Project Structure

├── application.py # Main Streamlit application
├── quikr_car.csv # Original Quikr used car dataset
├── quickr_car_cleaned_by_shaunak.csv # Cleaned dataset used for training
├── LinearRegressionModel_Shaunak.pkl # Trained regression model
├── requirements.txt # Project dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🔑 Features

- Upload your own dataset or use the sample dataset to explore car details.
- Input car attributes such as brand, model, year, kilometers driven, fuel type, etc.
- Get instant predictions of resale price using a trained regression model.
- Clean and simple interface built with **Streamlit** for easy user interaction.

---

## ⚙️ Tech Stack

- **Python** – Data handling and model training (`pandas`, `scikit-learn`, `joblib`)
- **Streamlit** – Web app development and deployment
- **GitHub + Streamlit Cloud** – Version control and hosting

---

## 🔍 Workflow Overview

### 1. Data Cleaning & Preprocessing
- Handled missing values and formatted price columns.
- Converted categorical variables into numeric encodings for model compatibility.
- Selected relevant features for prediction.

### 2. Model Training
- Trained a **Linear Regression** model on the cleaned dataset.
- Evaluated the model using metrics like R² and Mean Squared Error.
- Serialized the trained model using **Joblib** for deployment.

### 3. Web App Development
- Built the interactive frontend using **Streamlit**.
- Users can select car features and get real-time resale price predictions.
- Uploaded or sample datasets can also be explored for predictions.

### 4. Deployment
- Deployed the app on **Streamlit Cloud** for public access.

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Shaunak-Kunde/9_Car-Resale-Price-Predictor-using-ML.git
   cd 9_Car-Resale-Price-Predictor-using-ML
Install dependencies:

bash
pip install -r requirements.txt
Run the Streamlit app:

bash
streamlit run application.py
📊 Dataset
The model is trained on Quikr’s used car dataset. I performed cleaning and preprocessing including:

Handling missing values
Formatting prices and numeric features
Encoding categorical variables

### Note: Predictions are estimates based on dataset patterns and may not reflect exact market values.

## 🌟 Learning Outcomes
Cleaned and preprocessed real-world messy datasets.

Trained and saved regression models with scikit-learn.

Developed and deployed an interactive web app using Streamlit Cloud.

Gained experience in feature selection for real-world prediction tasks.

🙌 Acknowledgement
## Dataset source: Quikr used cars
