import streamlit as st
st.sidebar.title("Reg form")
with st.form(key='form1'):
    with st.sidebar:
        user_word = st.sidebar.text_input("enter a keyword","hello")
        select_language=st.sidebar.radio("Tweet language",  ('All','English','hindi'))
        include_retweets=st.sidebar.checkbox('Include retweets in data')
        num_of_tweets=st.sidebar.number_input('maximum number of tweets',100)
        submitted1=st.form_submit_button(label=' Search Twitter')

