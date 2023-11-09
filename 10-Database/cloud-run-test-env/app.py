import streamlit as st
from env import *
import os

st.write("It's working.")
st.write(NAME)
st.write(os.getenv("NAME"))
st.write(os.environ.get("NAME"))
