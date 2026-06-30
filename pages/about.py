import streamlit as st

def show():

    st.title("About WildLife Connect")
    st.subheader("Learn more about our Project")

    st.divider()

    left, right = st.columns([3,1])

    with left:
        with st.container(border=True):
            st.header("About WildLife Connect")

            st.write("""
            WildLife Connect is an interactive web-based dashboard that brings together information about India's Wildlife Sanctuaries and Conservations on a single platform.

            The dashboard allows users to explore protected area through an interactive map, search for spectic locations, apply filters, and learn about the flora and fauna naturally found in each region. By coming all essential information into one place, the platform provides an easy and organised way to explore India's rich wildlife heritage.
            """)

    st.write("")

    left, right = st.columns([1,3])

    with right:
        with st.container(border=True):

            st.header("Our Objective")

            st.write("""
            The objective of WildLife Connect is to provide a centralized and interactive platform for exploring India's WildLife Sanctuaries and Conservations.

            The dashboard aims to simplify access to wildlife information, encourage awareness about biodiversity, and help students, researchers, wildlife enthusiasts and travellers discover protected area through maps, search functionality and intelligent filtering.
            """)

    st.write("")

    left, right = st.columns([3,1])

    with left:
        with st.container(border=True):

            st.header("Dashboard Features")

            st.write("• Interactive map showing all Wildlife Sancturies and Conservations in one place.")
            st.write("• Two different shades of green to clearly differentiate Wildlife sanctuaries and conservation.")
            st.write("• Separate map views for wildlife sanctuaries, conservations and combined view.")
            st.write("• Search functionality to directly locate any protected area.")
            st.write("• Filter options to explore protected area based on state, flora and fauna.")
            st.write("• Clicking on any location displays detailed information about that protected area.")
            st.write("• Clean and simple dashboard interface designed for easy navigation.")
            st.write("• Centralized information instead of requiring users to visit multiple websites.")
            st.write("• Easily expandable in the future by adding more protected areas and additional information.")