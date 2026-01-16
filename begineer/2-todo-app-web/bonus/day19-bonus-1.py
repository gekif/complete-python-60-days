import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # Start camera
    camera_image = st.camera_input("Take a picture")

if camera_image:
    # Create pillow image instance
    img = Image.open(camera_image)

    # Convert pillow image to grayscale
    gray_img = img.convert("L")

    # Render grayscale image to app
    st.image(gray_img)



