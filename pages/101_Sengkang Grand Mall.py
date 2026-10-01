import streamlit as st

st.set_page_config(
    page_title="Sengkang Grand Mall"
)

st.header("Sengkang Grand Mall")

st.write("Select alternative carpark.")
if st.button("Blk 281 MSCP (08 min walk)"): # creates a button that leads to this specific carpark called Blk 281 MSCP
    st.switch_page("pages/201_Blk 281 MSCP.py")

st.write("Return to main page") #Create a back button if the user wishes to return to main page
if st.button("Main Page"):
    st.switch_page("Home.py")
