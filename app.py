import streamlit as st
import display
import form


st.sidebar.title('Save West Garage')

pages = {"Form":form,"Display":display}

st.sidebar.write("\n")
choice = st.sidebar.selectbox("Navigation",["Display","Form"])
pages[choice].app()

