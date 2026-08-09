import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Load Model and Encoders
# --------------------------------------------------
model = joblib.load(
    r"C:\Users\Khande\Desktop\project 2\Customer-Churn-Prediction\models\random_forest_model.pkl"
)

label_encoders = joblib.load(
    r"C:\Users\Khande\Desktop\project 2\Customer-Churn-Prediction\models\label_encoders.pkl"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("📊 Customer Churn Prediction")

st.sidebar.markdown("""
### About this Project

This application predicts whether a telecom customer is likely to churn using a **Random Forest Machine Learning Model**.

### Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

### Model
Random Forest Classifier
""")

# --------------------------------------------------
# Main Title
# --------------------------------------------------
st.title("📊 Customer Churn Prediction")

st.markdown("""
Predict whether a telecom customer is likely to churn using a trained **Random Forest Machine Learning model**.
""")

st.markdown("---")

st.header("Customer Information")

# --------------------------------------------------
# Two Columns
# --------------------------------------------------
col1, col2 = st.columns(2)

# ==========================
# LEFT COLUMN
# ==========================
with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

# ==========================
# RIGHT COLUMN
# ==========================
with col2:

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

st.markdown("---")

if st.button("🔍 Predict Churn"):

    # ----------------------------------------
    # Create Input Data
    # ----------------------------------------
    input_data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    input_df = pd.DataFrame([input_data])

    # ----------------------------------------
    # Encode Categorical Columns
    # ----------------------------------------
    categorical_columns = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod"
    ]

    for column in categorical_columns:
        input_df[column] = label_encoders[column].transform(input_df[column])

    input_df["SeniorCitizen"] = input_df["SeniorCitizen"].map({
        "No": 0,
        "Yes": 1
    })

    # ----------------------------------------
    # Prediction
    # ----------------------------------------
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.markdown("---")
    st.header("Prediction Result")

    if prediction == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")

    # ----------------------------------------
    # Metrics
    # ----------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🟢 Staying Probability",
            f"{probability[0]*100:.2f}%"
        )

    with col2:
        st.metric(
            "🔴 Churning Probability",
            f"{probability[1]*100:.2f}%"
        )

    # ----------------------------------------
    # Confidence
    # ----------------------------------------
    st.subheader("Prediction Confidence")

    confidence = max(probability)

    st.progress(float(confidence))

    st.write(f"Model Confidence: **{confidence*100:.2f}%**")

    # ----------------------------------------
    # Business Recommendation
    # ----------------------------------------
    st.subheader("Business Recommendation")

    if prediction == 1:

        st.warning("""
### ⚠ High Churn Risk

Recommended Actions

- Contact the customer immediately.
- Offer a retention discount.
- Suggest a long-term contract.
- Provide loyalty rewards.
- Improve customer support.
- Assign a customer success executive.
""")

    else:

        st.success("""
### ✅ Low Churn Risk

Recommended Actions

- Maintain current service quality.
- Continue customer engagement.
- Offer premium plans.
- Provide loyalty rewards.
- Cross-sell additional telecom services.
""")

    # ----------------------------------------
    # Probability Chart
    # ----------------------------------------
    st.subheader("Prediction Probability")

    probability_df = pd.DataFrame({
        "Category": ["Stay", "Churn"],
        "Probability": [
            probability[0]*100,
            probability[1]*100
        ]
    })

    st.bar_chart(
        probability_df.set_index("Category")
    )

# ----------------------------------------
# Footer
# ----------------------------------------
st.markdown("---")

st.markdown(
    """
<div style='text-align:center;'>

### Customer Churn Prediction System

Developed by **Harshvardhan Khande**

Computer Engineering | Machine Learning Project

</div>
""",
unsafe_allow_html=True
)