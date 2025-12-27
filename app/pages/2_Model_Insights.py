import streamlit as st
import pandas as pd
from pathlib import Path

OUT = Path("outputs/tables")

st.title("📈 Model Insights")

perf = pd.read_csv(OUT / "prediction_performance.csv")
st.subheader("Prediction model performance")
st.dataframe(perf)

sens_path = OUT / "price_sensitivity_summary.csv"
if sens_path.exists():
    sens = pd.read_csv(sens_path)
    st.subheader("Price sensitivity by category")
    st.dataframe(sens)
else:
    st.info("Price sensitivity summary not found yet.")
