import streamlit as st
import pandas as pd
import os
import json
from cloudant import Cloudant

events_doc_name = "events"
db_name = 'events_db'
client = None
db = None

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
            if 'VCAP_SERVICES' in os.environ:
                vcap = json.loads(os.getenv('VCAP_SERVICES'))
                print('Found VCAP_SERVICES')
                if 'cloudantNoSQLDB' in vcap:
                    creds = vcap['cloudantNoSQLDB'][0]['credentials']
                    user = creds['username']
                    password = creds['password']
                    url = 'https://' + creds['host']
                    client = Cloudant(user, password, url=url, connect=True)
                    db = client.create_database(db_name, throw_on_exists=False)
            elif "CLOUDANT_URL" in os.environ:
                client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True)
                db = client.create_database(db_name, throw_on_exists=False)
            elif os.path.isfile('vcap-local.json'):
                with open('vcap-local.json') as f:
                    vcap = json.load(f)
                    print('Found local VCAP_SERVICES')
                    creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
                    user = creds['username']
                    password = creds['password']
                    url = 'https://' + creds['host']
                    client = Cloudant(user, password, url=url, connect=True)
                    db = client.create_database(db_name, throw_on_exists=False)

            if events_doc_name in db:
                events_doc = db[events_doc_name]
                df = pd.read_json(events_doc["events_df"])
            else:
                df = pd.DataFrame(columns=['Title', 'Description', 'Dorm', 'Invite', 'Votes'])
                events_doc = db.create_document({
                    "_id": events_doc_name,
                    "events_df": df.to_json()
                })
            #TODO mitali add more pandas stuff here
            # create new data frame with new info
            temp = pd.DataFrame({
                "Title": pd.Series([event_title]),
                "Description": pd.Series([event_description]),
                "Dorm": pd.Categorical([dorm]), 
                "Invite": pd.Categorical([status]), 
                "Votes": [1]
            })
            df = df.append(temp)
            df = df.reset_index(drop=True)

            # append to old data frame events_df
            events_doc['events_df'] = df.to_json()
            events_doc.save()
            

            # check if all mandatory inputs are valid
            if event_title and event_description and dorm != " " and status != " ":
                st.balloons()
