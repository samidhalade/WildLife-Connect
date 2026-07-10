import streamlit as st

st.set_page_config(
    page_title="WildLife Connect",
    layout="wide"
)

st.title("WildLife Connect")
st.subheader("Explore India's Wildlife Sanctuaries and National Parks")

st.image(
    "images/forest/forest.jpg",
    use_container_width=True
)

st.markdown("---")

st.header("Welcome")

st.write("""
Welcome to **WildLife Connect**, an interactive dashboard that helps users
explore Wildlife Sanctuaries and National Parks across India.

The dashboard provides an easy way to discover protected areas,
understand India's biodiversity and plan wildlife trips.
""")

st.markdown("---")

st.header("Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Wildlife Sanctuaries", "10")

with c2:
    st.metric("National Parks", "10")

with c3:
    st.metric("States Covered", "11")

with c4:
    st.metric("Species", "100+")

st.markdown("---")

st.header("What You Can Do")

col1, col2 = st.columns(2)

with col1:

    st.success("Explore")

    st.write("""
✔ Interactive Maps

✔ Search Protected Areas

✔ Filter by State

✔ View Wildlife Distribution

✔ Discover Biodiversity
""")

with col2:

    st.success("Learn")

    st.write("""
✔ Flora

✔ Fauna

✔ Area

✔ Year of Establishment

✔ Wildlife Information

✔ Plan Wildlife Trips
""")

st.markdown("---")

st.header("Featured Wildlife Sanctuaries")

col1, col2 = st.columns(2)

with col1:

    st.image(
        "images/sanctuaries/bhadra.jpg",
        use_container_width=True
    )

    st.subheader("Bhadra Wildlife Sanctuary")

    st.write("""
Located in Karnataka, Bhadra Wildlife Sanctuary is known for
its Bengal Tigers, elephants and evergreen forests.
""")

with col2:

    st.image(
        "images/sanctuaries/bharatpur.jpg",
        use_container_width=True
    )

    st.subheader("Keoladeo (Bharatpur) Sanctuary")

    st.write("""
One of the most famous bird sanctuaries in India and a UNESCO
World Heritage Site.
""")

st.markdown("---")

st.header("Featured National Parks")

col1, col2 = st.columns(2)

with col1:

    st.image(
        "images/national_parks/kaziranga.jpg",
        use_container_width=True
    )

    st.subheader("Kaziranga National Park")

    st.write("""
Kaziranga National Park is home to the world's largest population
of the One-Horned Rhinoceros.
""")

with col2:

    st.image(
        "images/national_parks/ranthambore.jpg",
        use_container_width=True
    )

    st.subheader("Ranthambore National Park")

    st.write("""
Ranthambore is one of India's best places to observe Bengal Tigers
in their natural habitat.
""")

st.markdown("---")

st.header("Did You Know?")

st.info("""
India is one of the world's 17 megadiverse countries and protects
thousands of plant and animal species through its protected areas.
""")

st.markdown("---")

st.caption(
    "WildLife Connect | Streamlit • Folium • SQLite • Python"
)