# 📦 CartFlow — Order Cancellation Analysis in E‑commerce

<p align="center">
  <img src="images/cover_1.png" alt="CartFlow dashboard - Overview" width="49%">
  <img src="images/cover_2.png" alt="CartFlow cancellation insights" width="49%">
</p>

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen)](https://YOUR_STREAMLIT_URL)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This project analyzes order cancellation patterns in e‑commerce using **Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit‑learn**. It identifies key drivers of cancellations, segments with high cancellation rates, quantifies revenue impact, and provides data‑driven recommendations.

---

## 🎯 Goals

* Identify top cancellation reasons
* Segment customers and transactions by cancellation rate
* Calculate revenue loss from cancellations
* Recommend actions to reduce cancellations

---

## 🧰 Tech Stack

* **Python** 3.10+
* **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**, **Scikit‑learn**
* **Jupyter Notebook**
* **Streamlit** (demo app)

---

## 📦 Data

* `data/orders.csv` or `data/sample_orders.csv`
* Minimum required columns: `order_id`, `order_value`, `cancelled` (0/1), plus contextual features (e.g., `payment_method`, `shipping_eta`, `inventory_status`, `region`)
* Synthetic data is documented in `notebooks/00_data_generation.ipynb`

---

## 🔬 Methodology

1. **EDA** — data quality checks, outlier detection, target distribution
2. **Feature Engineering** — create relevant features from transactional data
3. **Modeling** — baseline logistic regression to predict cancellations
4. **Evaluation** — ROC‑AUC, PR‑AUC, calibration
5. **Recommendations** — targeted actions based on top cancellation drivers

---

## 📈 Key Results

* Main drivers: `shipping_eta > 7d`, `payment_declined`, `inventory_backorder`
* Priority segments: first‑time buyers, low AOV + long ETA, mobile checkout
* Example improvement: reduce cancellations from 12% to 10% (‑2pp)

---

## 💰 Business Impact Example

Reducing cancellations by 2 percentage points can yield significant revenue lift:

If `40,000` monthly orders, `AOV = $62`, cancellations reduced from 12% to 10%:

```
ΔRevenue = 40,000 × 62 × (0.12 − 0.10) = $49,600/month
```

---

## 🚀 Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo

Deploy on **Streamlit Community Cloud**, set main file to `app.py`, and update the badge link above.

---

## 📁 Structure

```
cartflow-cancellation-analysis/
├── app.py
├── data/
│   └── sample_orders.csv
├── images/
│   ├── cover_1.png
│   └── cover_2.png
├── notebooks/
│   ├── 00_data_generation.ipynb
│   └── 01_eda_and_model.ipynb
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📸 Screenshots

Ensure `images/cover_1.png` and `images/cover_2.png` are updated and visible at the top of this README.

---

## 📝 License

[MIT](LICENSE)

