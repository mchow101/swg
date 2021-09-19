import streamlit as st
import pandas as pd
import os
import json
from cloudant import Cloudant
import emailevents

events_doc_name = "events"
db_name = 'events_db'
client = None
db = None
df = None
events_doc = None

def like(i, increment):
    global df
    global events_doc
    if increment > 0:
        st.balloons()
    df.loc[i, "Votes"] = df.loc[i].Votes + increment
    #vote number is a non zero multiple of 10 and was just increased
    if df.loc[i].Votes != 0 and df.loc[i].Votes % 10 == 0 and increment > 0:
        emailevents.email(df, i)
    # append to old data frame events_df
    events_doc['events_df'] = df.to_json()
    events_doc.save()

def app():
    global db
    global df
    global events_doc
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
    df = df.sort_values(by="Votes", ascending=False)
    df = df.reset_index(drop=True)
    st.title("Display Posts")
    st.write('''---''')
    containers = []
    for i in range(0, len(df)):
        containers.append(st.empty())
    for i in range(0, len(df)):
        with containers[i].container(): 
            st.header(df.loc[i].Title)
            st.subheader(df.loc[i].Description)
            col1, col2, col3 = st.columns(3)
            col2.caption("Event idea from " + df.loc[i].Dorm)
            col1.caption(df.loc[i].Invite)
            col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
            if col2.button("Upvote", key=2*i):
                like(i, 1)
            if col3.button("Downvote", key=2*i + 1):
                like(i, -1)
            col1.subheader("Votes: " + str(df.loc[i].Votes))
            st.write('''---''')