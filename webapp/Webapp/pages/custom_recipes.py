import streamlit as st #all streamlit commands will be available through the "st" alias


import sys
sys.path.append('../../')
# Use absolute import for bot_lib
import bot_lib as glib
st.session_state.chat_type = "my_recipes"



st.set_page_config(page_title="Custom recipes and procedures") #HTML title
st.title("Your custom recipes and procedures") #page title

col1, col2 = st.columns(2)
with col1:
    return_button = st.button("Home")
with col2:
    reset_button = st.button("Reset")

if reset_button:
    st.session_state.chat_history = []
    st.session_state.memory = glib.get_memory() #initialize the memory

if return_button:
    st.switch_page("pages/webapp.py")


st.text("Your custom recipes and procedures")

if 'memory' not in st.session_state: #see if the memory hasn't been created yet
    st.session_state.memory = glib.get_memory() #initialize the memory


if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
    st.session_state.chat_history = [] #initialize the chat history

if 'vector_index' not in st.session_state: #see if the vector index hasn't been created yet
    with st.spinner("Indexing document..."): #show a spinner while the code in this with block runs
        st.session_state.vector_index = glib.get_index("../../user_product_index") #retrieve the index through the supporting library and store in the app's session cache




#Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
for message in st.session_state.chat_history: #loop through the chat history
    with st.chat_message(message["role"]): #renders a chat line for the given role, containing everything in the with block
        st.markdown(message["text"]) #display the chat content



input_text = st.chat_input("Chat with your bot here") #display a chat input box

if input_text: #run the code in this if block after the user submits a chat message
    
    with st.chat_message("user"): #display a user chat message
        st.markdown(input_text) #renders the user's latest message
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) #append the user's latest message to the chat history
    
    chat_response = glib.get_rag_chat_response(input_text=input_text, memory=st.session_state.memory, index=st.session_state.vector_index,) #call the model through the supporting library
    
    with st.chat_message("assistant"): #display a bot chat message
        st.markdown(chat_response) #display bot's latest response
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) #append the bot's latest message to the chat history
    
