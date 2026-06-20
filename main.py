import streamlit as st

tab1, tab2, tab3 = st.tabs(['Home', 'About', 'Contact'])

with tab1:
    st.title("Welcome to me web page!🙂🙂🙂 ")
    st.header("This is my blog")
    st.subheader("This is the first post")

st.divider()

st.markdown(
'''
My name is Nicholas, and I am a student, I love reading, fishing and sleeping, I live in the U.S. and I am 12 years old currently.

'''
)

if st.button("Send balloons!🎈"):
  st.balloons()

if st.button("Send snowflakes!❄️"):
  st.snow()

from streamlit_extras.let_it_rain import rain
if st.button("rain"):
    ## rain function
    rain(
        emoji="💧",
        font_size=25,
        falling_speed=0.7,
        animation_length="10", # or an integer for seconds
    )

    # Look at your line 30 or 29. Make sure the closing parenthesis matches!
col1, col2, col3, col4, = st.columns(4)

with col1:
    st.image("sunny.jpg", caption="Get ready to know some fun fun facts!")
    st.image("MrHappy.jpg", caption="Animals are the best!")

with col2:
    st.image("dolphin.jpg")
    st.markdown("Dolphins sleep one half of their brain at a time presumably to avoid drowning")
    st.image("ostrich.jpg")
    st.markdown("Did you know that ostrich eyes are bigger than their brains?")