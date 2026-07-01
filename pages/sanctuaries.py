import streamlit as st
import pandas as pd

def show():

    st.title("Wildlife Sanctuaries")

    data = pd.read_csv("data/sanctuaries.csv")

    st.dataframe(data)