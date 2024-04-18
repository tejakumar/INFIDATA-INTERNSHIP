import streamlit as st
st.header("temperature")
distance=st.number_input('enter the distance:',step=10)
fare=0
if distance<=10:
    fare=80
elif distance<=20:
    fare=80+(6*(distance-10))
elif distance <= 20:
    fare=80+(6*10)+(5(distance-20))
else:
    fare=80+(6*10)+(5*10)+(4(distance-30))
print('the fare to be paid is:',fare)