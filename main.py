import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("st.write")

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

st.write({
    "somekey": 123
})

st.write([
    'abc',
    123,
    {
        "some": [ 1, 2, 3],
        "other": {
            "a": 3,
            "b": "c"
        }
    }
]
)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
st.write(f'Below is a DataFrame: {df} Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 4),
     columns=['vx', 'vy', 'dc', 'ds']
)
c = alt.Chart(df2)\
    .mark_circle()\
    .encode(
        x='vx', 
        y='vy', 
        size='ds', 
        color='dc', 
        tooltip=['vx', 'vy']
    )
st.write(c)