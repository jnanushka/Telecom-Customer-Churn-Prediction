import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Page configuration
st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Polished modern theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero Banner */
    .hero-container {
        padding: 2.2rem 2rem;
        background: radial-gradient(circle at 10% 20%, #0f172a 0%, #1e293b 100%);
        border-radius: 16px;
        color: #ffffff;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .hero-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
        letter-spacing: -0.02em;
    }
    .hero-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        margin: 0;
    }

    /* Section Cards */
    .section-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.25rem 1.25rem 0.75rem 1.25rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
    }
    .section-header {
        font-size: 1.05rem;
        font-weight: 600;
        color: #0f172a;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 0.5rem;
    }

    /* Result Card Styling */
    .result-box {
        border-radius: 14px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        border: 1px solid #e2e8f0;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    .badge-churn {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        border: 1px solid #fecaca;
    }
    .badge-safe {
        background-color: #dcfce7;
        color: #166534;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        border: 1px solid #bbf7d0;
    }

    /* Primary CTA Button */
    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: #ffffff;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        border: none;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #1d4ed8;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# Load trained model and expected columns
@st.cache_resource
def load_assets():
    with open('model.sav', 'rb') as f_model:
        model = pickle.load(f_model)
    with open('columns.pkl', 'rb') as f_cols:
        expected_cols = pickle.load(f_cols)
    return model, expected_cols

try:
    model, expected_cols = load_assets()
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# Header Banner
st.markdown("""
<div class="hero-container">
    <div class="hero-title">⚡ Customer Churn Prediction Engine</div>
    <div class="hero-subtitle">Input customer demographics, services, and billing contracts to assess retention risk.</div>
</div>
""", unsafe_allow_html=True)

# Layout Inputs
col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    st.markdown('<div class="section-card"><div class="section-header">👤 Customer Demographics</div>', unsafe_allow_html=True)
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-card"><div class="section-header">📶 Subscribed Services</div>', unsafe_allow_html=True)
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service Provider", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="section-card"><div class="section-header">💳 Contract & Billing</div>', unsafe_allow_html=True)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox(
        "Payment Method", 
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=18.0, max_value=130.0, value=65.0, step=0.5)
    total_charges = st.number_input("Total Charges ($)", min_value=18.0, max_value=9000.0, value=float(tenure * monthly_charges), step=10.0)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
predict_btn = st.button("Analyze Churn Risk")

if predict_btn:
    raw_input = {
        'gender': gender,
        'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }
    
    input_df = pd.DataFrame([raw_input])
    encoded_df = pd.get_dummies(input_df)
    final_df = encoded_df.reindex(columns=expected_cols, fill_value=0)
    
    prediction = model.predict(final_df)[0]
    has_proba = hasattr(model, "predict_proba")
    proba = model.predict_proba(final_df)[0][1] if has_proba else None

    if prediction == 1:
        prob_str = f"Estimated probability: <b>{proba * 100:.1f}%</b>" if proba is not None else "Recommended action: Offer contract incentives or discounts."
        st.markdown(f"""
        <div class="result-box" style="border-left: 5px solid #ef4444;">
            <span class="badge-churn">High Risk</span>
            <h3 style="color: #991b1b; margin-top: 0.75rem;">Customer is Likely to Churn</h3>
            <p style="color: #64748b; margin-bottom: 0;">{prob_str}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        prob_str = f"Estimated churn risk: <b>{proba * 100:.1f}%</b>" if proba is not None else "Recommended action: Customer relationship is healthy."
        st.markdown(f"""
        <div class="result-box" style="border-left: 5px solid #22c55e;">
            <span class="badge-safe">Low Risk</span>
            <h3 style="color: #166534; margin-top: 0.75rem;">Customer is Likely to Stay (Loyal)</h3>
            <p style="color: #64748b; margin-bottom: 0;">{prob_str}</p>
        </div>
        """, unsafe_allow_html=True)