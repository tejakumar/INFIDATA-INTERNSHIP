import streamlit as st
if 'clicked' not in st.session_state:
    st.session_state.clicked=False
def click_button():
    st.session_state.clicked=True
    st.write('button clicked!')
st.button('click me', on_click=click_button)
if st.session_state.clicked:
    st.title('hello user....!')
    st.slider('select a value')
    st.info("demo")
