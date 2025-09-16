import streamlit as st
import random

if 'c_num' not in st.session_state:
    st.session_state['c_num'] = random.randint(1,100)
c_num = st.session_state.c_num
# 숫자 1~100 사이
h_num = st.number_input('숫자 입력', 1, 100)
st.write('입력한 숫자', h_num)

if st.button('결과 확인'):
    if c_num > h_num:
        st.write('업')
    elif c_num < h_num:
        st.write('다운')
    else:
        st.write('정답')
        st.balloons()