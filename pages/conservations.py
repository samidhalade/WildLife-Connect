import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Conservation Map",
    layout="wide"
)

st.title("National Parks of India")
st.subheader("Interactive Map of National Parks")

st.divider()

conservations_data = pd.read_csv("data/conservations.csv")

india_map = folium.Map(
    location=[22.5, 79.0],
    zoom_start=5
)

for index, row in conservations_data.iterrows():

    popup_text = f"""
    <b>{row['Name']}</b><br>
    <b>State:</b> {row['State']}<br>
    <b>Flora:</b> {row['Flora']}<br>
    <b>Fauna:</b> {row['Fauna']}<br>
    <b>Area:</b> {row['Area (sq km)']} sq km<br>
    <b>Established:</b> {row['Established']}<br>
    <b>Description:</b> {row['Description']}
    """

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=7,
        color="lightgreen",
        fill=True,
        fill_color="lightgreen",
        fill_opacity=0.9,
        tooltip=row["Name"],
        popup=popup_text
    ).add_to(india_map)

st_folium(
    india_map,
    width=900,
    height=600
)