import streamlit as st
import display
import form
from PIL import Image

st.sidebar.title('Save West Garage')

pages = {"Form":form,"Display":display}

st.sidebar.write("\n")
choice = st.sidebar.selectbox("Navigation",["Display","Form"])
pages[choice].app()


st.sidebar.markdown("<img src = \"https://s3.amazonaws.com/thetech-production/images/web_photos/web/9553_IMG_9447.jpg?1614818156\" width = 280 height = 210></img>",unsafe_allow_html=True)
st.sidebar.write("\n\n\n\n")
st.sidebar.write("insert appropriate tagline here")
