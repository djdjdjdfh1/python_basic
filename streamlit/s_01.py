import streamlit as st
st.title('hello world!')
st.header('header')
st.subheader('subheader')
st.button('button')
st.checkbox('checkbox')
st.selectbox('selectbox', ('option1', 'option2'))
st.slider('slider', 0, 100, 50) # min max default

name = st.text_input('이름을 입력하세요')
st.write(f'Hello {name}!')