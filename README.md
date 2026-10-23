# ⚡ Telecom Customer Churn Intelligence & Retention Studio

An enterprise-grade, end-to-end Machine Learning analytics platform and prescriptive retention engine built with **Streamlit**, **Scikit-Learn**, and **Altair**. 

This platform transforms raw customer usage, billing, and demographic data into real-time churn predictions, risk stratification, and explainable, rule-based retention playbooks designed for customer success teams and executive leadership.

---

## 🌟 Key Features

### 1. 📊 Executive Overview & KPI Dashboard
* **Real-Time Portfolio Metrics:** Instant visibility into Total Accounts Analyzed, Predicted Churners, Projected Churn Rate (%), and Retained Customer Base.
* **Calibrated Risk Stratification:** Dynamic cohort classification into **Critical Risk** ($P \ge 70\%$), **Medium Risk** ($35\% \le P < 70\%$), and **Low Risk** ($P < 35\%$).
* **Flexible Cutoff Sliders:** Interactive sidebar controls to customize risk thresholds according to business risk tolerance.

### 2. 📈 Behavioral & Contractual Analytics
* **6 Interactive Visualizations (Altair):**
  * *Churn vs. Retained Distribution:* Donut chart summarizing cohort health.
  * *Churn by Contract Type:* Comparative analysis showing month-to-month volatility vs. multi-year contract stability.
  * *Tenure Drop-Off Dynamics:* Lifecycle curve highlighting peak vulnerability in early onboarding months (1–12).
  * *Monthly Charges Density:* Boxplot comparing price sensitivity between churners and retained accounts.
  * *Internet Service Breakdown:* Fiber optic vs. DSL churn patterns.
  * *Risk Tier Distribution:* Cohort breakdown across prioritized risk tiers.

### 3. 🔍 Single-Customer Prediction Simulator
* **Interactive What-If Simulation:** Test individual subscriber profiles across 19 demographic, service, and billing attributes.
* **Instant Risk Assessment Dossier:**
  * Animated probability scoring with color-coded risk badges.
  * Automatic identification of key observed vulnerability triggers.
  * Direct prescription of tailored retention offers and priority response times.

### 4. 🎯 Smart Retention Studio & Customer Grid
* **Explainable Business Rule Engine:** Maps customer risk drivers to 7 deterministic retention playbooks:
  * *Annual Contract Migration Incentive:* Converting volatile month-to-month subscribers.
  * *Onboarding Health Check:* Proactive retention outreach for accounts under 12 months.
  * *Value-Add Digital Security Trial:* Offering complimentary tech support and online protection.
  * *Plan Right-Sizing Review:* Mitigating fiber optic billing friction.
  * *AutoPay Enrollment Credit:* Removing billing friction from electronic checks.
  * *Margin Protection:* Preventing unnecessary promotional discounts for healthy, low-risk accounts.
* **Interactive Customer Grid:** Real-time search by Customer ID, filtering by Risk Tier and Contract Type, sorting by churn probability.
* **1-Click Export:** Download the filtered retention action list as a CSV file for call-center and retention campaigns.
* **Customer Dossier Inspector:** Deep-dive into any individual customer from the active cohort.

### 5. 🧠 Model Insights & Strategic Drivers (Explainable AI)
* **Global Feature Importances:** Interactive chart showing the top 12 statistical drivers calculated by the Random Forest ensemble.
* **Executive Business Translation:** Direct translation of machine learning weights into practical commercial retention strategies.
* **Model Governance & Guardrails:** Full architectural transparency (100 trees, 50 dummy-encoded inputs, ensemble voting calibration, correlation vs. causation disclaimers).

---

## 🏗️ Architecture & Preprocessing Pipeline

```
Raw Customer Input (19 Fields)
        │
        ├──> Numeric Coercion & Imputation (TotalCharges, MonthlyCharges)
        ├──> Tenure Discretization: 12-Month Bins ('1 - 12' to '61 - 72')
        ├──> One-Hot Dummy Encoding
        └──> Reindexing to 50-Feature Training Schema (columns.pkl)
                     │
                     ▼
       Random Forest Classifier (model.sav)
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
Binary Prediction        Calibrated Probability
   (0 = Loyal, 1 = Churn)      P(Churn) in [0, 1]
                                  │
                                  ▼
                Smart Retention Recommendation Engine
                                  │
                                  ▼
                Actionable Customer Dossiers & KPIs
```

---

## 📁 Repository Structure

```
├── app.py              # Main Streamlit analytics & retention application
├── model.sav           # Serialized Random Forest classifier artifact
├── columns.pkl         # 50-feature expected training schema
├── sample_data.csv     # Telco customer cohort dataset (7,043 records)
├── requirements.txt    # Python package dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure Python 3.9+ is installed on your system.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```

The application will launch in your browser at `http://localhost:8501`.

---

## 💼 Business Impact & Portfolio Highlights
* **Revenue Protection:** Prioritizes retention desk outreach toward high-value, high-risk subscribers before cancellation occurs.
* **Margin Preservation:** Avoids margin-cannibalizing discounts on accounts that already exhibit low churn probability.
* **Explainable AI (XAI):** Solves the "black-box" dilemma by connecting statistical feature importance to actionable retention interventions.
