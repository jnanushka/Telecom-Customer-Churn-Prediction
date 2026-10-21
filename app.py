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
