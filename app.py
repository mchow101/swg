import streamlit as st
import display
import form
# from pillow import Image

st.sidebar.title('Save West Garage')

pages = {"Form":form,"Display":display}

st.sidebar.write("\n")
choice = st.sidebar.selectbox("Navigation",["Display","Form"])
pages[choice].app()


st.sidebar.markdown("<img src = \"https://s3.amazonaws.com/thetech-production/images/web_photos/web/9553_IMG_9447.jpg?1614818156\" width = 280 height = 210></img>",unsafe_allow_html=True)
st.sidebar.write("\n\n\n\n")
st.sidebar.write("West Garage Culture needs your help!\n\nSubmit your best and brightest event ideas via the form. Then, upvote your favorites, and downvote the ideas of your enemies.\n\nThe most popular ideas will be promoted to West Garage citizens directly.")
