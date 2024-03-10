import streamlit as st #all streamlit commands will be available through the "st" alias
import os
from time import sleep
import webbrowser as wb

st.set_page_config(page_title="Recipes & Procedures") #HTML title
st.title("Recipes & Procedures") #page title
st.markdown("You can explore your procedures or discover new recipes ")

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
with left_column:
    custom_recip_butt = left_column.button('Your Procedures & Recipes')
with right_column:
    general_recip_butt = right_column.button('General recipes')

if custom_recip_butt: # and esiste l'indice con i file caricati
    folder_path = '../../user_product_index'
    if os.path.exists(folder_path):
        st.switch_page("pages/custom_recipes.py")
    else:
        st.error("You have not uploaded any file yet")
        with st.spinner("Redirecting"):
            sleep(2)
            wb.open_new_tab("http://localhost:8501/upload_file")
            st.switch_page("pages/webapp.py")


if general_recip_butt: # and esiste l'indice 
    st.switch_page("pages/general_recipes.py")
