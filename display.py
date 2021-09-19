import streamlit as st
import pandas as pd

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
    df.loc[i, "Votes"] = df.loc[i].Votes + 1

def app():
    st.title("Display Posts")
    st.write('''---''')
    for i in range(0, len(df)):
        # container = st.container()
        # container.write(df.loc[i].Title)
        with st.container(): # st.expander(container):
            st.header(df.loc[i].Title)
            st.subheader(df.loc[i].Description)
            col1, col2, col3 = st.columns(3)
            col2.caption("Event idea from " + df.loc[i].Dorm)
            col1.caption(df.loc[i].Invite)
            if st.button("Upvote", key=i):
                like(i)
            st.write(df.loc[i].Votes)
            st.write('''---''')