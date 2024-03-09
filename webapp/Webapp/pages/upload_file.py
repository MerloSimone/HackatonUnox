import streamlit as st
import os
import shutil

# Function to process files  
def get_files(uploaded_files):
    if uploaded_files is not None:
        num = 0
        for file in uploaded_files: 
            # Save file in doc folder
            with open(os.path.join("../../recipes_and_proc", file.name),"wb") as f: 
                f.write(file.getbuffer())
                num += 1
        st.success(f"{num} files have been stored!")


# Create a doc folder if it doesn't exist
if not os.path.exists('../../recipes_and_proc'):
    os.mkdir('../../recipes_and_proc')

st.title("File Uploader")

# Upload widget with drag and drop support
uploaded_files = st.file_uploader("Choose files or drag them here", accept_multiple_files=True) 

# Button to trigger function
if st.button("Send Files"):
    get_files(uploaded_files)
