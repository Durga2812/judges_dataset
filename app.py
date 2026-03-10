import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

# Upload dataset
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.write("Dataset Preview")
    st.dataframe(df)

    st.write("Basic Statistics")
    st.write(df.describe())

    st.write("Bar Chart")
    st.bar_chart(df.select_dtypes(include="number"))