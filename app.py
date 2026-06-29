import streamlit as st

st.set_page_config(
    page_title="WildLife Connect",
    layout="wide"
)

st.title("WildLife Connect")
st.subheader("Interactive Dashboard for India's Wildlife Sanctuaries and Consercations")
st.divider()

top_left, top_right= st.columns([3,2])

with top_right:
    search = st.text_input(
        "Search",
        placeholder= "Search Sanctuary or Conservation"
    )

    filter1, filter2, filter3 = st.columns(3)

    with filter1: 
        state = st.selectbox(
            "State",
            ["Maharashtra", "Madhya Pradesh", "Gujarat", "Rajasthan", "Kerala", "Assam"]
        )

    with filter2:
        flora = st.selectbox(
            "Flora",
            ["Bamboo", "Teak", "Sal", "Sandalwood", "Rosewood"]
        )

    with filter3:
        fauna = st.selectbox(
            "Fauna",
                ["Tiger", "Lion", "Elephant", "Leopard", "Rhinoceros"]
        )

    st.divider()
    left_panel, centre_panel = st.columns([2,4])

    with left_panel:
        st.button("Home", use_container_width=True)
        st.button("Sanctuary Map", use_container_width=True)
        st.button("Conservation Map", use_container_width=True)
        st.button("Combined Map", use_container_width=True)
        st.button("About Us", use_container_width=True)

    with centre_panel:
        st.subheader("India Map")