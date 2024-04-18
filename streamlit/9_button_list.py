import streamlit as st
animal_shelter=['cat','dog','rabbit','bird']
animal=st.text_input('type an animal')
if st.button('Check availability'):
    have_it=animal.lower() in animal_shelter
    if(have_it):
       st.write("we has this animal")
    else:
       st.write("we dont have this animal")