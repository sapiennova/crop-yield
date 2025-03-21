import streamlit as st

def aboutus_page():
    # Set page configuration
    st.set_page_config(page_title="About - Crop Yield Estimation", page_icon="🌱")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                text-align: center;
            }
            h1 {
                color: #2d7d46;
            }
            .tips {
                text-align: left;
                margin-top: 20px;
            }
            .tips h2 {
            text-align: center;
            color: #fff;
            background-color: #2c3e50;
            padding: 15px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 5px;
            margin-bottom: 20px;
            }
            .tips ul {
                list-style-type: none;
                padding: 0;
            }
            .tips li {
                background: #eaf4ea;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #666;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
   
    # Farming Tips
    st.markdown("""
        <div class="tips">
            <h2>🌱 Farming Tips & Suggestions</h2>
            <ul>
                <li>📌 Choose the right crop according to your soil type and climate.</li>
                <li>💧 Ensure proper irrigation techniques to optimize water usage.</li>
                <li>🌾 Use organic fertilizers for better soil health and sustainability.</li>
                <li>🔬 Regularly test soil quality for balanced nutrient levels.</li>
                <li>🐞 Apply integrated pest management techniques to reduce chemical dependency.</li>
                <li>📊 Keep records of past crop yields to improve future predictions.</li>
                <li>🛰️ Utilize modern AI and data-driven solutions for better decision-making.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div class="footer">
            <p>🌾 Developed to assist farmers with data-driven insights for better crop production.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
# Run the function if the script is executed
if __name__ == "__main__":
    aboutus_page()