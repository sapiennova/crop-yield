import streamlit as st
from pages import Home, Crop_Yield_Estimation, Tips, About_us, FAQs

# Define pages
PAGES = {
    "Home": Home,
    "Crop Yield Estimation": Crop_Yield_Estimation,
    "Tips": Tips,
    "About Us": About_us,
    "FAQ": FAQs,
}

# Streamlit UI setup
st.set_page_config(page_title="Smart Harvest", page_icon="🌾", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Render the selected page
page = PAGES[selection]
if selection == "Home":
    page.home_page()
elif selection == "Crop Yield Estimation":
    page.estimation_page()
elif selection == "Tips":
    page.tips_page()
elif selection == "About Us":
    page.aboutus_page()
elif selection == "FAQ":
    page.faq_page()
