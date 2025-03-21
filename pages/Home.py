import streamlit as st

# Streamlit UI Configuration
st.set_page_config(
    page_title="Smart Harvest",
    page_icon="🌾",
)

# Adding Background Image (This assumes the image URL is hosted or available locally)
bg_image_url = "https://images.unsplash.com/photo-1560493676-04071c5f467b?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Custom CSS to style the Streamlit app
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{bg_image_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        color: white;
    }}
    
    .stTitle {{
        background-color: rgba(20, 20, 20, 1);  /* Grey background with transparency */
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        color: white;
        font-size: 40px;
        font-weight: bold;
    }}

    /* Navigation bar styling */
    nav {{
        background-color: #333;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        height: 40px;
        color: rgb(51, 34, 34);
    }}

    nav ul {{
        margin: 0;
        padding-left: 30px;
        list-style: none;
    }}

    nav li {{
        display: inline;
        float: left;
    }}

    nav a {{
        display: inline-block;
        width: 120px;
        text-align: center;
        text-decoration: none;
        padding: 10px 0;
        color: #eee;
    }}

    nav li:hover {{
        background-color: #444;
    }}

    /* Footer Styling */
    footer {{
        background-color: #333;
        padding: 1rem;
        text-align: center;
        font-size: 14px;
    }}

    footer .footer-cols {{
        display: grid;
        grid-gap: 20px;
        grid-template-columns: repeat(3, 1fr);
        padding: 2rem;
        text-align: left;
        font-size: 14px;
    }}

    footer .footer-cols ul {{
        list-style: none;
    }}

    footer .footer-cols ul li:first-child {{
        font-size: 1.2rem;
        padding-bottom: 0.5rem;
        border-bottom: #444 solid 2px;
        margin-bottom: 1rem;
    }}
    
    .container {{
        max-width: 1180px;
        text-align: center;
        margin: 0 auto;
        padding: 0 3rem;
        color: black;
        background-color: rgba(100, 100, 100, 0.7);  /* Opaque background for the form */
        padding: 50px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 20px;
    }}

    .btn {{
        padding: 1rem;
        color: #FFF;
        display: inline-block;
    }}
    
    .btn-primary {{
        background: #ED6100;
    }}
    
    .btn-primary:hover {{
        background: #FB8500;
    }}
    
    .btn-secondary {{
        background: #B20265;
    }}
    
    .btn-secondary:hover {{
        background: #ED0286;
    }}

    .text-light {{
        color: #f4f4f4;
    }}

    .mb {{
        margin-bottom: 1rem;
    }}
    .mt {{
        margin-top: 2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation bar HTML
st.markdown(
    """
    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Features</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>
    """,
    unsafe_allow_html=True
)

# Display title inside a grey box
st.markdown("<div class='stTitle'>🌾 Smart Harvest</div>", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <img src="https://plus.unsplash.com/premium_photo-1722682239737-4bc41d2b8c0d?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Smart Harvest Image" style="max-width:100%; height:auto; border-radius: 8px;">
    </div>
""", unsafe_allow_html=True)

# Add a container for the main content with the updated styles
st.markdown(""" 
    <div class="container">
        <p>
            Welcome to the Smart Harvest! <br>
            Select from the options below to estimate crop yields based on various factors.
        </p>
        <p>
            At Smart Harvest, we aim to provide advanced tools and insights to help farmers optimize their crop yields. Our system leverages the latest technology to predict crop performance based on environmental conditions, soil health, and historical data.
        </p>
        <p>
            Whether you are a small-scale farmer or part of a larger agricultural operation, our platform offers easy-to-understand predictions and recommendations to help you make data-driven decisions. By understanding crop growth patterns and external influences, you can increase efficiency and reduce risks associated with farming.
        </p>
        <p>
            Start your journey with Smart Harvest today and gain access to personalized insights that can transform your farming practices. No matter the crop or farming method, we are here to guide you every step of the way.
        </p>
        <div class="mt">
            <button class="btn btn-primary">Start Estimating</button>
            <button class="btn btn-secondary">Learn More</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer section
st.markdown(""" 
    <footer>
        <div class="footer-cols">
            <ul>
                <li>About</li>
                <li>Help</li>
                <li>Terms of Service</li>
            </ul>
            <ul>
                <li>Privacy Policy</li>
                <li>Contact Us</li>
                <li>Support</li>
            </ul>
            <ul>
                <li>Follow Us</li>
                <li>Facebook</li>
                <li>Twitter</li>
            </ul>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 Smart Harvest | All rights reserved.</p>
        </div>
    </footer>
""", unsafe_allow_html=True)
