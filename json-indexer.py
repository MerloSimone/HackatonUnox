import os

from pathlib import Path
from langchain.vectorstores import FAISS
from langchain.embeddings import BedrockEmbeddings
from langchain.document_loaders import JSONLoader


def get_json_splits(json_file):
    """Function takes in the pdf data and returns the
    splits so for further processing can be done."""

    loader = JSONLoader(json_file, jq_schema=".", text_content=False)
    return loader.load()


def embed_index(doc_list, embed_fn, index_store):
    """Function takes in existing vector_store,
    new doc_list and embedding function that is
    initialized on appropriate model. Local or online.
    New embedding is merged with the existing index. If no
    index given a new one is created"""
    # check whether the doc_list is documents, or text
    faiss_db = FAISS.from_texts(doc_list, embed_fn)

    if os.path.exists(index_store):
        local_db = FAISS.load_local(index_store, embed_fn)
        # merging the new embedding with the existing index store
        local_db.merge_from(faiss_db)
        print("Merge completed")
        local_db.save_local(index_store)
        print("Updated index saved")
    else:
        faiss_db.save_local(folder_path=index_store)
        print("New store created...")


doc_folder = "./data/recipe/"
file_list = []


def list_directory_tree_with_pathlib(starting_directory):
    path_object = Path(starting_directory)
    for file_path in path_object.rglob('*'):
        if file_path.is_file():
            print(file_path)
            file_path_str = file_path.as_posix()
            if file_path_str.endswith("json"):
                file_list.append(file_path_str)


embeddings = BedrockEmbeddings(
    credentials_profile_name="default",  # sets the profile name to use for AWS credentials (if not the default)
    region_name="us-east-1",  # sets the region name (if not the default)
    # endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
)  # create a Titan Embeddings client

pdf_path = "XAVC-0511-EPRM-SPC_en_08-2023.pdf"  # assumes local PDF file with this name
list_directory_tree_with_pathlib(doc_folder)
i = 0
for elem in file_list:
    print(i)
    i = i + 1
    documents = get_json_splits(elem)
    print(documents)

    # embed_index(
    #     doc_list=documents,
    #     embed_fn=embeddings,
    #     index_store='recipes_index'
    # )

print("---------------")
