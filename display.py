import streamlit as st
import pandas as pd
import os
import json
from cloudant import Cloudant

events_doc_name = "events"
db_name = 'events_db'
client = None
db = None
events_df = None

# fill in with importing data from database
# test for now
df = pd.DataFrame({
    "Title": pd.Series(["West Side Party", "Bumper Cars", "West Big Thing"]),
    "Description": pd.Series(["East Side Party but WG", "beep beep in west garage", "Joint with Next Big Thing"]),
    "Dorm": pd.Categorical(["East Campus", "East Campus", "Next"]), 
    "Invite": pd.Categorical(["All MIT Students", "WG Residents Only", "WG Residents Only"]), 
    "Votes": 0
})
def like(i):
    st.balloons()
    events_df.loc[i, "Votes"] = events_df.loc[i].Votes + 1

def app():
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
        events = db[events_doc_name]["events_df"]
    else:
        events_df = pd.DataFrame(columns=['Title', 'Description', 'Dorm', 'Invite', 'Votes'])
        events_doc = db.create_document({
            "_id": events_doc_name,
            "events_df": events_df
        })

    st.title("Display Posts")
    st.write('''---''')
    for i in range(0, len(events_df)):
        # container = st.container()
        # container.write(events_df.loc[i].Title)
        with st.container(): # st.expander(container):
            st.header(events_df.loc[i].Title)
            st.subheader(events_df.loc[i].Description)
            col1, col2, col3 = st.columns(3)
            col2.caption("Event idea from " + events_df.loc[i].Dorm)
            col1.caption(events_df.loc[i].Invite)
            if st.button("Upvote", key=i):
                like(i)
            st.write(events_df.loc[i].Votes)
            st.write('''---''')