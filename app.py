import streamlit as st
import numpy as np
from PIL import Image
import joblib

model = joblib.load("alzheimer_model.pkl")

st.title("Alzheimer MRI Classifier")

uploaded_file = st.file_uploader("Sube una imagen MRI", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    image = image.resize((128,128))
    img_array = np.array(image).reshape(1, -1)

    prediction = model.predict(img_array)

    st.write("Predicción:", prediction[0])
