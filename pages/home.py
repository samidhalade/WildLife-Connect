import streamlit as st

st.set_page_config(
    page_title="Home",
    layout="wide"
)

st.title("WildLife Connect")

st.markdown(
    """
    ## Explore India's Protected Natural Heritage

    Discover Wildlife Sanctuaries and Conservation Areas across India.
    Learn about India's rich biodiversity, explore protected regions,
    and plan your next wildlife adventure.
    """
)

st.image(
    "images/hero/forest.jpg",
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Explore Map", use_container_width=True):
        st.switch_page("pages/explore_map.py")

with col2:
    if st.button("Learn More", use_container_width=True):
        st.write("Scroll down to learn more about wildlife conservation.")

st.divider()