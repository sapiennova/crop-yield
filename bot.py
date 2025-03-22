import streamlit as st
import google.generativeai as genai

def callbot():
    # Load API Key securely
    GENAI_API_KEY = "AIzaSyAuWjWVjVM-jGsoFy-hp8xr2JL97-_aekc"  # Add your API Key here
    genai.configure(api_key=GENAI_API_KEY)

    # Initialize Gemini AI model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Streamlit Page Configuration
    st.set_page_config(page_title="Smart Harvest", layout="wide")

    # Initialize session states
    if "chat_open" not in st.session_state:
        st.session_state["chat_open"] = False

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Function to toggle chatbot visibility
    def toggle_chat():
        st.session_state["chat_open"] = not st.session_state["chat_open"]

    
    # **Language Selection Dropdown**
    language_options = {"English": "english", "Hindi": "hindi", "Tamil": "tamil", "Gujarati": "gu"}
    #selected_language = st.selectbox("🌍 Choose Language:", list(language_options.keys()))

    # Update session state with selected language
    st.session_state["selected_lang"] = 'en'#language_options[selected_language]
    # **Google Translate HTML Embed**
    st.markdown("""
        <div id="google_translate_element"></div>
        <script type="text/javascript">
            function googleTranslateElementInit() {
                new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'en,hi,ta,gu', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
            }
        </script>
        <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
        <style>
            #google_translate_element {
                text-align: right;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Floating Chatbot Button
    if not st.session_state["chat_open"]:
        if st.button("💬 Open Chatbot", key="open_chat"):
            st.session_state["chat_open"] = True  

    # Floating Chatbot Container (Appears When Opened)
    if st.session_state["chat_open"]:
        with st.container():
            st.markdown('<div class="floating-chat">', unsafe_allow_html=True)

            col1, col2 = st.columns([4, 1])
            col1.subheader("🤖 Chatbot")
            if col2.button("✖ Close Bot", key="close_chat"):
                st.session_state["chat_open"] = False
                st.rerun()

            # Display chat history
            chat_history = st.container()
            for msg in st.session_state["messages"]:
                chat_history.write(msg)

            # User input
            user_input = st.text_input("Type your message:", key="user_input")

            if st.button("Send", key="send_message") and user_input:
                st.session_state["messages"].append(f"**You:** {user_input}")

                # Get AI response
                response = model.generate_content(user_input)  # No translation needed
                bot_reply = response.text

                st.session_state["messages"].append(f"**Bot:** {bot_reply}")
                st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)
