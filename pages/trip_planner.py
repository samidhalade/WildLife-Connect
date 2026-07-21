import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Trip Planner",
    layout="wide"
)

st.title("Wildlife Trip Planner")

st.write(
    "Plan your visit to India's Wildlife Sanctuaries and National Parks."
)

st.divider()

parks = pd.read_csv("data/national_parks.csv")
sanctuaries = pd.read_csv("data/sanctuaries.csv")

parks["Type"] = "National Park"
sanctuaries["Type"] = "Wildlife Sanctuary"

places = pd.concat(
    [parks, sanctuaries],
    ignore_index=True
)

def get_itinerary(place):

    tiger = [
        "Jim Corbett National Park",
        "Bandhavgarh National Park",
        "Kanha National Park",
        "Bandipur National Park",
        "Ranthambore National Park",
        "Bhadra Wildlife Sanctuary",
        "Wayanad Wildlife Sanctuary"
    ]

    birds = [
        "Vedanthangal Bird Sanctuary",
        "Ranganathittu Bird Sanctuary",
        "Bharatpur Bird Sanctuary",
        "Nal Sarovar Bird Sanctuary"
    ]

    mangrove = [
        "Sundarbans National Park",
        "Bhitarkanika Wildlife Sanctuary"
    ]

    mountains = [
        "Hemis National Park"
    ]

    rhino = [
        "Kaziranga National Park"
    ]

    if place in tiger:

        return [
            "Arrival • Hotel Check-in • Evening Nature Walk",
            "Early Morning Jeep Safari • Tiger Tracking • Wildlife Photography",
            "Forest Trail • Interpretation Centre • Bird Watching",
            "Nearby Village Visit • Sunset Point • Campfire",
            "Morning Safari • Souvenir Shopping • Departure"
        ]

    elif place in birds:

        return [
            "Arrival • Wetland Walk",
            "Early Morning Bird Watching • Boating",
            "Photography Session • Nature Trail",
            "Bird Interpretation Centre • Sunset Photography",
            "Departure"
        ]

    elif place in mangrove:

        return [
            "Arrival • Village Visit",
            "Mangrove Boat Safari",
            "Crocodile Spotting • Bird Watching",
            "Nature Photography",
            "Departure"
        ]

    elif place in mountains:

        return [
            "Arrival at Leh",
            "Visit Hemis National Park",
            "Snow Leopard Trail",
            "Monastery Visit • Stargazing",
            "Departure"
        ]

    elif place in rhino:

        return [
            "Arrival",
            "Elephant Safari",
            "Jeep Safari • Rhino Photography",
            "Orchid Park Visit",
            "Departure"
        ]

    else:

        return [
            "Arrival",
            "Safari",
            "Nature Walk",
            "Photography",
            "Departure"
        ]

def get_checklist(place):

    tiger = [
        "Jim Corbett National Park",
        "Bandhavgarh National Park",
        "Kanha National Park",
        "Bandipur National Park",
        "Ranthambore National Park",
        "Bhadra Wildlife Sanctuary",
        "Wayanad Wildlife Sanctuary"
    ]

    birds = [
        "Vedanthangal Bird Sanctuary",
        "Ranganathittu Bird Sanctuary",
        "Bharatpur Bird Sanctuary",
        "Nal Sarovar Bird Sanctuary"
    ]

    mangrove = [
        "Sundarbans National Park",
        "Bhitarkanika Wildlife Sanctuary"
    ]

    mountains = [
        "Hemis National Park"
    ]

    rhino = [
        "Kaziranga National Park"
    ]

    if place in tiger:

        return [
            "Camera",
            "Identity Proof",
            "Comfortable Walking Shoes",
            "Cap / Hat",
            "Sunglasses",
            "Sunscreen",
            "Water Bottle",
            "Power Bank",
            "Mosquito Repellent"
        ]

    elif place in birds:

        return [
            "Binoculars",
            "Camera",
            "Bird Guide / Notebook",
            "Cap",
            "Water Bottle",
            "Comfortable Shoes",
            "Power Bank"
        ]

    elif place in mangrove:

        return [
            "Raincoat",
            "Mosquito Repellent",
            "Waterproof Bag",
            "Camera",
            "Binoculars",
            "Water Bottle",
            "First Aid Kit"
        ]

    elif place in mountains:

        return [
            "Thermal Jacket",
            "Woollen Gloves",
            "Trekking Shoes",
            "Woollen Cap",
            "UV Sunglasses",
            "Medicines",
            "Power Bank"
        ]

    elif place in rhino:

        return [
            "Camera",
            "Cap",
            "Water Bottle",
            "Comfortable Shoes",
            "Sunglasses",
            "Power Bank"
        ]

    else:

        return [
            "Camera",
            "Water Bottle",
            "Comfortable Shoes"
        ]


col1, col2 = st.columns(2)

with col1:

    traveller = st.text_input(
        "Your Name"
    )

    destination = st.selectbox(
        "Choose Destination",
        places["Name"]
    )

    travellers = st.number_input(
        "Number of Travellers",
        min_value=1,
        max_value=20,
        value=1
    )

