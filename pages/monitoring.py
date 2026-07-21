import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Monitoring & Surveillance",
    layout="wide"
)

st.title("Monitoring & Surveillance")

st.write(
    "Monitor forest boundaries, wildlife movement and surveillance statistics."
)

st.divider()

monitoring = pd.read_csv("data/monitoring.csv")

parks = pd.read_csv("data/national_parks.csv")
sanctuaries = pd.read_csv("data/sanctuaries.csv")

locations = pd.concat([parks, sanctuaries], ignore_index=True)

data = monitoring.merge(
    locations[["Name", "Latitude", "Longitude"]],
    left_on="Place",
    right_on="Name",
    how="left"
)

safe = len(data[data["Boundary Status"] == "Safe"])

warning = len(data[data["Boundary Status"] == "Warning"])

critical = len(data[data["Boundary Status"] == "Critical"])

animals = data["Animals Near Boundary"].sum()

intrusions = data["Human Intrusions Today"].sum()

patrols = data["Drone Patrols"].sum()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Animals Near Boundary",
        animals
    )

with c2:
    st.metric(
        "Human Intrusions",
        intrusions
    )

with c3:
    st.metric(
        "Drone Patrols",
        patrols
    )

c4, c5, c6 = st.columns(3)

with c4:
    st.metric(
        "Safe Zones",
        safe
    )

with c5:
    st.metric(
        "Warning Zones",
        warning
    )

with c6:
    st.metric(
        "Critical Zones",
        critical
    )

st.divider()

st.header("Live Monitoring Map")

india = folium.Map(
    location=[22.5,79],
    zoom_start=5
)

for _, row in data.iterrows():

    if row["Boundary Status"] == "Safe":
        colour = "green"

    elif row["Boundary Status"] == "Warning":
        colour = "orange"

    else:
        colour = "red"

    popup = f"""
    <b>{row['Place']}</b><br><br>

    Boundary Status : {row['Boundary Status']}<br>

    Animals Near Boundary : {row['Animals Near Boundary']}<br>

    Boundary Crossings : {row['Boundary Crossings Today']}<br>

    Human Intrusions : {row['Human Intrusions Today']}<br>

    Drone Patrols : {row['Drone Patrols']}<br>

    Last Alert : {row['Last Alert']}
    """

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=8,
        color=colour,
        fill=True,
        fill_color=colour,
        fill_opacity=1,
        tooltip=row["Place"],
        popup=popup
    ).add_to(india)

st_folium(
    india,
    width=1100,
    height=650
)

st.divider()

st.header("Geo-Fencing Status")

for _, row in data.iterrows():

    with st.container():

        col1, col2 = st.columns([3,2])

        with col1:

            st.subheader(row["Place"])

            st.write(f"**Boundary Status:** {row['Boundary Status']}")

            st.write(
                f"**Animals Near Boundary:** {row['Animals Near Boundary']}"
            )

            st.write(
                f"**Boundary Crossings Today:** {row['Boundary Crossings Today']}"
            )

            st.write(
                f"**Last Alert:** {row['Last Alert']}"
            )

        with col2:

            if row["Boundary Status"] == "Safe":

                st.success("SAFE")

            elif row["Boundary Status"] == "Warning":

                st.warning("WARNING")

            else:

                st.error("CRITICAL")

        st.divider()