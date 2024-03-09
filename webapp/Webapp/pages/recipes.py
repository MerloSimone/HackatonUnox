import streamlit as st #all streamlit commands will be available through the "st" alias
import os
from time import sleep

st.set_page_config(page_title="Recipes selection") #HTML title
st.title("Recipes selection") #page title


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
with left_column:
    custom_recip_butt = left_column.button('Custom recipes')
with right_column:
    general_recip_butt = right_column.button('General recipes')

if custom_recip_butt: # and esiste l'indice con i file caricati
    folder_path = '../../user_product_index'
    if os.listdir(folder_path):
        st.switch_page("pages/custom_recipes.py")
        st.session_state.chat_type = "my_recipes"
    else:
        st.error("You have not uploaded any file yet")
        with st.spinner("Redirecting"):
            sleep(2)
            st.switch_page("pages/upload_file.py")


if general_recip_butt: # and esiste l'indice 
    st.switch_page("pages/general_recipes.py")
    st.session_state.chat_type = "other_recipes"
