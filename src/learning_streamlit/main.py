import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

number = st.slider("Pick a number", 0, 100)

print(number)

st.write(f"You picked {number}")