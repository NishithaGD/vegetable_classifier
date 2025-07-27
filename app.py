import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load your trained model
model = load_model('your_model.h5')

# Define the class names (update these to match your training labels)
class_names = [
    "Beans", "Bitter Gourd", "Bottle Gourd", "Brinjal", "Broccoli", 
    "Cabbage", "Capsicum", "Carrot", "Cauliflower", "Cucumber", 
    "Papaya", "Potato", "Pumpkin", "Radish", "Tomato"
]
# Streamlit UI
st.title("Vegetable Image Classification🥕🍅🫛")
st.write("Upload a vegetable image and the model will predict its class.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    img_resized = img.resize((150, 150))  # Your model expects 150x150 input
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 150, 150, 3)
    img_array = img_array / 255.0  # Normalize

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.success(f"Predicted Vegetable: **{predicted_class}**")
    st.info(f"Confidence: {confidence:.2f}")
