import streamlit as st
import time
import webbrowser as wb
st.title('Dang Nhap')
username = st.text_input('Username', '')
password = st.text_input('Password', '')

if st.button('Dang nhap'):
  if username == '86565' and password == '123123':
    st.success('Dang nhap thanh cong')
    time.sleep(3)
    wb.open('http://mevabeuit.com')
  else:
    st.error('Sai Username hoac Password')