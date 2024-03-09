import streamlit as st #all streamlit commands will be available through the "st" alias

st.set_page_config(page_title="Recipes selection") #HTML title
st.title("Recipes selection") #page title


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
custom_recip_butt = left_column.button('Custom recipes', key="Custom recipes")
general_recip_butt = right_column.button('General recipes', key="General recipes")

if custom_recip_butt:
    st.switch_page("pages/custom_recipes.py")
    st.session_state.chat_type = "my_recepes"
if general_recip_butt:
    st.switch_page("pages/general_recipes.py")
    st.session_state.chat_type = "other_recipes"