with col2:

    travel_date = st.date_input(
        "Travel Date"
    )

    days = st.slider(
        "Trip Duration (Days)",
        min_value=1,
        max_value=10,
        value=3
    )

    budget = st.selectbox(
        "Budget",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

st.divider()

if "generated" not in st.session_state:
    st.session_state.generated = False

if st.button("Generate Trip Plan"):

    st.session_state.generated = True
    st.session_state.destination = destination
    st.session_state.days = days
    st.session_state.travellers = travellers
    st.session_state.budget = budget
    st.session_state.traveller = traveller

if st.session_state.generated:

    data = places[
        places["Name"] == st.session_state.destination
    ].iloc[0]

    st.divider()

    folder = (
        "national_parks"
        if data["Type"] == "National Park"
        else "sanctuaries"
    )

    image_path = f"images/{folder}/{data['Image']}"

    try:

        st.image(
            image_path,
            width=500
        )

    except Exception:

        st.info("Image not available.")

    st.header("Destination Information")

    left, right = st.columns(2)

    with left:

        st.metric(
            "Destination",
            data["Name"]
        )

        st.metric(
            "Type",
            data["Type"]
        )

        st.metric(
            "State",
            data["State"]
        )

        st.metric(
            "Area",
            f"{data['Area (sq km)']} sq km"
        )

        st.metric(
            "Established",
            data["Established"]
        )

    with right:

        st.metric(
            "Entry Fee",
            f"₹{data['Entry Fee']}"
        )

        st.metric(
            "Timings",
            data["Timings"]
        )

        st.metric(
            "Best Season",
            data["Best Season"]
        )

        st.metric(
            "Travellers",
            st.session_state.travellers
        )

        st.metric(
            "Duration",
            f"{st.session_state.days} Days"
        )

    st.divider()

    st.subheader("About")

    st.write(data["Description"])

    st.subheader("Flora")

    st.write(data["Flora"])

    st.subheader("Fauna")

    st.write(data["Fauna"])

    st.divider()

    st.header("Travel Information")

    st.write(f"**Nearest Airport:** {data['Nearest Airport']}")

    st.write(f"**Nearest Railway Station:** {data['Nearest Railway Station']}")

    st.write(f"**Nearest Bus Stand:** {data['Nearest Bus Stand']}")

    st.write(f"**Nearest City:** {data['Nearest City']}")

    st.markdown(
        f"📍 [Open Google Maps]({data['Google Maps']})"
    )

    st.markdown(
        f"[Official Website]({data['Official Website']})"
    )

    st.divider()

    st.header("Estimated Budget")

    if st.session_state.budget == "Low":

        hotel = 1500

    elif st.session_state.budget == "Medium":

        hotel = 3000

    else:

        hotel = 6000

    total = (
        hotel * st.session_state.days
        + int(data["Entry Fee"]) * st.session_state.travellers
        + 800 * st.session_state.days
    )

    st.success(f"Estimated Trip Cost: ₹{total:,}")

    st.divider()

    # -----------------------------
    # SUGGESTED ITINERARY
    # -----------------------------

    st.header("Suggested Itinerary")

    itinerary = get_itinerary(data["Name"])

    total_days = st.session_state.days

    for day in range(total_days):

        with st.expander(f"Day {day + 1}"):

            st.write(itinerary[day])

    st.divider()

    # -----------------------------
    # PACKING CHECKLIST
    # -----------------------------

    st.header("Packing Checklist")

    st.write(
        "Recommended items to carry for your trip:"
    )

    checklist = get_checklist(data["Name"])

    for item in checklist:

        st.markdown(f"✅ {item}")

    st.divider()

    st.header("Travel Tips")

    tips = []

    if data["Type"] == "National Park":

        tips.extend([
            "Book safari tickets in advance.",
            "Carry a camera with extra batteries.",
            "Maintain silence during safaris.",
            "Do not litter inside the park."
        ])

    else:

        tips.extend([
            "Carry binoculars for bird watching.",
            "Wear comfortable walking shoes.",
            "Stay on designated nature trails.",
            "Avoid disturbing wildlife."
        ])

    if data["Name"] == "Hemis National Park":

        tips.extend([
            "Carry warm clothes.",
            "Stay hydrated due to high altitude."
        ])

    elif data["Name"] == "Sundarbans National Park":

        tips.extend([
            "Follow boat safety instructions.",
            "Carry mosquito repellent."
        ])

    elif data["Name"] == "Kaziranga National Park":

        tips.extend([
            "Keep a safe distance from rhinos.",
            "Visit during early morning safaris."
        ])

    for tip in tips:

        st.info(tip)

    st.divider()

    st.success(
        f"Your {st.session_state.days}-day trip to **{data['Name']}** has been planned successfully!"
    )
    st.divider()

    st.header("Travel Tips")

    tips = []

    if data["Type"] == "National Park":

        tips.extend([
            "Book safari tickets in advance.",
            "Carry a camera with extra batteries.",
            "Maintain silence during safaris.",
            "Do not litter inside the park."
        ])

    else:

        tips.extend([
            "Carry binoculars for bird watching.",
            "Wear comfortable walking shoes.",
            "Stay on designated nature trails.",
            "Avoid disturbing wildlife."
        ])

    if data["Name"] == "Hemis National Park":

        tips.extend([
            "Carry warm clothes.",
            "Stay hydrated due to high altitude."
        ])

    elif data["Name"] == "Sundarbans National Park":

        tips.extend([
            "Follow boat safety instructions.",
            "Carry mosquito repellent."
        ])

    elif data["Name"] == "Kaziranga National Park":

        tips.extend([
            "Keep a safe distance from rhinos.",
            "Visit during early morning safaris."
        ])

    for tip in tips:

        st.info(tip)

    st.divider()

    st.success(
        f"Your {st.session_state.days}-day trip to **{data['Name']}** has been planned successfully!"
    )