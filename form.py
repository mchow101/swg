import streamlit as st

def app():
    st.title("Form")
    with st.form(key='my_form'):
        text_input = st.text_input(label='Enter some text')
        submit_button = st.form_submit_button(label='Submit')
