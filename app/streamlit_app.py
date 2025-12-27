import streamlit as st

st.set_page_config(page_title="ElasticLens", layout="wide")

st.title("ElasticLens — Pricing & Discount Impact Simulator")
st.write("Synthetic retail example: understand demand drivers and run what-if scenarios.")

st.page_link("pages/1_Data_Overview.py", label="Go to Data Overview", icon="📊")
st.page_link("pages/2_Model_Insights.py", label="Go to Model Insights", icon="📈")
st.page_link("pages/3_Scenario_Simulator.py", label="Go to Scenario Simulator", icon="🧪")
