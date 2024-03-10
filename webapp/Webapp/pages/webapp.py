import streamlit as st

st.set_page_config(page_title="How can UNOX help you?")
st.title("Unox chatbot")


# c1 = st.columns([1])
# with c1:
upload = st.button('Upload file', use_container_width=True) 

col1, col2 = st.columns(2)
with col1:
   prod_button = st.button('Products', use_container_width=True)
with col2:
   recip_button = st.button('Recipes & Procedures', use_container_width=True)

# if start_button:
#    st.write("You clicked the start button!")

if prod_button:
   st.switch_page("pages/product.py") 
   st.session_state.chat_type = "product_exploration"

if recip_button:
   st.switch_page("pages/recipes.py")

if upload:
   st.switch_page("pages/upload_file.py")