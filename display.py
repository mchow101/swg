import streamlit as st
import pandas as pd

# fill in with importing data from database
# test for now
df = pd.DataFrame({
    "Title": pd.Series(["West Side Party", "Bumper Cars", "West Big Thing"]),
    "Description": pd.Series(["East Side Party but WG", "beep beep in west garage", "Joint with Next Big Thing"]),
    "Dorm": pd.Categorical(["East Campus", "East Campus", "Next"]), 
    "Invite": pd.Categorical(["All MIT Students", "WG Residents Only", "WG Residents Only"])
})

def app():
    st.title("Display Posts")

    for i in range(0, len(df)):
        with st.expander(df.loc[i].Title):
            st.subheader(df.loc[i].Description)
            st.caption(df.loc[i].Dorm)
            st.caption(df.loc[i].Invite)
            st.balloons()