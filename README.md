Car Resale Price Predictor 🚗💰

This project is something I built to explore how machine learning can be applied to a very practical problem – predicting the resale price of used cars. The idea came from browsing used car listings and noticing how unpredictable prices can be depending on the model, brand, year, and condition.

The app is deployed on Streamlit Cloud so that anyone can try it out directly in the browser.

🔑 Features

Upload or use sample data to explore car details.

Enter car features (brand, model, year, km driven, fuel type, etc.) and get an instant predicted resale price.

Clean and simple Streamlit interface for easy use.

Built using a machine learning regression model trained on Quikr’s used car dataset.

📂 Project Structure
.
├── application.py      # Main Streamlit app
├── quikr_car.csv       # Original dataset
├── quickr_car_cleaned_by_shaunak.csv  # Cleaned dataset
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

⚙️ Tech Stack

Python (pandas, scikit-learn, joblib)

Streamlit for the UI

GitHub + Streamlit Cloud for deployment

🚀 How to Run Locally

Clone this repo

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run application.py

📊 Dataset

The model is trained on Quikr’s used car dataset. I did some basic cleaning (handling missing values, formatting prices, etc.) before using it for training.

Note: Predictions are based on patterns in the dataset and should be taken as rough estimates, not exact market values.

🌟 What I Learned

How to clean and preprocess messy real-world datasets.

Training and saving regression models with scikit-learn.

Deploying a data science project using Streamlit Cloud.

The importance of feature selection when working with real-world problems.

🙌 Acknowledgement

Dataset source: Quikr used cars.
