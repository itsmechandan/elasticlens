import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from pathlib import Path

DATA = Path("data/processed/model_data.csv")
MODEL = Path("outputs/models/demand_prediction_model.pkl")

st.title("Scenario Simulator")

df = pd.read_csv(DATA)
model = load(MODEL)

latest_week = int(df["week"].max())
base = df[df["week"] == latest_week].copy()

st.write(f"Baseline week used: **Week {latest_week}**")

price_change = st.slider("Price change (%)", -10, 10, 5)
discount_change = st.slider("Discount change (absolute % points)", -10, 10, -3)
marketing_change = st.slider("Marketing change (%)", -20, 20, 10)

scenario = base.copy()
scenario["final_price"] = scenario["final_price"] * (1 + price_change/100)
scenario["discount_percent"] = np.maximum(scenario["discount_percent"] + discount_change, 0)
scenario["marketing_spend"] = scenario["marketing_spend"] * (1 + marketing_change/100)

features = ["final_price", "discount_percent", "marketing_spend", "week"]

base["pred_units"] = model.predict(base[features])
scenario["pred_units"] = model.predict(scenario[features])

base_rev = (base["pred_units"] * base["final_price"]).sum()
base_profit = (base["pred_units"] * (base["final_price"] - base["cost_price"])).sum()

sc_rev = (scenario["pred_units"] * scenario["final_price"]).sum()
sc_profit = (scenario["pred_units"] * (scenario["final_price"] - scenario["cost_price"])).sum()

st.subheader("Impact vs baseline")
st.metric("Revenue change (%)", f"{(sc_rev/base_rev - 1)*100:.2f}")
st.metric("Profit change (%)", f"{(sc_profit/base_profit - 1)*100:.2f}")

st.caption("This is a what-if simulation using the trained prediction model. It is meant for decision support, not guaranteed outcomes.")
