# Terminal -> streamlit run file name.py

import streamlit as st

st.title('Calculator')
st.markdown('welcome to my first streamlit app')

c1, c2 = st.columns(2)
fnum = c1.number_input('enter first number', value= 0)
snum = c2.number_input('enter second number', value= 0)

options= ['Add','subtract','multiply','divide']
choice = st.radio('select operation', options)

button= st.button('calculate')

if button:
    if choice =='Add':
        result= fnum + snum
    if choice == 'subtract':
        result= fnum - snum
    if choice == 'multiply':
        result= fnum * snum
    if choice == 'divide':
        result= fnum / snum

    st.success(f'the result is {result}')

    



