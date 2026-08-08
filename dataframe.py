import streamlit as st

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30 ,40],\
})

df

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns= ('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

#import streamlit as st

#product_data = {
    #"Product": [
        #":material/devices: Widget Pro",
        #":material/smart_toy: Smart Device",
        #":material/inventory: Premium Kit",
    #],
    #"Category": [
        #":blue[Electronics]",
        #":green[IoT]",
        #":violet[Bundle]",
    #],
    #"Stock": [
        #"🟢 Full",
        #"🟡 Low",
        #"🔴 Empty",
    #],
    #"Units sold":,
    #"Revenue":,
#}

#st.table(product_data, border="horizontal")

#chart_data = pd.DataFrame(
   # np.random.randn(20, 1)
    #columns = ['a', 'b', 'c', 'd']
#)

#st.line_chart(chart_data)

#map_data = pd.DataFrame(
    #np.random.randn(1000, 2) / [50, 50] + [30.4508, 91.1545],
    #columns = ['lat', 'lon']
#)

#st.map(map_data)

#[37.76, -122.4] san fransisco

#x = st.slider('x')
#st.write(x, 'cubed is', x ** 3)

import streamlit as st

st.text_input("Your name", key="name")
st.text_input("Your city", key="city")
st.session_state.name
st.session_state.city

import streamlit as st
import pandas as pd
import numpy as np

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['Col1', 'Col2', 'Col3']
    )

    chart_data

    df = pd.DataFrame({
        'first column': [1,2,3,4],
        'second column' : [10,20,30,40]
    })

    option = st.selectbox(
        'Which number do you like the best?',
        df['first column']
    )

    'You selected: ', option



    
    df = pd.DataFrame({
        'first column': [1,2,3,4,5,6,7,8,9,10,11,12],
    })

    option = st.selectbox(
        'What grade are you currently in, or is going to be in?',
        df['first column']
    )

    'My grade is:', option



    
    
    df = pd.DataFrame({
        'first column': ['dog', 'cat', 'fish', 'hamster', 'rabbit', 'turtle', 'bird', 'snake', 'lizard', 'frog'],
    })

    option = st.selectbox(
        'What is your favorite pet in these options?',
        df['first column']
    )

    'My favorite pet out of these options is:', option



    left_column, right_column = st.columns(2)
    left_column.button('Press me!')

    with right_column:
        option = st.radio(
            'Choosing colors',
            ("red", "yellow", "green", "blue")
        )

        st.write(f"You have chosen {option} color!")


        import time

        'Starting a lon computation...'

        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

    '...and now we\'re done!'





