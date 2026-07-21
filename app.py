import streamlit as st

st.set_page_config(
    page_title="WildLife Connect",
    layout="wide"
)

navigation = st.navigation(
    {
        "WildLife Connect": [

            st.Page(
                "home.py",
                title="Home",
            ),

            st.Page(
                "pages/explore_map.py",
                title="Explore Map",
            ),

            st.Page(
                "pages/sanctuaries.py",
                title="Wildlife Sanctuaries",
            ),

            st.Page(
                "pages/national_parks.py",
                title="National Parks",
            ),

            st.Page(
                "pages/monitoring.py",
                title="Monitoring & Surveillance",
    ),

            st.Page(
                "pages/trip_planner.py",
                title="Trip Planner",
            ),

            st.Page(
                "pages/about.py",
                title="About",
            ),

            st.Page(
                "pages/details.py",
                title="Details",
            )

        ]
    }
)

navigation.run()