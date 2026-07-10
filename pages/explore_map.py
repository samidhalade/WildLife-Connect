import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Explore Map",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

sanctuaries = pd.read_csv("data/sanctuaries.csv")
national_parks = pd.read_csv("data/national_parks.csv")

sanctuaries["Type"] = "Sanctuary"
national_parks["Type"] = "National Park"

all_places = pd.concat(
    [sanctuaries, national_parks],
    ignore_index=True
)

# -----------------------------
# PAGE TITLE
# -----------------------------

st.title("Explore Protected Areas")

st.write(
    "Search and explore Wildlife Sanctuaries and National Parks across India."
)

st.divider()

# -----------------------------
# SEARCH BAR
# -----------------------------

search = st.text_input(
    "Search",
    placeholder="Search Sanctuary or National Park"
)

# -----------------------------
# FILTERS
# -----------------------------

c1, c2, c3 = st.columns(3)

with c1:

    state = st.selectbox(
        "State",
        ["All"] + sorted(all_places["State"].unique())
    )

with c2:

    category = st.selectbox(
        "Category",
        ["All", "Sanctuary", "National Park"]
    )

with c3:

    fauna = st.selectbox(
        "Fauna",
        ["All"] + sorted(all_places["Fauna"].unique())
    )

filtered = all_places.copy()

if state != "All":
    filtered = filtered[
        filtered["State"] == state
    ]

if category != "All":
    filtered = filtered[
        filtered["Type"] == category
    ]

if fauna != "All":

    filtered = filtered[
        filtered["Fauna"].str.contains(
            fauna,
            case=False,
            na=False
        )
    ]

# -----------------------------
# SEARCH
# -----------------------------

results = filtered.copy()

if search:

    results = filtered[
        filtered["Name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# -----------------------------
# MAP POSITION
# -----------------------------

latitude = 22.5
longitude = 79
zoom = 5

if search and not results.empty:

    latitude = results.iloc[0]["Latitude"]
    longitude = results.iloc[0]["Longitude"]
    zoom = 8

india_map = folium.Map(
    location=[latitude, longitude],
    zoom_start=zoom
)

# -----------------------------
# MARKERS
# -----------------------------

for _, row in filtered.iterrows():

    if row["Type"] == "Sanctuary":
        colour = "darkgreen"
    else:
        colour = "lightgreen"

    radius = 6

    if search:

        if not results.empty:

            if row["Name"] == results.iloc[0]["Name"]:

                colour = "red"
                radius = 10

    popup = f"""
    <b>{row['Name']}</b><br><br>

    <b>Type:</b> {row['Type']}<br>

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

    ).add_to(india_map)

# -----------------------------
# DISPLAY MAP
# -----------------------------

st_folium(
    india_map,
    width=1200,
    height=650
)

st.divider()

st.divider()

st.header("Protected Areas")

for index, row in filtered.iterrows():

    col1, col2 = st.columns([5,1])

    with col1:

        st.subheader(row["Name"])

        st.write(f"State: {row['State']}")

        st.write(f"**Category:** {row['Type']}")

        st.write(row["Description"])

    with col2:

        if st.button(
            "View Details",
            key=f"details_{index}"
        ):

            st.session_state.selected_place = row["Name"]

            st.switch_page("pages/details.py")

    st.divider()

st.divider()

# -----------------------------
# RESULTS TABLE
# -----------------------------

st.subheader("Protected Areas")

st.dataframe(
    filtered[
        [
            "Name",
            "Type",
            "State",
            "Flora",
            "Fauna",
            "Area (sq km)"
        ]
    ],
    use_container_width=True
)

st.divider()
