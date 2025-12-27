import streamlit as st
import pandas as pd
from pathlib import Path

DATA = Path("data/processed/model_data.csv")

st.title("Data Overview")

df = pd.read_csv(DATA)
st.write("Rows:", len(df))
st.dataframe(df.head(20))

weekly = df.groupby("week")[["revenue","profit"]].sum().reset_index()
st.line_chart(weekly.set_index("week")[["revenue","profit"]])
