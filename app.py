import streamlit as st
import display
import form
from PIL import Image

st.sidebar.title('Save West Garage')

pages = {"Form":form,"Display":display}

st.sidebar.write("\n")
choice = st.sidebar.selectbox("Navigation",["Display","Form"])
pages[choice].app()

im = Image.open("C:/Users/iisim/Documents/GitHub/swg/wg-pic.jpg")
st.sidebar.image(im)
st.sidebar.write("\n\n\n\n")
st.sidebar.write("insert appropriate tagline here")
