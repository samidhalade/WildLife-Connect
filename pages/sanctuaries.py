import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Wildlife Sanctuaries")

sanctuaries = pd.read_csv("data/sanctuaries.csv")

india_map = folium.Map(
    location=[22.5,79],
    zoom_start=5
)

for index,row in sanctuaries.iterrows():

    folium.CircleMarker(
        location=[row["Latitude"],row["Longitude"]],
        radius=6,
        color="darkgreen",
        fill=True,
        fill_color="darkgreen",
        tooltip=row["Name"],
        popup=row["Name"]
    ).add_to(india_map)

st_folium(
    india_map,
    width=900,
    height=600
)