import streamlit as st

st.title("Welcome to me web page! ")
st.header("This is my blog")
st.subheader("This is the first post")

st.divider()

st.markdown(
'''
My name is Nicholas, and I am a student, I love reading, fishing and sleeping, I live in the U.S. and I am 12 years old currently.

'''
)

if st.button("Send balloons!"):
  st.balloons()

if st.button("Send snowflakes!"):
  st.snow()