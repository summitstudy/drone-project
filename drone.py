import streamlit as st
from djitellopy import Tello
import time 
import random
st.image('screen.png', caption='', use_column_width=True)

comList = ['오른쪽으로 회전', '왼쪽으로 회전', '왼쪽으로 이동', '오른쪽으로 이동', '전진','후진']

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value

st.markdown("""
<style>
    .stButton>button {
        color: black;
        background-color: #F0F2F6;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# 버튼 생성
if st.button('삽입', on_click=increment_counter, kwargs=dict(increment_value=1)):
    # 버튼이 눌렸을 때 실행될 코드
    pass

if st.button('삭제', on_click=decrement_counter, kwargs=dict(decrement_value=1)):
    # 버튼이 눌렸을 때 실행될 코드
    pass

with st.form('코딩'):
    finalCom = []
    for i in range(st.session_state.count):
        comListItem = st.selectbox(f'✨{i+1}번째 동작', comList, key=f'comlist{i+1}')
        comVal = st.number_input('거리 혹은 각도', min_value=20, max_value=500, step=10, key=f'valinput{i}')
        finalCom.append([comListItem, comVal])

    if st.form_submit_button('드론실행'):
        st.write(finalCom)
        tello = Tello()
        tello.connect()
        tello.takeoff()
        for comItem, val in finalCom:
            val = int(val)
            if comItem == comList[0]:
                tello.rotate_clockwise(val)
            elif comItem == comList[1]:
                tello.rotate_counter_clockwise(val)
            elif comItem == comList[2]:
                tello.move_left(val)
            elif comItem == comList[3]:
                tello.move_right(val)
            elif comItem == comList[4]:
                tello.move_forward(val)
            elif comItem == comList[5]:
                tello.move_back(val)     

        tello.land()     

