import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "Main menu",
    ("Food", "Game", "Movie")
    )

with st.sidebar:
    add_radio = st.radio(
        "Choose your favorite activity",
        ("play games", "Watch movies")
    )