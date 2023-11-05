# Simple Streamlit App Docker Python
import streamlit as st
st.subheader("Simple Notepad :notebook:")
st.caption("Add your thoughts here! It will be stored in a database!")
st.subheader("",divider="rainbow")

name = st.text_input("Your Name here")
note = st.text_area("Add Note here")
if st.button("Add a note"):
    st.write(name,":", note)
    st.balloons()
    
st.subheader("",divider="rainbow")
st.write("**Previous Notes**")
