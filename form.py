import streamlit as st

def app():
    st.title("Form")
    with st.form(key='my_form',clear_on_submit=True):
        event_title = st.text_input(label='Event Title:')
        event_description = st.text_area(label = "Event Description:", height = 24)
        
        
        leftcol,rightcol = st.columns(2)

        
       
        
        dorm = leftcol.selectbox("Your Dorm:",["","Baker","Burton Conner","East Campus","McCormick","Maseeh","MacGregor","Next","New","Random","Simmons","West Garage","FSILG","Off Campus","Other"])


        status = rightcol.selectbox("Who is invited?",["","WG Residents Only", "All MIT Students","Other"])
        

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            # check if all mandatory inputs are valid
            if event_title and event_description and dorm != " " and status != " ":
                st.balloons()
