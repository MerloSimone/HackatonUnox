import streamlit as st #all streamlit commands will be available through the "st" alias
import pandas as pd
import numpy as np


st.set_page_config(page_title="POOR6", layout="wide")  #set the page width wider to accommodate columns

st.title("POOR6")  #page title

st.markdown("markdown")

st.header("header")

st.subheader("subheader")

st.caption("caption")

st.code("code")

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()


df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')

st.divider()    
    
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.divider()    
    

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")
    
st.divider()       


st.divider()

with st.container():
    col1, col2, col3 = st.columns(3)
    col11, col22 = st.columns(2)
    
    with col1:
        st.write("col1")
    
    with col2:
        st.write("col2")
        
    with col3:
        st.write("col3")
        
    with col11:
        st.write("col11")
        
    with col22:
        st.write("col22")
        
        
st.divider()

st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
