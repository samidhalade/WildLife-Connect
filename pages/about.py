import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide"
)

st.title("About WildLife Connect")

st.markdown("---")

st.header("Project Overview")

st.write("""
WildLife Connect is an interactive web dashboard developed to
bring together information about India's Wildlife Sanctuaries
and National Parks into one platform.

The dashboard allows users to explore protected areas through
interactive maps, search locations, filter wildlife reserves,
and learn about their biodiversity.
""")

st.markdown("---")

st.header("Project Objectives")

st.write("""
• Create a centralized platform for protected areas.

• Help users explore India's biodiversity.

• Provide wildlife information in an interactive manner.

• Assist users in planning wildlife trips.

• Promote wildlife conservation awareness.
""")

st.markdown("---")

st.header("Features")

st.write("""
Interactive Maps

Wildlife Sanctuary Map

National Park Map

Search Locations

Filter by State

Flora & Fauna Information

Wildlife Explorer

Trip Planner

Place Details

SQLite Database
""")

st.markdown("---")

st.header("Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Frontend")

    st.write("""
• Streamlit

• HTML

• CSS

• Folium
""")

with col2:

    st.subheader("Backend")

    st.write("""
• Python

• Pandas

• SQLite

• Streamlit
""")

st.markdown("---")

st.header("Future Enhancements")

st.write("""
• Live weather information

• Nearby hotels

• Travel routes

• Entry fees

• Wildlife gallery

• Animal identification

• AI Trip Planner

• Wildlife recommendation system
""")

st.markdown("---")

st.header("Developer")

st.write("""
**Samidha Lade**

B.Tech Computer Science Engineering

SRM Institute of Science and Technology

WildLife Connect was developed as an interactive dashboard
to make information about India's protected areas easily
accessible and visually engaging.
""")

st.markdown("---")

st.success(
    "Thank you for exploring WildLife Connect!"
)