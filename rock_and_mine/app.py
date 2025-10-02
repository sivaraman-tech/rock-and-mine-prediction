import streamlit as st
import numpy as np
import pickle

# Load the saved model
model = pickle.load(open("rock_mine_model.pkl", "rb"))

st.title("🔍 Rock vs Mine Prediction")
st.write("Enter sonar data features to predict whether it is Rock or Mine")

# Input from user
input_data = st.text_area("Enter 60 sonar values (comma separated):")

if st.button("Predict"):
    try:
        # Convert input into numpy array
        features = np.array([list(map(float, input_data.split(",")))])
        
        # Predict
        prediction = model.predict(features)[0]
        
        if prediction == "R":
            st.success("✅ The object is a **Rock**")
        else:
            st.success("💣 The object is a **Mine**")
    except:
        st.error("⚠️ Please enter valid 60 numeric values separated by commas.")
