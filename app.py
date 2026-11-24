import os, sys
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.database import init_db
from src.data_manager import add_expense, generate_sample_data, import_csv
from src.analysis import load_expenses, category_summary, monthly_summary, payment_summary, daily_summary, budget_summary
from src.report import export_reports

init_db()
st.set_page_config(page_title="Personal Expense Tracker", page_icon="💸", layout="wide")
st.title("💸 Personal Expense Tracker")
st.caption("Python + Pandas + SQLite + Streamlit")

with st.sidebar:
    st.header("Add Expense")
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food","Transport","Shopping","Bills","Entertainment","Education","Health","Other","Income"])
    amount = st.number_input("Amount (₹)", min_value=0.0, step=50.0)
    method = st.selectbox("Payment Method", ["UPI","Cash","Card","Bank Transfer"])
    description = st.text_input("Description")
    if st.button("Add Expense", type="primary"):
        add_expense(str(date), category, amount, method, description)
        st.success("Expense added.")
        st.rerun()

    st.divider()
    if st.button("Generate Sample Data"):
        st.success(f"Added {generate_sample_data()} transactions.")
        st.rerun()

    uploaded = st.file_uploader("Import CSV", type=["csv"])
    if uploaded is not None and st.button("Import CSV"):
        st.success(f"Imported {import_csv(uploaded)} rows.")
        st.rerun()

    if st.button("Export Reports"):
        export_reports()
        st.success("Reports exported to outputs/")

df = load_expenses()
if df.empty:
    st.info("No expenses yet. Use Generate Sample Data in the sidebar.")
    st.stop()

expenses = df[df["category"] != "Income"].copy()
income = df[df["category"] == "Income"].copy()
total_spend = expenses["amount"].sum()
total_income = income["amount"].sum()
savings = total_income - total_spend
top = category_summary(expenses).iloc[0]["category"] if not expenses.empty else "None"

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Spending", f"₹{total_spend:,.0f}")
c2.metric("Income", f"₹{total_income:,.0f}")
c3.metric("Savings", f"₹{savings:,.0f}")
c4.metric("Top Category", top)

st.subheader("📊 Category-wise Spending")
cat = category_summary(expenses)
fig, ax = plt.subplots(figsize=(8,4))
ax.bar(cat["category"], cat["amount"])
ax.set_ylabel("Amount (₹)")
ax.tick_params(axis="x", rotation=35)
fig.tight_layout()
st.pyplot(fig)

st.subheader("📈 Monthly Spending Trend")
monthly = monthly_summary(expenses)
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(monthly["month"], monthly["amount"], marker="o")
ax.set_ylabel("Amount (₹)")
ax.tick_params(axis="x", rotation=35)
fig.tight_layout()
st.pyplot(fig)

col1,col2 = st.columns(2)
with col1:
    st.subheader("💳 Payment Methods")
    pay = payment_summary(expenses)
    fig, ax = plt.subplots(figsize=(6,5))
    ax.pie(pay["amount"], labels=pay["payment_method"], autopct="%1.1f%%")
    st.pyplot(fig)
with col2:
    st.subheader("📅 Daily Spending")
    daily = daily_summary(expenses)
    fig, ax = plt.subplots(figsize=(6,5))
    ax.plot(daily["date"], daily["amount"])
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    st.pyplot(fig)

st.subheader("🎯 Budget Check")
st.dataframe(budget_summary(expenses), use_container_width=True)
st.subheader("🧾 Transactions")
st.dataframe(df.sort_values("date", ascending=False), use_container_width=True)

st.download_button("Download Transactions CSV", df.to_csv(index=False).encode("utf-8"), "expenses.csv", "text/csv")
