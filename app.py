import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from pages import about

st.set_page_config(
    page_title="WildLife Connect",
    layout="wide"
)

# ----------------------------
# Read CSV Files
# ----------------------------

sanctuaries_data = pd.read_csv("data/sanctuaries.csv")
conservations_data = pd.read_csv("data/conservations.csv")

all_places = pd.concat(
    [sanctuaries_data, conservations_data],
    ignore_index=True
)

filtered_places = all_places.copy()

# ----------------------------
# Session State
# ----------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ----------------------------
# Title
# ----------------------------

st.title("WildLife Connect")

st.subheader(
    "Interactive Dashboard for India's Wildlife Sanctuaries and National Parks"
)

st.divider()

# ----------------------------
# Top Section
# ----------------------------

top_left, top_right = st.columns([3,2])

with top_left:

    total_places = len(all_places)

    total_sanctuaries = len(sanctuaries_data)

    total_parks = len(conservations_data)

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric("Protected Areas", total_places)

    with c2:
        st.metric("Sanctuaries", total_sanctuaries)

    with c3:
        st.metric("Conservations", total_parks)

with top_right:

    search = st.text_input(
        "Search",
        placeholder="Search Sanctuary or Conservations"
    )

    results = filtered_places

    if search:

        results = filtered_places[
            filtered_places["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

        if not results.empty:

            place = results.iloc[0]

            st.success("Location Found")

            st.write("**Name :**", place["Name"])
            st.write("**State :**", place["State"])
            st.write("**Flora :**", place["Flora"])
            st.write("**Fauna :**", place["Fauna"])
            st.write("**Area :**", place["Area (sq km)"], "sq km")

        else:

            st.error("No location found")

# ----------------------------
# Filters
# ----------------------------

filter1,filter2,filter3 = st.columns(3)

with filter1:

    state = st.selectbox(

        "State",

        sorted(
            ["All"] +
            list(all_places["State"].unique())
        )

    )

with filter2:

    flora = st.selectbox(

        "Flora",

        sorted(
            ["All"] +
            list(all_places["Flora"].unique())
        )

    )

with filter3:

    fauna = st.selectbox(

        "Fauna",

        sorted(
            ["All"] +
            list(all_places["Fauna"].unique())
        )

    )

if state != "All":

    filtered_places = filtered_places[
        filtered_places["State"] == state
    ]

if flora != "All":

    filtered_places = filtered_places[
        filtered_places["Flora"] == flora
    ]

if fauna != "All":

    filtered_places = filtered_places[
        filtered_places["Fauna"] == fauna
    ]

st.divider()

# ----------------------------
# Main Layout
# ----------------------------

left_panel, centre_panel = st.columns([2,5])

with left_panel:

    st.subheader("Navigation")

    if st.button(
        "Home",
        use_container_width=True
    ):
        st.session_state.page = "Home"

    if st.button(
        "Sanctuary Map",
        use_container_width=True
    ):
        st.session_state.page = "Sanctuaries"

    if st.button(
        "Conservations",
        use_container_width=True
    ):
        st.session_state.page = "Conservations"

    if st.button(
        "About Us",
        use_container_width=True
    ):
        st.session_state.page = "About"

with centre_panel:

    if st.session_state.page == "Home":

        st.subheader("India Map")

        map_lat = 22.5
        map_lon = 79.0
        zoom = 5

        if search:

            if not results.empty:

                map_lat = results.iloc[0]["Latitude"]
                map_lon = results.iloc[0]["Longitude"]
                zoom = 8

        india_map = folium.Map(

            location=[map_lat,map_lon],

            zoom_start=zoom

        )

        for index,row in filtered_places.iterrows():

            if "National Park" in row["Name"]:

                marker_color = "lightgreen"

            else:

                marker_color = "darkgreen"

            if search:

                if not results.empty:

                    if row["Name"] == results.iloc[0]["Name"]:

                        marker_color = "red"

                        marker_radius = 10

                    else:

                        marker_radius = 6

                else:

                    marker_radius = 6

            else:

                marker_radius = 6

            popup_text = f"""
            <b>{row['Name']}</b><br>
            State : {row['State']}<br>
            Flora : {row['Flora']}<br>
            Fauna : {row['Fauna']}<br>
            Area : {row['Area (sq km)']} sq km<br>
            Established : {row['Established']}
            """

            folium.CircleMarker(

                location=[
                    row["Latitude"],
                    row["Longitude"]
                ],

                radius=marker_radius,

                color=marker_color,

                fill=True,

                fill_color=marker_color,

                fill_opacity=1,

                tooltip=row["Name"],

                popup=popup_text

            ).add_to(india_map)

        st_folium(

            india_map,

            width=900,

            height=600

        )
    elif st.session_state.page == "Sanctuaries":

        st.subheader("Wildlife Sanctuaries")

        sanctuary_map = folium.Map(
            location=[22.5, 79.0],
            zoom_start=5
        )

        for index, row in sanctuaries_data.iterrows():

            popup_text = f"""
            <b>{row['Name']}</b><br>
            State : {row['State']}<br>
            Flora : {row['Flora']}<br>
            Fauna : {row['Fauna']}<br>
            Area : {row['Area (sq km)']} sq km<br>
            Established : {row['Established']}<br>
            Description : {row['Description']}
            """

            folium.CircleMarker(

                location=[
                    row["Latitude"],
                    row["Longitude"]
                ],

                radius=7,

                color="darkgreen",

                fill=True,

                fill_color="darkgreen",

                fill_opacity=1,

                tooltip=row["Name"],

                popup=popup_text

            ).add_to(sanctuary_map)

        st_folium(
            sanctuary_map,
            width=900,
            height=600
        )



    elif st.session_state.page == "Conservations":

        st.subheader("Conservations")

        park_map = folium.Map(
            location=[22.5, 79.0],
            zoom_start=5
        )

        for index, row in conservations_data.iterrows():

            popup_text = f"""
            <b>{row['Name']}</b><br>
            State : {row['State']}<br>
            Flora : {row['Flora']}<br>
            Fauna : {row['Fauna']}<br>
            Area : {row['Area (sq km)']} sq km<br>
            Established : {row['Established']}<br>
            Description : {row['Description']}
            """

            folium.CircleMarker(

                location=[
                    row["Latitude"],
                    row["Longitude"]
                ],

                radius=7,

                color="lightgreen",

                fill=True,

                fill_color="lightgreen",

                fill_opacity=1,

                tooltip=row["Name"],

                popup=popup_text

            ).add_to(park_map)

        st_folium(
            park_map,
            width=900,
            height=600
        )



    elif st.session_state.page == "About":

        about.show()