import os
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationalRetrievalChain

from langchain.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

import streamlit as st #all streamlit commands will be available through the "st" alias


class llm_model(object):

    def __init__(self,maxTokens=1024,temperature=0,topP=0.5):
        self.maxTokens=maxTokens
        self.temperature=temperature
        self.topP=topP

        self.model_kwargs =  { #AI21
            "maxTokens": maxTokens, 
            "temperature": temperature, 
            "topP": topP, 
            "stopSequences": ["Human:"], 
            "countPenalty": {"scale": 0 }, 
            "presencePenalty": {"scale": 0 }, 
            "frequencyPenalty": {"scale": 0 } 
        }
    
        self.llm = Bedrock( credentials_profile_name="default", #sets the profile name to use for AWS credentials (if not the default)
            region_name="us-east-1", #sets the region name (if not the default)
            #endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
            model_id="ai21.j2-ultra-v1", #set the foundation model
            model_kwargs=self.model_kwargs) #configure the properties for Claude


    def get_model(self):
        return self.llm

    def get_kwargs(self):
        return self.model_kwargs



