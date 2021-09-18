import streamlit as st
import display
import form


on_display = True
on_form = False

st.sidebar.title('Save West Garage')

pages = {"Form":form,"Display":display}

choice = st.sidebar.selectbox("Navigation",["Form","Display"])

pages[choice].app()

