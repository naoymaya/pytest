import streamlit as st
import pandas as pd

st.title('My first app')

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     })

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)
st.write('You selected: ', option)
