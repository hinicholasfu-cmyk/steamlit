import random
import streamlit as st
from streamlit_extras.let_it_rain import rain
import time


symbols = ['☹️', '🙁', '😐', '🙂', '😃']


st.markdown("""
<h1 style="color :white">Welcome to my gambler's paradise slot machine game!🎰</h1>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNYEuyKl8i1BRUEO_83Js9LXoMpjn2OrtGvGMpE31avg&s=10");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid='stAudio']{
      display: none;
   }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-suqvXMQ-f3HzGcfBx5OJ2wabNdwTYoP1HMimHtvw8g&s=10")
st.write("Press the button to spin")

st.divider()

if "coin" not in st.session_state:
    st.session_state['coin'] = 0

if 'score' not in st.session_state:
    st.session_state['score'] = 0



def showSymbol (box, symbol):
    box.markdown(
        f'<p style="font-size: 100px; text-align: center; margin: 0;">{symbol}</p>', unsafe_allow_html=True
    )

def showCornerGif(url, duration=5):
    placeholder = st.empty()
    placeholder.markdown(
        f'<p style="position: fixed; bottom:0; left:0;"><img src={url} width=300></img></p>', unsafe_allow_html=True
    )
    time.sleep(duration)
    placeholder.empty()
if st.button("Press to spin 🎰"):
    spin_sound = st.empty()
    spin_sound.audio("mixkit-final-level-bonus-2061.wav", autoplay=True)
    col1, col2, col3 = st.columns(3)
    box1 = col1.empty()
    box2 = col2.empty()
    box3 = col3.empty()

    for i in range(15):
       #showSymbol(box1, random.choice(symbols))
       #showSymbol(box2, random.choice(symbols))
       #showSymbol(box3, random.choice(symbols))
       showSymbol(box1, random.choice(symbols))
       showSymbol(box2, random.choice(symbols)) 
       showSymbol(box3, random.choice(symbols))
       time.sleep(0.2)


    s1 = random.choice(symbols)
    s2 = random.choice(symbols)
    s3 = random.choice(symbols)

    #box1.header(s1)
    #box2.header(s2)
    #box3.header(s3)
    showSymbol(box1, s1)
    showSymbol(box2, s2)
    showSymbol(box3, s3)

    clapping_sound = st.empty()

    if s1 == s2 == s3:
        clapping_sound.audio("mixkit-ending-show-audience-clapping-478.wav", autoplay=True)
        st.success("╰(*°▽°*)╯ Congrats! you win! Jackpot! you have 3 matching symbols!")
        st.audio("mixkit-clinking-coins-1993.wav", autoplay=True)
        st.session_state.score += 100
        st.session_state.coin += 50
        showCornerGif('https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyZTE1MmdxbDB1d2gzeHBhMGphdmZ4c29vcnIwdWdmY3RuN2w0ZzAxcCZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/S00sIdupYky9PDbkaJ/200w.gif')
        rain(
            emoji=s1,
            font_size=100,
            falling_speed=5,
            animation_length=1
        )
    elif s1 == s2 or s1 == s3 or s2 == s3:
        if s1 == s2 or s1 == s3:
            em = s1
        elif s2 == s3:
            em = s2

        st.audio("mixkit-clinking-coins-1993.wav", autoplay=True)
        clapping_sound.audio("mixkit-ending-show-audience-clapping-478.wav", autoplay=True)
        st.success(" 2 matched! Awesome!")
        st.session_state.score += 10
        st.session_state.coin += 10
        showCornerGif('https://i.pinimg.com/originals/78/78/a2/7878a20aaed4de2b44a8b61fc38e9a36.gif')
        rain(
            emoji=em,
            font_size=100,
            falling_speed=5,
            animation_length=1
        )
        clapping_sound.empty()
    else:
        st.info("So close! Try again please!")

st.markdown(f"** Your score: {st.session_state.score}", unsafe_allow_html=True)
st.markdown(f"💰 Your coin: {st.session_state.coin}", unsafe_allow_html=True)
#st.write(f'Your coin: {st.session_state.coin}')
