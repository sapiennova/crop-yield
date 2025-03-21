import streamlit as st

# Function to show a collapsible FAQ section
def faq_section(question, answer):
    with st.expander(question):
        st.write(answer)

# Streamlit app structure
def app():
    st.set_page_config(page_title="FAQ - Crop Yield Estimation", layout="wide")

    # Heading
    st.title("Frequently Asked Questions")

    # FAQ Sections
    faq_section("👉 How do I estimate my crop yield?", 
                "Enter your crop details, land area, and rainfall in the tool. The system will calculate an estimate based on historical data.")
    
    faq_section("👉 What should I do if my yield is low?", 
                "Check soil quality, optimize irrigation, and use recommended fertilizers and pesticides.")
    
    faq_section("👉 How accurate is the prediction?", 
                "The prediction is based on available data and may vary due to changes in weather, soil conditions, and farming practices.")
    
    # Add more FAQs as needed
    faq_section("👉 Can I use the tool for different crops?", 
                "Yes, the tool supports a variety of crops. Just enter the specific crop details for each case.")

# Run the app
if __name__ == "__main__":
    app()
