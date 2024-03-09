import streamlit as st
import json

st.write("""
# My Web App
""")

col1, col2 = st.columns(2)

send_data = ""
structure_data = ""

with col1:
    text1 = st.text_area('Text Area 1', height=200)

    btn1 = st.button('Structure Data', on_click=structure_data, args=(text1,))

with col2:
    text2 = st.text_area('Text Area 2', height=200)

    btn2 = st.button('Send Data', on_click=send_data, args=(text2,))


def structure_data(input):
    # Function to structure data
    data = json.loads(input) 
    return data

def send_data(input):
    # Function to send data
    st.write('Sending:', input)