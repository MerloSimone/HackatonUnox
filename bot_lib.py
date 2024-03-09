import os
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationalRetrievalChain

from langchain.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

from models import llm_model

import streamlit as st #all streamlit commands will be available through the "st" alias

def get_llm():

	if 'chat_type' not in st.session_state:
		print('not defined')
	else:
		if st.session_state.chat_type == 'product_exploration':
			print('ok')
		elif st.session_state.chat_type == 'my_recipes':
			print('ok')
		elif st.session_state.chat_type == 'other_recipes':
			print('ok')
		elif st.session_state.chat_type == 'add_recipes':
			print('ok')
		elif st.session_state.chat_type == 'email':
			return llm_model(maxTokens=2048,temperature=0.5,topP=0.5).get_model()
		else:
			print('ok')


	return llm_model(maxTokens=1024,temperature=0.2,topP=0.5).get_model()
""" 
    model_kwargs =  { #AI21
        "maxTokens": 1024, 
        "temperature": 0.2, 
        "topP": 0.5, 
        "stopSequences": ["Human:"], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    
    llm = Bedrock(
        credentials_profile_name="default", #sets the profile name to use for AWS credentials (if not the default)
        region_name="us-east-1", #sets the region name (if not the default)
        #endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="ai21.j2-ultra-v1", #set the foundation model
        model_kwargs=model_kwargs) #configure the properties for Claude

    return llm
"""




def get_index(): #creates and returns an in-memory vector store to be used in the application
    
    
    embeddings = BedrockEmbeddings(
        credentials_profile_name="default", #sets the profile name to use for AWS credentials (if not the default)
        region_name="us-east-1", #sets the region name (if not the default)
        #endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
    ) #create a Titan Embeddings client
    
    """
    #base_path=""

    #pdf_files_paths = [base_path+f for f in os.listdir() if (os.path.isfile(f) and f.endswith("pdf"))]

    pdf_path = "XAVC-0511-EPRM-SPC_en_08-2023.pdf" #assumes local PDF file with this name

    #loaders=[]
    #for(file_path in pdf_files_path):
    #	loader.append(PyPDFLoader(file_path=file_path))

    loader = PyPDFLoader(file_path=pdf_path) #load the pdf file
    
    text_splitter = RecursiveCharacterTextSplitter( #create a text splitter
        separators=["\n\n", "\n", ".", " "], #split chunks at (1) paragraph, (2) line, (3) sentence, or (4) word, in that order
        chunk_size=1000, #divide into 1000-character chunks using the separators above
        chunk_overlap=100 #number of characters that can overlap with previous chunk
    )
    
    index_creator = VectorstoreIndexCreator( #create a vector store factory
        vectorstore_cls=FAISS, #use an in-memory vector store for demo purposes
        embedding=embeddings, #use Titan embeddings
        text_splitter=text_splitter, #use the recursive text splitter
    )
    

    #index_from_loader = index_creator.from_loaders(loaders) 

    index_from_loader = index_creator.from_loaders([loader]) #create an vector store index from the loaded PDF
    
    #return index_from_loader #return the index to be cached by the client app
    """
    return FAISS.load_local("new_index",embeddings)


def get_memory(): #create memory for this chat session
    
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True) #Maintains a history of previous messages
    
    return memory
    
def get_rag_chat_response(input_text, memory, index): #chat client function
    
    llm = get_llm() 
    
    #conversation_with_retrieval = ConversationalRetrievalChain.from_llm(llm, index.vectorstore.as_retriever(), memory=memory)
    conversation_with_retrieval = ConversationalRetrievalChain.from_llm(llm, index.as_retriever(), memory=memory)
    
    chat_response = conversation_with_retrieval({"question": input_text}) #pass the user message, history, and knowledge to the model
    
    return chat_response['answer']

def get_rag_mail_response(input_text, index): #chat client function
    
    llm = get_llm()
    st.session_state.memory=get_memory()
    st.session_state.chat_history = []
    st.session_state.chat_history.append({"role":"user", "text":input_text})
	
    conversation_with_retrieval = ConversationalRetrievalChain.from_llm(llm, index.as_retriever(), memory=st.session_state.memory)
    
    chat_response = conversation_with_retrieval({"question": input_text})
    
    return chat_response['answer']





