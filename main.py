import streamlit as st

st.title("Welcome to me web page! 🥳🥳🥳")
st.header("This is my blog")
st.subheader("This is the first post")

st.divider()

st.markdown(
'''
My name is Nicholas, and I am a student

'''
)

if st.button("Send balloons!"):
  st.balloons()

if st.button("Send snowflakes!"):
  st.snow()