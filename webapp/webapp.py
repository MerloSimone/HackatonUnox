import streamlit as st #all streamlit commands will be available through the "st" alias

st.set_page_config(page_title="Streamlit Demo") #HTML title
st.title("Streamlit Demo") #page title


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
bottone_uno = left_column.button('Products', key="Products")
bottone_due = right_column.button('Recipes', key="Recipes")

if bottone_uno:
    st.switch_page("pages/vag1.py")
if bottone_due:
    st.switch_page("pages/vag2.py")
