import streamlit as st #all streamlit commands will be available through the "st" alias

st.set_page_config(page_title="How can UNOX help you?") #HTML title
st.title("How can UNOX help you?") #page title


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
prod_button = left_column.button('Products', key="Products")
recip_button = right_column.button('Recipes', key="Recipes")

if prod_button:
    st.switch_page("pages/product.py")
    st.session_state.chat_type = "product_exploration"
if recip_button:
    st.switch_page("pages/recipes.py")
