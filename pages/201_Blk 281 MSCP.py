import streamlit as st
import library

st.set_page_config(
    page_title="Blk 281 MSCP"
)

st.header("Blk 281 MSCP")

st.subheader("08 min walk to mall") #duration of walking mall to carpark and vice versa

lots_available = library.carpark_lots(url="https://api.data.gov.sg/v1/transport/carpark-availability",code="SK91") # ping the HDB carpark API to get lots available (refer to library on how the function works)
st.write(f"Lots Available: {lots_available}") #write down the lots available

st.image("assets/screenshot.png") #screenshot of a map showing the location of the carpark

st.subheader("Address") #writing the address
st.write("281 Sengkang East Ave")
st.write("Singapore 540281")

st.subheader("Google Maps Link Button") #having a google maps button that when clicked, leads straight to that place on google maps, where users can ask google maps to ask for directions
st.link_button("Google Maps","https://maps.app.goo.gl/ZSjVQKpGeMtCcV1c8") #Note: It's NOT an applet in the website, it redirects to the Google Maps App or the Google Maps website

st.subheader("Walking Route Videos")
st.write("Carpark to Mall")
st.video("https://youtu.be/XQUveA2kkiE") # shows the YouTube video of the sheltered walkway from Carpark to Mall
st.write("Mall to Carpark")
st.video("https://youtu.be/iFtiuHoMBpk") # shows the YouTube video of the sheltered walkway from Mall to Carpark

st.subheader("Remarks") #writing of other important relevant info here
st.write("Walkling path is 100% sheltered and 100% barrier-free")
st.write("White lots parking: Deck 2B onwards")
st.write("Lift access: Decks ending with A (eg. 1A, 2A, 3A, 4A...)")

if st.button("Back to Previous Page"): #create a "Previous Page" button to return to the previous page
    st.switch_page("pages/101_Sengkang Grand Mall.py")
if st.button("Back to Main Page"): #create a "Main Page" button to return to main page
    st.switch_page("Home.py")