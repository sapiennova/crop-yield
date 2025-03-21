import pandas as pd
import streamlit as st
import base64
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Function to encode image to base64 (handles both URLs and local file paths)
def get_base64_image(image_path):
    # If the image path is a URL, download the image
    if image_path.startswith('http'):
        response = requests.get(image_path)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
        else:
            raise ValueError("Failed to fetch image from URL.")
    else:
        # If it's a local file path, open and read it
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()

# Load the crop yield data
data = pd.read_csv('crop_yield.csv')

# Check if 'Yield' column is already in the dataset, if not, calculate it
if 'Yield' not in data.columns:
    data['Yield'] = data['Production'] * 1000 / data['Area']

# One-hot encode categorical columns like 'Crop', 'Season', and 'State'
data = pd.get_dummies(data, columns=['Crop', 'Season', 'State'], drop_first=True)

# Absolute URL to Background image
bg_image_url = 'https://images.unsplash.com/photo-1560493676-04071c5f467b?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

# Get the base64 encoded image
encoded_image = get_base64_image(bg_image_url)

# Select features (X) and target variable (Y) for the model
features = data.drop(columns=['Production', 'Yield', 'Crop_Year'])  # Drop unnecessary columns, including 'Crop_Year'
target = data['Yield']  # We want to predict 'Yield'

# Split the data into training and testing sets (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Create and train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Extract unique values for Crop, Season, and State (for dropdowns in Streamlit)
crop_columns = [col for col in data.columns if col.startswith('Crop_')]
# Remove the column 'Crop_Year' if it exists in the crop columns list
crop_columns = [col for col in crop_columns if col != 'Crop_Year']
unique_crops = [col.replace('Crop_', '') for col in crop_columns]

season_columns = [col for col in data.columns if col.startswith('Season_')]
unique_seasons = [col.replace('Season_', '') for col in season_columns]

state_columns = [col for col in data.columns if col.startswith('State_')]
unique_states = [col.replace('State_', '') for col in state_columns]

# Define a function to make predictions based on user inputs
def predict_and_estimate(crop, season, state, area_hectares, rainfall):
    
    # Create a dictionary to store the input data for prediction
    input_data = {
        'Area': area_hectares,
        'Annual_Rainfall': rainfall
    }

    # Add the one-hot encoded values for Crop, Season, and State
    for col in features.columns:
        if col == f'Crop_{crop}':
            input_data[col] = 1
        elif col == f'Season_{season}':
            input_data[col] = 1
        elif col == f'State_{state}':
            input_data[col] = 1
        else:
            input_data[col] = 0

    # Make the prediction using the trained model
    yield_value = model.predict(pd.DataFrame(input_data, index=[0]))[0]

    # Estimate pesticide and fertilizer needs (just basic assumptions here)
    pesticide_per_hectare = yield_value * 0.5  # Example estimation
    fertilizer_per_hectare = yield_value * 100  # Example estimation

    total_yield = yield_value * area_hectares  # Total yield based on area

    yield_per_hectare = yield_value  # Assign a different variable for yield per hectare

    # Apply logic to prevent unnatural output
    if yield_value < 0 or total_yield < 0 or pesticide_per_hectare < 0 or fertilizer_per_hectare < 0:
        return "Error: The calculated values are not valid. Please check the input data."

    # Also check for extremely low or unreasonable values for yield and pesticide/fertilizer
    if yield_value < 0.1 or pesticide_per_hectare > 1000 or fertilizer_per_hectare > 5000:
        return "Warning: The estimated values are outside the expected range. Please verify your inputs."

    return total_yield, yield_per_hectare, pesticide_per_hectare, fertilizer_per_hectare

# Streamlit UI
# Page title and Icon
st.set_page_config(
    page_title="Smart Harvest",
    page_icon="🌾",
)

# Adding Background Image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{encoded_image}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh 100vw;
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
    .stForm {{
        background-color: rgba(100, 100, 100, 0.7);  /* Opaque background for the form */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display title inside a grey box
st.markdown("<div class='stTitle'>🌾 Crop Yield Estimation</div>", unsafe_allow_html=True)

# Create a form
with st.form(key="crop_yield_form", clear_on_submit=False):
    # Form elements are now directly placed within the form context
    crop = st.selectbox("Select Crop Type", unique_crops)
    season = st.selectbox("Select Season", unique_seasons)
    state = st.selectbox("Select State", unique_states)

    area_hectares = st.number_input("Enter Land Area (hectare)", min_value=0.0, value=1.0)
    rainfall = st.number_input("Enter Annual Rainfall (mm)", min_value=0.0, value=1000.0)

    # Submit button to trigger the estimation
    submit_button = st.form_submit_button(label="Estimate Yield")

# Calculate and display results when button is clicked
if submit_button:
    result = predict_and_estimate(crop, season, state, area_hectares, rainfall)

    if isinstance(result, str):  # If the result is an error or warning message
        st.error(result)
    else:
        total_yield, yield_per_hectare, pesticide, fertilizer = result

        # Display results with a simple, friendly style
        st.markdown(""" 
            <style>
                .result-box {
                    background-color: #f2f7fb;
                    border-left: 4px solid #4285F4;
                    padding: 20px;
                    margin-top: 20px;
                    border-radius: 8px;
                    font-family: 'Arial', sans-serif;
                }
                .result-box h3 {
                    color: #4285F4;
                    font-size: 22px;
                    margin-bottom: 10px;
                }
                .result-box p {
                    font-size: 16px;
                    line-height: 1.6;
                    color: #333;
                }
                .result-title {
                    font-weight: bold;
                    font-size: 18px;
                    color: #444;
                }
                .result-box-footer {
                    background-color: #4285F4;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    font-size: 14px;
                    margin-top: 20px;
                    text-align: center;
                }
            </style>
        """, unsafe_allow_html=True)

        # Total yield result box
        st.markdown(f"""
        <div class="result-box">
            <h3>🌾 Crop Yield Estimation</h3>
            <p class="result-title">Total Yield:</p>
            <p>{total_yield:.2f} tonnes</p>
            <p class="result-title">Yield per Hectare:</p>
            <p>{yield_per_hectare:.2f} tonnes</p>
        </div>
        """, unsafe_allow_html=True)

        # Pesticide and Fertilizer result box
        st.markdown(f"""
        <div class="result-box">
            <p class="result-title">🧪 Pesticide Needed per Hectare:</p>
            <p>{pesticide:.2f} kg</p>
            <p class="result-title">🌱 Fertilizer Needed per Hectare:</p>
            <p>{fertilizer:.2f} kg</p>
        </div>
        """, unsafe_allow_html=True)

        # More descriptive message
        st.markdown(f"""
        <div class="result-box-footer">
            📊 These values are approximate and based on the data you've entered. Please use them as a rough guide to help with planning.
        </div>
        """, unsafe_allow_html=True)
