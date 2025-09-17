# 1~100 사이의 데이터 
import random
datas = [random.randint(1,100) for i in range(10)]

import streamlit as st
st.bar_chart(datas)
st.line_chart(datas)
st.area_chart(datas)
st.columns(2)