import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Wildlife Explorer",
    layout="wide"
)

sanctuaries = pd.read_csv("data/sanctuaries.csv")
parks = pd.read_csv("data/national_parks.csv")

animals = sorted(
    list(
        set(
            sanctuaries["Fauna"].tolist() +
            parks["Fauna"].tolist()
        )
    )
)

st.title("Wildlife Explorer")

st.write(
    "Explore protected areas based on the wildlife you wish to see."
)

st.divider()

animal = st.selectbox(

    "Select an Animal",

    animals

)

st.header(f"Places where you can find {animal}")

sanctuary_results = sanctuaries[
    sanctuaries["Fauna"] == animal
]

park_results = parks[
    parks["Fauna"] == animal
]

if sanctuary_results.empty and park_results.empty:

    st.warning("No records found.")

else:

    if not sanctuary_results.empty:

        st.subheader("Wildlife Sanctuaries")

        st.dataframe(
            sanctuary_results[
                [
                    "Name",
                    "State",
                    "Flora",
                    "Area (sq km)"
                ]
            ],
            use_container_width=True
        )

    if not park_results.empty:

        st.subheader("National Parks")

        st.dataframe(
            park_results[
                [
                    "Name",
                    "State",
                    "Flora",
                    "Area (sq km)"
                ]
            ],
            use_container_width=True
        )

st.divider()

