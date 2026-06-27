import streamlit as st

st.logo("https://www.tasteofhome.com/wp-content/uploads/2018/01/Crispy-Fried-Chicken_EXPS_TOHJJ22_6445_DR-_02_03_11b-14.jpg", size="medium", link="https://www.tasteofhome.com/recipes/crispy-fried-chicken/")

st.sidebar.image("https://i.redd.it/94pwblzk4caf1.jpeg", width=200)
st.sidebar.subheader("""Nicholas😐""")

pages = {
    "Daily life": [
        st.Page("page1.py", title = "Page 1"),
        st.Page("page2.py", title = "Page 2")
    ],
    "favorite food": [
        st.Page("food.py", title = "Food")
    ]
}

pg = st.navigation(pages, position="top")
pg.run()
