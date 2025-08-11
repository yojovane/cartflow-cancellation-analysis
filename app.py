# app.py — CartFlow (Streamlit demo)
from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="CartFlow — Cancellation Analysis",
    page_icon="🛒",
    layout="wide"
)

# ---------- Resolve project paths (always at repo root) ----------
project_base_dir = Path.cwd()
if project_base_dir.name == "notebooks":
    project_base_dir = project_base_dir.parent

data_dir   = project_base_dir / "data"
images_dir = project_base_dir / "images"
data_dir.mkdir(exist_ok=True)
images_dir.mkdir(exist_ok=True)

# ---------- Load data ----------
@st.cache_data(show_spinner=False)
def load_orders():
    # Priority: orders.csv (official) -> sample_orders.csv (fallback)
    candidates = [data_dir / "orders.csv", data_dir / "sample_orders.csv"]
    for p in candidates:
        if p.exists():
            df = pd.read_csv(p, parse_dates=["order_date"], dayfirst=False, infer_datetime_format=True)
            return df, p
    return None, None

df, source_path = load_orders()

st.title("🛒 CartFlow — Order Cancellation Analysis")

if df is None:
    st.warning(
        "No data found. Please run *notebooks/00_data_generation.ipynb* to create "
        "data/orders.csv, or place a data/sample_orders.csv file."
    )
    st.stop()

st.caption(f"Loaded: {source_path} — {df.shape[0]:,} rows × {df.shape[1]} columns")

# ---------- Minimal cleaning & feature engineering for UI ----------
df = df.copy()
if "device_type" in df.columns:
    df["device_type"] = df["device_type"].astype(str).str.title()

if "order_value" in df.columns and df["order_value"].isna().any():
    df["order_value"] = df["order_value"].fillna(df["order_value"].median())

if "order_date" in df.columns and not np.issubdtype(df["order_date"].dtype, np.datetime64):
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

if "customer_tenure_days" in df.columns:
    df["first_time_customer"] = (df["customer_tenure_days"] < 30).astype(int)
else:
    df["first_time_customer"] = 0

if "order_value" in df.columns:
    bins = [0, 50, 150, 300, 800]
    labels = ["0-50", "50-150", "150-300", "300+"]
    df["aov_bucket"] = pd.cut(df["order_value"], bins=bins, labels=labels, include_lowest=True)

if "order_date" in df.columns:
    df["is_weekend"] = df["order_date"].dt.weekday.isin([5, 6]).astype(int)

# ---------- KPIs ----------
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Orders", f"{len(df):,}")
with col2:
    canc_rate = df["cancelled"].mean()*100 if "cancelled" in df.columns else 0
    st.metric("Cancellation Rate", f"{canc_rate:.1f}%")
with col3:
    aov = df["order_value"].mean() if "order_value" in df.columns else 0
    st.metric("Average Order Value (AOV)", f"${aov:,.2f}")
with col4:
    ftb = df["first_time_customer"].mean()*100 if "first_time_customer" in df.columns else 0
    st.metric("First‑time Buyers", f"{ftb:.1f}%")

st.divider()

# ---------- Charts (pick ones that mirror your README covers) ----------
tab1, tab2, tab3 = st.tabs(["Top Reasons", "By Order Value", "By Device"])

with tab1:
    st.subheader("Top Cancellation Reasons (%)")
    if "cancellation_reason" in df.columns and "cancelled" in df.columns:
        reasons = (
            df[df["cancelled"] == 1]["cancellation_reason"]
            .value_counts(normalize=True)
            .mul(100)
            .sort_values(ascending=False)
            .round(1)
        )
        st.bar_chart(reasons)
    else:
        st.info("Columns cancellation_reason and/or cancelled not found.")

with tab2:
    st.subheader("Cancellation Rate by Order Value (buckets)")
    if "aov_bucket" in df.columns and "cancelled" in df.columns:
        order = ["0-50", "50-150", "150-300", "300+"]
        rate = df.groupby("aov_bucket")["cancelled"].mean().mul(100).reindex(order)
        st.bar_chart(rate)
    else:
        st.info("Columns aov_bucket and/or cancelled not found.")

with tab3:
    st.subheader("Cancellation Rate by Device Type")
    if "device_type" in df.columns and "cancelled" in df.columns:
        rate_dev = df.groupby("device_type")["cancelled"].mean().mul(100).sort_values(ascending=False)
        st.bar_chart(rate_dev)
    else:
        st.info("Columns device_type and/or cancelled not found.")

st.divider()

# ---------- Business Impact Calculator ----------
st.subheader("💵 Business Impact Calculator")
colA, colB, colC = st.columns(3)
with colA:
    monthly_orders = st.number_input("Monthly Orders", min_value=100, value=40000, step=1000)
with colB:
    current_rate = st.slider("Current Cancellation Rate (%)", 0.0, 50.0, float(canc_rate if canc_rate>0 else 12.0), 0.5)
with colC:
    target_rate = st.slider("Target Cancellation Rate (%)", 0.0, 50.0, 10.0, 0.5)

aov_input = st.number_input("Average Order Value (AOV, $)", min_value=1.0, value=float(aov if aov>0 else 62.0), step=1.0)

delta_rev = monthly_orders * aov_input * ((current_rate - target_rate) / 100.0)
st.success(f"Estimated Monthly Revenue Impact: *${delta_rev:,.0f}*")

st.caption("Formula: orders × AOV × (current_rate − target_rate)")

# ---------- Footer ----------
st.write("---")
st.caption("CartFlow demo • Streamlit • Data source: orders.csv")