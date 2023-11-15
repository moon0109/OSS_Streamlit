import streamlit as st

#OSS 중산 시험 결과
OSS_Score = [80, 70, 55, 30, 3, 3, 1, 0]

st.write("# 23114169")
st.write("## 문준우")

OSS_Score


st.area_chart(OSS_Score)