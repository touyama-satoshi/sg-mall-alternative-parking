import streamlit as st

st.set_page_config(
    page_title="Home Page"
) # The text that you see on your web browser's tab name

st.header("🇸🇬 Shopping Mall Alternative Carparks")

st.write("Select your shopping mall.")

if st.button("Sengkang Grand Mall"): # a button that brings you Sengkang Grand Mall's page (with its alternative carparks)
    st.switch_page("pages/101_Sengkang Grand Mall.py")
