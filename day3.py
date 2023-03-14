import streamlit as st 
# create button 
st.header("Button")
if st.button("Say Hello"): 
    st.write("Hello, Mr. World")
else: 
    st.write("Good bye, ya")