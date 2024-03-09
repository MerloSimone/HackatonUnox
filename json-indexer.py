import os
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationalRetrievalChain

from langchain.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import JSONLoader, PyPDFLoader

from models import llm_model

from pathlib import Path

import streamlit as st #all streamlit commands will be available through the "st" alias



def flatten_json(json_obj, prefix=''):
    flattened = {}
    for key, value in json_obj.items():
        new_key = prefix + key
        if isinstance(value, dict):
            flattened.update(flatten_json(value, new_key + '_'))
        else:
            flattened[new_key] = value
    return flattened
def metadata_func(record: dict, metadata: dict) -> dict:
    # flatten the record
    flatten = flatten_json(record)

    # iterate over the record and add the metadata
    for key, value in flatten.items():
        if key == "imgUrl":
            continue
        metadata[key] = value
    return metadata

def get_json_splits(json_file):
    """Function takes in the pdf data and returns the
    splits so for further processing can be done."""

    loader = JSONLoader(json_file, jq_schema=".", content_key="title", metadata_func=metadata_func)
    return loader.load()


def get_pdf_splits(pdf_file):
    """Function takes in the pdf data and returns the
    splits so for further processing can be done."""

def get_pdf_splits(pdf_file):
    """Function takes in the pdf data and returns the
    splits so for further processing can be done."""

    loader = PyPDFLoader(pdf_file)
    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter( #create a text splitter
        separators=["\n\n", "\n", ".", " "], #split chunks at (1) paragraph, (2) line, (3) sentence, or (4) word, in that order
        chunk_size=1000, #divide into 1000-character chunks using the separators above
        chunk_overlap=100 #number of characters that can overlap with previous chunk
    )

    doc_list = []
    #Pages will be list of pages, so need to modify the loop
    for pg in pages:
        pg_splits = text_splitter.split_text(pg.page_content)
        doc_list.extend(pg_splits)

    return doc_list


def embed_index(doc_list, embed_fn, index_store):
    """Function takes in existing vector_store,
    new doc_list and embedding function that is
    initialized on appropriate model. Local or online.
    New embedding is merged with the existing index. If no
    index given a new one is created"""
    #check whether the doc_list is documents, or text
    faiss_db = FAISS.from_documents(doc_list, embed_fn)


    if os.path.exists(index_store):
        local_db = FAISS.load_local(index_store,embed_fn)
        #merging the new embedding with the existing index store
        local_db.merge_from(faiss_db)
        print("Merge completed")
        local_db.save_local(index_store)
        print("Updated index saved")
    else:
        faiss_db.save_local(folder_path=index_store)
        print("New store created...")







doc_folder="./data/recipe/"
file_list=[]



def list_directory_tree_with_pathlib(starting_directory, file_type="pdf"):
    path_object = Path(starting_directory)
    for file_path in path_object.rglob('*'):
        if file_path.is_file():
            file_path_str=file_path.as_posix()
            if file_path_str.endswith(file_type):
                print(file_path_str)
                file_list.append(file_path_str)


embeddings = BedrockEmbeddings(
    credentials_profile_name="default", #sets the profile name to use for AWS credentials (if not the default)
    region_name="us-east-1", #sets the region name (if not the default)
    #endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
) #create a Titan Embeddings client



pdf_path = "XAVC-0511-EPRM-SPC_en_08-2023.pdf" #assumes local PDF file with this name
list_directory_tree_with_pathlib(doc_folder, "json")
i=0
for elem in file_list:
    print(i)
    i=i+1
    documento = get_json_splits(elem)
    # documento = get_pdf_splits(elem)
    embed_index(
        doc_list=documento,
        embed_fn=embeddings,
        index_store='pdf_json_recipe_new_index'
    )

print("---------------")