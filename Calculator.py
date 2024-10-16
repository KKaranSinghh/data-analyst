# Terminal -> streamlit run file name

import streamlit as st

st.title('Calculator')
st.markdown('welcome to my first streamlit app')

c1, c2 = st.columns(2)
fnum = c1.number_input('enter first number', value= 0)
snum = c2.number_input('enter second number', value= 0)

options= ['Add','subtract','multiply','divide']
choice = st.radio('select operation', options)
