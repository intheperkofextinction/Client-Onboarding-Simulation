import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------
# Page Setup
# ---------------------
st.set_page_config(page_title="Client Onboarding Dashboard", layout="wide")
st.title(" Client Onboarding Pipeline Simulation")
st.markdown("This dashboard simulates an end-to-end client onboarding workflow, including document submission, AML checks, KYC, and review status.")

# ---------------------
# Load Data
# ---------------------
@st.cache_data
def load_data():
    return pd.read_csv("client_data.csv")

df = load_data()

# ---------------------
# Summary Stats
# ---------------------
st.markdown("###  Summary Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric(" Total Clients", len(df))
col2.metric(" Approved", df["Review_Status"].value_counts().get("Approved", 0))
col3.metric(" Rejected", df["Review_Status"].str.contains("Rejected").sum())
col4.metric(" AML Escalated", df["Review_Status"].str.contains("Escalated").sum())

# ---------------------
# Sidebar Filters
# ---------------------
st.sidebar.header(" Filter Clients")
status_options = df["Review_Status"].unique().tolist()
selected_status = st.sidebar.multiselect("Select Review Status", options=status_options, default=status_options)

country_options = sorted(df["Nationality"].unique())
selected_countries = st.sidebar.multiselect("Select Country", options=country_options, default=country_options)

filtered_df = df[
    (df["Review_Status"].isin(selected_status)) &
    (df["Nationality"].isin(selected_countries))
]

# ---------------------
# Review Status Chart
# ---------------------
st.markdown("###  Review Status Distribution")
status_counts = filtered_df["Review_Status"].value_counts().reset_index()
status_counts.columns = ["Review_Status", "Count"]

fig = px.bar(
    status_counts,
    x="Review_Status",
    y="Count",
    color="Review_Status",
    labels={"Review_Status": "Status", "Count": "Client Count"},
    title="Client Distribution by Review Status"
)
st.plotly_chart(fig, use_container_width=True)

# ---------------------
# AML Escalated Table
# ---------------------
st.markdown("###  AML Escalated Clients")
aml_df = filtered_df[filtered_df["Review_Status"].str.contains("Escalated")]
st.dataframe(aml_df, use_container_width=True)

# ---------------------
# Full Table (Optional)
# ---------------------
with st.expander(" View Full Filtered Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

# ---------------------
# Footer
# ---------------------
st.markdown("---")
st.markdown("Built with Python & Streamlit | Simulated Client Onboarding Pipeline | Created by Amal")

