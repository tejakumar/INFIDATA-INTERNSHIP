import streamlit as st
from PIL import Image

st.header("Image Gallery")

st.info("My Image")
img=Image.open("img.png")
st.image(img,width=300)

st.info("Car Image")
img2=Image.open("img_1.png")
st.image(img2,width=400)
