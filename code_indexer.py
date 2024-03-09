import os
import requests

from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredHTMLLoader

from pathlib import Path

# response = requests.get("https://d3bnjxknjlugy9.cloudfront.net/")
# with open("data/documents.html", "w") as f:
#     f.write(response.text)


def get_html():
    """Function takes in the pdf data and returns the
    splits so for further processing can be done."""

    loader = UnstructuredHTMLLoader("data/documents.html")
    return loader.load()

def embed_index(doc_list, embed_fn, index_store):
    # check whether the doc_list is documents, or text
    faiss_db = FAISS.from_documents(doc_list, embed_fn)

    if os.path.exists(index_store):
        local_db = FAISS.load_local(index_store, embed_fn)
        local_db.merge_from(faiss_db)
        print("Merge completed")
        local_db.save_local(index_store)
        print("Updated index saved")
    else:
        faiss_db.save_local(folder_path=index_store)
        print("New store created...")


embeddings = BedrockEmbeddings(
    credentials_profile_name="default",  # sets the profile name to use for AWS credentials (if not the default)
    region_name="us-east-1",  # sets the region name (if not the default)
    # model_id="meta.llama2-70b-chat-v1",  # set the foundation model
    # endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
)  # create a Titan Embeddings client

document = get_html()

embed_index(
    doc_list=document,
    embed_fn=embeddings,
    index_store='code_new_index'
)

print("---------------")


# input_text = """Instruction: Create a single recipe request body in JSON format. Ensure the JSON follows the structure of a recipe based on the Description of each field.
#     The recipe is:""" + input_text

# llm_model(maxTokens=2048,temperature=0.1, topP=0.3).get_model()