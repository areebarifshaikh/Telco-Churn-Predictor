import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


# --- 1. Load the Model ---
# We use st.cache_resource to load the model only once, improving performance
@st.cache_resource
def load_model():
    # Load the entire pipeline (preprocessor + best model)
    try:
        model = joblib.load('best_churn_model.pkl')
        return model
    except FileNotFoundError:
        st.error("Error: 'best_churn_model.pkl' not found. Make sure the model file is in the same directory.")
        return None


pipeline = load_model()

# --- 2. GUI Setup ---
st.set_page_config(page_title="Telco Customer Churn Predictor", layout="centered")

st.title("📞 Telco Customer Churn Predictor")
st.markdown("Enter the customer details below to predict their likelihood of churning (leaving the company).")

if pipeline:
    # --- 3. Sidebar for User Input ---
    # Organized input using st.sidebar or st.columns for better aesthetics

    st.subheader("Customer Profile")

    # Group 1: Demographics
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ('Male', 'Female'))
        senior_citizen = st.selectbox("Senior Citizen", ('No', 'Yes'),
                                      format_func=lambda x: 'Yes' if x == 'Yes' else 'No')
    with col2:
        partner = st.selectbox("Partner", ('No', 'Yes'))
        dependents = st.selectbox("Dependents", ('No', 'Yes'))
    with col3:
        tenure = st.slider("Tenure (Months)", 1, 72, 12)

    # Group 2: Services
    st.subheader("Service Usage")
    col4, col5, col6 = st.columns(3)
    with col4:
        phone_service = st.selectbox("Phone Service", ('Yes', 'No'))
        multiple_lines = st.selectbox("Multiple Lines", ('No', 'Yes', 'No phone service'))
    with col5:
        internet_service = st.selectbox("Internet Service", ('DSL', 'Fiber optic', 'No'))
        online_security = st.selectbox("Online Security", ('No', 'Yes', 'No internet service'))
    with col6:
        online_backup = st.selectbox("Online Backup", ('No', 'Yes', 'No internet service'))
        tech_support = st.selectbox("Tech Support", ('No', 'Yes', 'No internet service'))

    # Group 3: Streaming & Protection
    col7, col8, col9 = st.columns(3)
    with col7:
        device_protection = st.selectbox("Device Protection", ('No', 'Yes', 'No internet service'))
    with col8:
        streaming_tv = st.selectbox("Streaming TV", ('No', 'Yes', 'No internet service'))
    with col9:
        streaming_movies = st.selectbox("Streaming Movies", ('No', 'Yes', 'No internet service'))

    # Group 4: Billing
    st.subheader("Billing Details")
    col10, col11 = st.columns(2)
    with col10:
        contract = st.selectbox("Contract Type", ('Month-to-month', 'One year', 'Two year'))
        paperless_billing = st.selectbox("Paperless Billing", ('Yes', 'No'))
    with col11:
        payment_method = st.selectbox("Payment Method",
                                      ('Electronic check', 'Mailed check',
                                       'Bank transfer (automatic)', 'Credit card (automatic)'))
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=18.0, max_value=120.0, value=70.0, step=0.01)

    # Calculate Total Charges based on tenure * monthly charges (used as a default approximation)
    total_charges = monthly_charges * tenure

    # Hidden input for Total Charges (for model consistency)
    # The original model used TotalCharges, so we estimate it here.
    # Note: If the customer is new (tenure=1), TotalCharges is equal to MonthlyCharges
    st.markdown(f"*(Estimated Total Charges: ${total_charges:.2f})*",
                help="Calculated as Monthly Charges * Tenure for model consistency.")

    # --- 4. Prepare Data for Prediction ---

    # Map 'Yes'/'No' for Senior Citizen to 1/0 for model input consistency
    senior_citizen_val = 1 if senior_citizen == 'Yes' else 0

    # Create a DataFrame matching the structure AND column names of the training data
    data = {

        'Gender': [gender],
        'Senior_Citizen': [senior_citizen_val],  # Note: uses the integer variable
        'Partner': [partner],
        'Dependents': [dependents],
        'Tenure': [tenure],


        'Phone_Service': [phone_service],
        'Multiple_Lines': [multiple_lines],
        'Internet_Service': [internet_service],
        'Online_Security': [online_security],
        'Online_Backup': [online_backup],
        'Device_Protection': [device_protection],
        'Tech_Support': [tech_support],
        'Streaming_TV': [streaming_tv],
        'Streaming_Movies': [streaming_movies],


        'Contract': [contract],
        'Paperless_Billing': [paperless_billing],
        'Payment_Method': [payment_method],


        'Monthly_Charges': [monthly_charges],
        'Total_Charges': [total_charges]
    }
    input_df = pd.DataFrame(data)

    # --- 5. Prediction Button ---
    st.markdown("---")
    if st.button("Predict Churn Risk", help="Click to run the model prediction."):

        with st.spinner('Analyzing customer profile...'):
            # Predict
            prediction = pipeline.predict(input_df)
            # Predict probability of churn (class 1)
            churn_probability = pipeline.predict_proba(input_df)[:, 1][0]

            st.subheader("Prediction Result")

            if prediction[0] == 1:
                st.error(f"🔴 High Risk of Churn!")
                st.metric(label="Churn Probability", value=f"{churn_probability:.2%}")
                st.warning(
                    "Immediate action is recommended (e.g., offer a contract renewal discount, tech support follow-up).")
            else:
                st.success(f"🟢 Low Risk of Churn.")
                st.metric(label="Churn Probability", value=f"{churn_probability:.2%}")
                st.info("Customer is likely to remain subscribed.")

else:
    st.error("Model not loaded. Please check the console for errors.")