import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Details",
    layout="wide"
)

sanctuaries = pd.read_csv("data/sanctuaries.csv")
parks = pd.read_csv("data/national_parks.csv")

selected = st.session_state.get("selected_place")

if selected is None:
    st.switch_page("pages/explore_map.py")

if selected in parks["Name"].values:

    place = parks[
        parks["Name"] == selected
    ].iloc[0]

    folder = "national_parks"

else:

    place = sanctuaries[
        sanctuaries["Name"] == selected
    ].iloc[0]

    folder = "sanctuaries"

st.title(place["Name"])

st.subheader(place["State"])

st.divider()

left, right = st.columns([1, 2])

with left:

    image_path = f"images/{folder}/{place['Image']}"

    try:

        st.image(
            image_path,
            width=320
        )

    except Exception:

        st.warning("Image not available.")

with right:

    st.metric(
        "Area",
        f"{place['Area (sq km)']} sq km"
    )

    st.metric(
        "Established",
        place["Established"]
    )

    st.metric(
        "Entry Fee",
        place["Entry Fee"]
    )

    st.metric(
        "Timings",
        place["Timings"]
    )

    st.metric(
        "Best Season",
        place["Best Season"]
    )

st.divider()

st.write("## Description")
st.write(place["Description"])

st.write("## Flora")
st.write(place["Flora"])

st.write("## Fauna")
st.write(place["Fauna"])

st.divider()

st.subheader("Travel Information")

st.write(f"**Nearest Airport:** {place['Nearest Airport']}")

st.write(f"**Nearest Railway Station:** {place['Nearest Railway Station']}")

st.write(f"**Nearest Bus Stand:** {place['Nearest Bus Stand']}")

st.write(f"**Nearest City:** {place['Nearest City']}")

st.markdown(
    f"[Open Google Maps]({place['Google Maps']})"
)

st.markdown(
    f"[Official Website]({place['Official Website']})"
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button("⬅ Back"):

        st.switch_page("pages/explore_map.py")

with col2:

    if st.button("Plan My Trip"):

        st.switch_page("pages/trip_planner.py")