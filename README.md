# 📦 CartFlow — Order Cancellation Analysis in E‑commerce

<p align="center">
  <img src="images/cover_1.png" alt="CartFlow dashboard - Overview" width="49%">
  <img src="images/cover_2.png" alt="CartFlow cancellation insights" width="49%">
</p>

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen)](https://REPLACE_WITH_YOUR_STREAMLIT_URL)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This project explores **order cancellation patterns** in an e‑commerce operation. Using **Python, Pandas, and Seaborn**, it identifies recurring drivers of cancellations and proposes **data‑driven actions** to reduce loss and improve conversion.

---

## 🎯 Project Goals

* Identify the **most frequent cancellation reasons**
* Profile **customer/transaction segments** with higher cancel rates
* Quantify **revenue loss** due to cancellations
* Deliver **actionable recommendations** for mitigation

---

## 🧰 Tech Stack

* **Python** 3.10+
* **Pandas**, **NumPy**, **Seaborn**, **Matplotlib**, **Scikit‑learn**
* **Jupyter Notebook**
* **Streamlit** (1‑click demo)

> Note: previously misspelled as "Seabor" — corrected to **Seaborn**.

---

## 📦 Data

* `data/orders.csv` (or `data/sample_orders.csv` for the demo)
* Minimum columns: `order_id`, `order_value`, `cancelled` (0/1) + context features (e.g., `payment_method`, `shipping_eta`, `inventory_status`, `region`)
* If simulated, the README documents **how** and **why** the data was generated (see `notebooks/00_data_generation.ipynb`).

---

## 🔬 Methodology (Overview)

1. **EDA**: missing values, outliers, leakage checks, class balance
2. **Feature engineering**: recency/frequency/value, device, payment, shipping ETA buckets
3. **Modeling**: baseline logistic regression for cancellation probability
4. **Evaluation**: ROC‑AUC, PR‑AUC, calibration; cost‑sensitive thresholding
5. **Prescriptions**: playbook por driver (pagamento, logística, inventário, UX)

---

## 📈 Results (Sample)

* Top drivers: `shipping_eta > 7d`, `payment_declined`, `inventory_backorder`
* Priority segments: new customers (first order), low AOV + long ETA, mobile checkout
* Baseline cancel rate: **12.0%** → scenario target **10.0%** (‑2pp)

> Replace the bullets above with your actual findings from the notebook.

---

## 💰 Business Impact

**Key takeaway:** even small reductions in cancellation rate can have **outsized revenue impact**.

* Baseline monthly orders: **N\_orders**
* Avg order value (AOV): **\$AOV**
* Baseline cancellation rate: **r0**
* Target cancellation rate: **r1** (e.g., r1 = r0 − 2pp)

**Monthly revenue lift (approx.):**

```math
ΔRev ≈ N_orders × AOV × (r0 − r1)
```

**Example (replace with your data):**
If `N_orders = 40,000`, `AOV = $62`, and cancellations go **12% → 10%**:

```
ΔRev ≈ 40,000 × 62 × (0.12 − 0.10) = **$49,600 / month**
```

**Levers to achieve r1:** payment retry flows, clearer shipping ETA, inventory hold windows, proactive email/SMS on risk signals, UX copy for address/payment.

---

## 🚀 Quickstart (Local)

```bash
# 1) create env
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# 2) install
pip install -r requirements.txt

# 3) run notebook
jupyter notebook notebooks/01_eda_and_model.ipynb

# 4) run demo app
streamlit run app.py
```

---

## 🌐 Live Demo (Streamlit)

* Deploy on **Streamlit Community Cloud** → set main file to `app.py`
* Replace the badge link at the top with your public URL

```bash
# expected files for demo
app.py
data/sample_orders.csv
```

---

## 📁 Repository Structure

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

Add your main visuals at `images/cover_1.png` and `images/cover_2.png`, then verify they render at the top of this README.

---

## 📝 License

[MIT](LICENSE)

- Seabor
