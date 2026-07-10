import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="National Parks",
    layout="wide"
)

national_parks = pd.read_csv("data/national_parks.csv")

st.title("National Parks of India")

st.write(
    "Explore India's famous National Parks through an interactive map."
)

st.divider()

search = st.text_input(
    "Search National Park",
    placeholder="Search by park name..."
)

latitude = 22.5
longitude = 79
zoom = 5

searched_name = None

if search:

    result = national_parks[
        national_parks["Name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    if not result.empty:

        searched_name = result.iloc[0]["Name"]

        latitude = result.iloc[0]["Latitude"]
        longitude = result.iloc[0]["Longitude"]
        zoom = 9

park_map = folium.Map(
    location=[latitude, longitude],
    zoom_start=zoom
)

for _, row in national_parks.iterrows():

    colour = "lightgreen"
    radius = 7

    if searched_name == row["Name"]:

        colour = "red"
        radius = 10

    popup = f"""
    <b>{row['Name']}</b><br><br>

    <b>State:</b> {row['State']}<br>

    <b>Flora:</b> {row['Flora']}<br>

    <b>Fauna:</b> {row['Fauna']}<br>

    <b>Area:</b> {row['Area (sq km)']} sq km<br>

    <b>Established:</b> {row['Established']}<br><br>

    {row['Description']}
    """

    folium.CircleMarker(

        location=[
            row["Latitude"],
            row["Longitude"]
        ],

        radius=radius,

        color=colour,

        fill=True,

        fill_color=colour,

        fill_opacity=1,

        tooltip=row["Name"],

        popup=popup

    ).add_to(park_map)

st_folium(
    park_map,
    width=1100,
    height=650
)

st.divider()

st.header("National Parks")

display_data = national_parks

if search and searched_name is not None:

    display_data = national_parks[
        national_parks["Name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

for index, row in display_data.iterrows():

    with st.container():

        col1, col2 = st.columns([1, 3])

        with col1:

            image_path = f"images/national_parks/{row['Image']}"

            try:
                st.image(
                    image_path,
                    use_container_width=True
                )

            except Exception:
                st.warning("Image not available.")

        with col2:

            st.subheader(row["Name"])

            st.write(f"**State:** {row['State']}")

            st.write(f"**Flora:** {row['Flora']}")

            st.write(f"**Fauna:** {row['Fauna']}")

            st.write(f"**Area:** {row['Area (sq km)']} sq km")

            st.write(f"**Established:** {row['Established']}")

            st.write(row["Description"])

            if st.button(
                "View Details",
                key=f"park_{index}"
            ):

                st.session_state.selected_place = row["Name"]

                st.switch_page("pages/details.py")

        st.divider()