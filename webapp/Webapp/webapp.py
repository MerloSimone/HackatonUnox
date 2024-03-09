import streamlit as st

st.set_page_config(page_title="How can UNOX help you?") 
st.title("How can UNOX help you?")

col1, col2 = st.columns(2)

with col1:
   prod_button = st.button('Products')
with col2:
   recip_button = st.button('Recipes')

if prod_button:
   st.switch_page("pages/product.py")
   st.session_state.chat_type = "product_exploration"
if recip_button:
   st.switch_page("pages/recipes.py")