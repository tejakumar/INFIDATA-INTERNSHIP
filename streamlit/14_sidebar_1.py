import streamlit as st
add_selectbox = st.sidebar.selectbox(
    "how would you like to be contacted?",
    ("email","home phone","mobile phone")
)

with st.sidebar:
    add_radio = st.radio(
        "choose a shipping method",
        ("standard (5-15 days)", "Express  (2-5 days)")
    )