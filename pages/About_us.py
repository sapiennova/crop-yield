import streamlit as st

# Custom CSS to replicate your original style
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        .heading {
            text-align: center;
            color: #fff;
            background-color: #2c3e50;
            padding: 15px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        p {
            text-align: center;
            color: #555;
        }
        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        label {
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            transition: 0.3s;
        }
        input:focus, textarea:focus {
            border-color: #28a745;
            box-shadow: 0 0 5px rgba(40, 167, 69, 0.5);
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background-color: #218838;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("<div class='heading'>About Us</div>", unsafe_allow_html=True)

# Text content
st.write("Welcome to the Crop Yield Estimation project. Our mission is to help farmers make data-driven decisions by providing accurate yield predictions.")

# Embed video
st.markdown("<div class='heading'>Watch Our Introduction</div>", unsafe_allow_html=True)
st.video("https://www.youtube.com/embed/LjK22MtE4Vs")

# Contact form
st.markdown("<div class='heading'>Contact Us</div>", unsafe_allow_html=True)

# Form submission logic
with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message", height=150)
    
    submit_button = st.form_submit_button("Send Message")
    
    if submit_button:
        # Display success message
        st.success("Your message has been sent successfully!")
        # Reset form fields after 3 seconds
        st.experimental_rerun()

# To ensure the button works and the form looks correct
