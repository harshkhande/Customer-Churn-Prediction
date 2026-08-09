# 📊 Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. This project predicts whether a customer is likely to leave (churn) based on their demographic information, services subscribed, contract type, billing information, and account history.

The project implements an end-to-end Machine Learning pipeline, from data preprocessing to deployment using Streamlit.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Encoding using LabelEncoder
- Machine Learning Model Training
- Model Evaluation
- Customer Churn Prediction
- Feature Importance Analysis
- Interactive Streamlit Web Application
- Churn Probability Prediction
- Business Recommendations based on prediction

---

## 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── customer_churn_preprocessed.csv
│
├── models/
│   ├── random_forest_model.pkl
│   ├── decision_tree_model.pkl
│   ├── logistic_regression_model.pkl
│   └── label_encoders.pkl
│
├── notebooks/
│   ├── 1_Data_Loading.ipynb
│   ├── 2_Preprocessing.ipynb
│   ├── 3_Model_Training.ipynb
│   ├── 4_Model_Evaluation.ipynb
│   ├── 5_Customer_Churn_Prediction.ipynb
│   └── 6_Feature_Importance.ipynb
│
├── results/
│   └── feature_importance.csv
│
└── screenshots/
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib

---

## 📊 Machine Learning Models

The following classification models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Best Performing Model

**Random Forest Classifier**

---

## 📈 Important Features

Top important features identified by the Random Forest model:

1. TotalCharges
2. MonthlyCharges
3. tenure
4. Contract
5. PaymentMethod

---

## 🖥️ Streamlit Application

The web application allows users to:

- Enter customer information
- Predict customer churn
- View churn probability
- View customer retention recommendations

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Customer-Churn-Prediction.git
```

Move into the project folder:

```bash
cd Customer-Churn-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add screenshots of your Streamlit application here.

Example:

- Home Page
- Prediction Result
- Business Recommendation

---

## 📚 Dataset

Dataset: Telco Customer Churn Dataset

Number of Records: **7043**

Features Used: **19**

Target Variable: **Churn**

---

## 👨‍💻 Author

**Harshvardhan Khande**

Computer Engineering Student

Machine Learning | Data Analytics | Artificial Intelligence

---

## ⭐ Future Improvements

- Hyperparameter tuning
- Model comparison dashboard
- SHAP Explainable AI
- Cloud deployment
- REST API integration
- Docker containerization

---

## 📄 License

This project is developed for educational and portfolio purposes.