
# 🌾 Crop Yield Estimation System

This Crop Yield Estimation System helps farmers, agricultural researchers, and decision-makers predict crop yields and estimate agricultural resource needs based on factors like crop type, season, state, land area, and rainfall. The system uses machine learning to predict yields and provides estimates for required resources such as pesticides and fertilizers.

## Features

- Predicts total yield and yield per hectare based on user input.
- Easy-to-use web interface built with Streamlit.
- Uses a linear regression model trained on historical crop yield data.
- Designed to help farmers and agricultural stakeholders plan and manage their crops efficiently.


## Key Inputs

- Total Yield: The predicted total yield in tonnes.
- Yield per Hectare: The predicted yield per hectare.
- Pesticide Needed per Hectare: Estimate of pesticide requirements based on predicted yield.
- Fertilizer Needed per Hectare: Estimate of fertilizer requirements based on predicted yield.
## Getting Started

Before running this project, you need to have Python installed along with the following libraries:

"pandas", 
"streamlit",
"scikit-learn" and
"base64"

``` pip install pandas streamlit scikit-learn```


## Run the application

Once you have the necessary libraries installed, you can run the Streamlit application with the following command in terminal:

```streamlit run cropyield.py```
## How it works

- Input Data: The user provides inputs like crop type, season, state, land area, and rainfall.
- Prediction: The system processes this input through a linear regression model trained on historical crop yield data and returns predictions for total yield and yield per hectare.
- Resource Estimation: The app also provides estimates for pesticide and fertilizer needs based on the predicted yield.
- Output: Results are displayed in an easy-to-understand format, with sections for each type of estimate (yield and resources).
## Libraries

- Data Source: Historical crop yield data .[https://www.kaggle.com/datasets/akshatgupta7/crop-yield-in-indian-states-dataset]
- Libraries: Built using Streamlit for the UI and scikit-learn for the machine learning model.