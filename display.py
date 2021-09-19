import streamlit as st
import pandas as pd

# fill in with importing data from database
# test for now
df = pd.DataFrame({
    "Title": pd.Series(["West Side Party", "Bumper Cars", "West Big Thing"]),
    "Description": pd.Series(["East Side Party but WG", "beep beep in west garage", "Joint with Next Big Thing"]),
    "Dorm": pd.Categorical(["East Campus", "East Campus", "Next"]), 
    "Invite": pd.Categorical(["All MIT Students", "WG Residents Only", "WG Residents Only"]), 
    "Votes": [0, 1, -2]
})
df = df.sort_values(by="Votes", ascending=False)
df = df.reset_index(drop=True)

def like(i, increment):
    global df
    if increment > 0:
        st.balloons()
    df.loc[i, "Votes"] = df.loc[i].Votes + increment

def app():
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