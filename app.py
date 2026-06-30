import streamlit as st

from pages import about
from pages import sanctuaries
from pages import conservations
from pages import combined_map

st.set_page_config(
    page_title="WildLife Connect",
    layout="wide"
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

    elif st.session_state.page == "About":
        about.show()

    elif st.session_state.page == "Sanctuaries":
        sanctuaries.show()

    elif st.session_state.page == "Conservations":
        conservations.show()

    elif st.session_state.page == "Combined":
        combined_map.show()