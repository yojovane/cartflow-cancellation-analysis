📦 CartFlow — E-commerce Order Cancellation Analysis
<p align="center">
  <img src="images/cover_1.png" alt="CartFlow Dashboard - Overview" width="49%">
  <img src="images/cover_2.png" alt="CartFlow Dashboard - Cancellation Insights" width="49%">
</p>

This data analysis project explores patterns and causes of order cancellations in e-commerce operations. Using Python, Pandas, and Seaborn, it identifies key cancellation drivers and proposes data-driven actions to reduce losses and optimize conversion.

🎯 Project Goals
Identify the most frequent cancellation reasons.

Analyze the profile of customer and transaction segments with high cancellation rates.

Quantify revenue loss due to cancellations.

Provide strategic recommendations to mitigate the issue.

🧰 Tech Stack
Python (v3.10+)

Data Science Libraries: Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn

Tools: Jupyter Notebook (for analysis and modeling), Streamlit (for the demo application)

📦 Data Structure
Source: data/orders.csv (or data/sample_orders.csv for the demo).

Minimum Columns: order_id, order_value, cancelled (0/1), plus contextual features like payment_method, shipping_eta, inventory_status, and region.

Simulated Data: The notebooks/00_data_generation.ipynb notebook details how and why the data was generated.

🔬 Methodology
Exploratory Data Analysis (EDA): Inspection of missing values, outliers, and class balance verification.

Feature Engineering: Creation of variables such as recency/frequency/value, device type, payment method, and shipping time buckets.

Modeling: Development of a logistic regression model to predict cancellation probability.

Evaluation: Use of metrics like ROC-AUC, PR-AUC, and calibration to assess model performance.

Recommendations: Creation of an action playbook per segment, focusing on payments, logistics, inventory, and user experience (UX).

📈 Results (Sample)
Key Drivers: shipping_eta > 7d, payment_declined, inventory_backorder.

Priority Segments: New customers, low AOV with long delivery times, and users checking out on mobile.

Baseline Cancellation Rate: 12.0% → Target: 10.0% (2pp reduction).

Note: Replace the above examples with your actual analysis findings.

💰 Business Impact
Key takeaway: Even small reductions in the cancellation rate can have an outsized impact on revenue.

Approximate Revenue Lift Calculation:

ΔReceita ≈ N_orders × AOV × (r0 − r1)

Where:

N_orders: Monthly orders

AOV: Average order value

r0: Initial cancellation rate

r1: Target cancellation rate

Example (replace with your data):
If N_orders = 40,000, AOV = $62, and the cancellation rate drops from 12% to 10%:

ΔReceita ≈ 40,000 × 62 × (0.12 − 0.10) = **$49,600 / month**

Levers to achieve r1: Payment retry flows, clearer shipping estimates, inventory hold windows, proactive email/SMS on risk signals, and UX optimization.

🚀 Quickstart (Local)
# 1) Create and activate the virtual environment
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the analysis notebook
jupyter notebook notebooks/01_eda_and_model.ipynb

# 4) Run the demo application
streamlit run app.py

📁 Repository Structure
cartflow-cancellation-analysis/
├── app.py
├── data/
│   └── sample_orders.csv
├── images/
│   ├── cover_1.png
│   └── cover_2.png
├── notebooks/
│   ├── 00_data_generation.ipynb
│   └── 01_eda_and_model.ipynb
├── requirements.txt
├── README.md
└── LICENSE
