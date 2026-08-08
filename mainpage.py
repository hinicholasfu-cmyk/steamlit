import streamlit as st

st.logo(
    "https://www.tasteofhome.com/wp-content/uploads/2018/01/Crispy-Fried-Chicken_EXPS_TOHJJ22_6445_DR-_02_03_11b-14.jpg", 
    size="medium", 
    link="https://www.tasteofhome.com/recipes/crispy-fried-chicken/"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Log in")
    with st.form("Login_form"):
        username = st.text_input("username")
        password = st.text_input("Password", type='password')
        submitted = st.form_submit_button("Log in")
        if submitted:
            if username == 'abcd' and password == '1234':
                st.session_state.logged_in = True
                st.session_state.usename = username
                st.rerun()
            else:
                st.error("username and password incorrect")

def logout():
        st.session_state.logged_in = False
        st.rerun()

st.sidebar.image("https://i.redd.it/94pwblzk4caf1.jpeg", width=200)
st.sidebar.subheader("""Nicholas😐""")

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

pages = {
    "Daily life": [
        st.Page("page1.py", title="Page 1", icon=":material/home:", default=True),
        st.Page("page2.py", title="Page 2", icon=":material/contact_page:")
    ],
    "favorite food": [
        st.Page("food.py", title="Food", icon=":material/icecream:")
    ],
    "Data Analytics": [
        st.Page("dataframe.py", title="Table", icon=":material/data_thresholding:")
    ],
    "Game": [
        st.Page("game.py", title="Slot Machine", icon=":material/sports_esports:")
    ],
    "Settings": [
        logout_page
    ]
}
if st.session_state.logged_in:
  pg = st.navigation(pages)
else:
  pg = st.navigation([login_page])
pg.run()
