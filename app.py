import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from pages import about
from pages import sanctuaries
from pages import conservations
from pages import combined_map

st.set_page_config(
    page_title="WildLife Connect",
    layout="wide"
)

sanctuaries_data = pd.read_csv("data/sanctuaries.csv")
conservations_data = pd.read_csv("data/conservations.csv")

all_places = pd.concat(
    [sanctuaries_data, conservations_data],
    ignore_index=True
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

st.title("WildLife Connect")
st.subheader("Interactive Dashboard for India's Wildlife Sanctuaries and Conservations")
st.divider()

top_left, top_right = st.columns([3,2])

with top_right:

    search = st.text_input(
        "Search",
        placeholder="Search Sanctuary or Conservation"
    )

    if search:

        results = all_places[
            all_places["Name"].str.contains(search, case=False, na=False)
       ]

        if not results.empty:
           st.success("Search Results")

           st.dataframe(results)

        else:
             st.error("No matching location found.")

    filter1, filter2, filter3 = st.columns(3)

    with filter1:
        state = st.selectbox(
            "State",
            [
                "Maharashtra",
                "Madhya Pradesh",
                "Gujarat",
                "Rajasthan",
                "Kerala",
                "Assam"
            ]
        )

    with filter2:
        flora = st.selectbox(
            "Flora",
            [
                "Bamboo",
                "Teak",
                "Sal",
                "Sandalwood",
                "Rosewood"
            ]
        )

    with filter3:
        fauna = st.selectbox(
            "Fauna",
            [
                "Tiger",
                "Lion",
                "Elephant",
                "Leopard",
                "Rhinoceros"
            ]
        )

st.divider()

left_panel, centre_panel = st.columns([2,4])

with left_panel:

    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"

    if st.button("Sanctuary Map", use_container_width=True):
        st.session_state.page = "Sanctuaries"

    if st.button("Conservation Map", use_container_width=True):
        st.session_state.page = "Conservations"

    if st.button("Combined Map", use_container_width=True):
        st.session_state.page = "Combined"

    if st.button("About Us", use_container_width=True):
        st.session_state.page = "About"

with centre_panel:

    if st.session_state.page == "Home":

        st.subheader("India Map")

        india_map = folium.Map(
            location=[22.5, 79.0],
            zoom_start=5
        )

        for index, row in all_places.iterrows():

            if "National Park" in row["Name"]:
                color = "lightgreen"
            else:
                color = "darkgreen"

            folium.CircleMarker(
                location=[row["Latitude"], row["Longitude"]],
                radius=6,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=1,
                tooltip=row["Name"],
                popup=row["Name"]
            ).add_to(india_map)

        st_folium(
            india_map,
            width=800,
            height=600
        )

    elif st.session_state.page == "About":
        about.show()

    elif st.session_state.page == "Sanctuaries":
        sanctuaries.show()

    elif st.session_state.page == "Conservations":
        conservations.show()

    elif st.session_state.page == "Combined":
        combined_map.show()