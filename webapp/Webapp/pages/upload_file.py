import streamlit as st
import os
import shutil
import os
from langchain.embeddings import BedrockEmbeddings

# import sys
# sys.path.append('../')
from user_indexer import get_pdf_splits, embed_index


embeddings = BedrockEmbeddings(
        credentials_profile_name="default", #sets the profile name to use for AWS credentials (if not the default)
        region_name="us-east-1", #sets the region name (if not the default)
        #endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
    ) #create a Titan Embeddings client



# Function to process files  
def get_files(uploaded_files):
    docs_paths = []
    if uploaded_files is not None:
        num = 0
        for file in uploaded_files: 
            # Save file in doc folder
            with open(os.path.join("../../recipes_and_proc", file.name),"wb") as f: 
                f.write(file.getbuffer())
                num += 1
                doc_path = str(os.path.join("../../recipes_and_proc/")) + str(file.name)
                print(f"The document path is: {doc_path}")
                docs_paths.append(doc_path)
                # mi prendo il path del file
        st.success(f"{num} files have been stored! Wait until all the files will be processed..")

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        i = 0 
        for doc_path in docs_paths:
            i += 1
            # Update the progress bar with each iteration.
            bar.progress((len(doc_path)/i)/100)
            documento = get_pdf_splits(doc_path)
            embed_index(doc_list=documento, embed_fn=embeddings, index_store='../../user_product_index')

        bar.progress(100)
        st.success(f"All files have been processed!")
        # faccio l'index di tutti i file uploadati


# Create a doc folder if it doesn't exist
if not os.path.exists('../../recipes_and_proc'):
    os.mkdir('../../recipes_and_proc')

st.title("File Uploader")

# Upload widget with drag and drop support
uploaded_files = st.file_uploader("Choose files or drag them here", accept_multiple_files=True) 

col1, col2 = st.columns(2)

with col1: 
    send_button = st.button("Send Files", use_container_width=True)
with col2:
    ret_button = st.button("Return", use_container_width=True)

# Button to trigger function
if send_button:
    get_files(uploaded_files)

if ret_button:
    st.switch_page("pages/webapp.py")
    


