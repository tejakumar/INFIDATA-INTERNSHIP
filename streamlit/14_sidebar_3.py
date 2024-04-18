import streamlit as st
st.title("Airthmetic operation")
st.markdown("please give the input")
st.sidebar.title("Select the operations")
st.sidebar.markdown("Select the options accordingly:")
choice=st.sidebar.selectbox('Select',('ADD','SUB','MUL','DIV'))
selected_status =st.sidebar.selectbox('Select number', options=['2N','3N'])
if choice =='ADD':
    if selected_status =='2N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       sum=n1+n2
       st.success(sum)
    elif selected_status =='3N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       n3=st.number_input("enter n3:")
       sum=n1+n2+n3
       st.success(sum)
elif choice == 'SUB':
    if selected_status =='2N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       sub=n1-n2
       st.success(sub)
    elif selected_status =='3N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       n3=st.number_input("enter n3:")
       sub=n1-n2-n3
       st.success(sub)
elif choice == 'MUL':
    if selected_status =='2N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       mul=n1*n2
       st.success(mul)
    elif selected_status =='3N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       n3=st.number_input("enter n3:")
       mul=n1*n2*n3
       st.success(mul)
elif choice == 'DIV':
    if selected_status =='2N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       div=n1/n2
       st.success(div)
    elif selected_status =='3N':
       n1=st.number_input("enter n1:")
       n2=st.number_input("enter n2:")
       n3=st.number_input("enter n3:")
       div=n1/n2/n3
       st.success(div)

