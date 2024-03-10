import streamlit as st
import bot_lib as glib
import requests
import json

st.set_page_config(page_title="Text to JSON")
st.title("Text to Recipe")

rcol, lcol = st.columns([0.5, 0.5])
    
if 'vector_index' not in st.session_state: #see if the vector index hasn't been created yet
    with st.spinner("Indexing document..."): #show a spinner while the code in this with block runs
        st.session_state.vector_index = glib.get_index("./code_new_index") #retrieve the index through the supporting library and store in the app's session cache

if 'memory' not in st.session_state: #see if the memory hasn't been created yet
    st.session_state.memory = glib.get_memory() #initialize the memory


with rcol:
   txt_text = st.text_area(
    "Insert here the recipe text",
    """Recipe title: LASAGNE

Ingredients
1 tbsp olive oil
1 onion, diced
1 carrot, diced
1 celery stalk, diced
2 garlic cloves, finely sliced
250g beef mince
250g pork mince
1 tbsp tomato purée
400g tin chopped tomatoes
200ml beef stock
200ml red wine
1 tsp Worcestershire sauce
9-12 lasagne sheets (depending on the size of your baking dish)
50g Parmesan, grated
150g pack mozzarella, shredded
50g butter
50g plain flour
550ml semi-skimmed milk


Method
In a large pan, heat the olive oil over a low heat. Fry the onion, carrot, celery and garlic for 5 mins, or until softened. Add the mince and fry on a medium heat until golden. Turn up the heat, pour in the wine and bubble until reduced. Stir in the tomato purée, chopped tomatoes and stock. Add in the Worcestershire sauce and simmer for 15 mins, or until the liquid has reduced. Season.
Meanwhile, make the white sauce. Melt the butter in a small saucepan over a low heat and add the flour. Whisk until combined and cook on low for 1-2 mins. Remove from the heat and gradually whisk in the milk until you have a loose sauce. Season. Return to a gentle heat and whisk constantly until the sauce thickens.
Preheat the oven to gas 6, 200°C, fan 180°C. Layer up the lasagne in a baking dish, starting with a third each of the ragu, then the pasta, then the white sauce. Repeat twice. Top with the Parmesan and mozzarella then bake in the oven for 40-45 mins, until piping hot and crisp and bubbling on top. Serve immediately.""",height = 350
    )

with lcol:
   query = """Please produce the JSON version of the recipe provided below. Use known tree structure to be filled only with information from the below text. Text:""" + txt_text
   #response = glib.get_rag_chat_response(question=query, memory=st.session_state.memory, index=st.session_state.vector_index,) #call the model through the supporting library
   response = glib.get_rag_chat_response(input_text=query, memory=glib.get_memory(), index=st.session_state.vector_index,) #call the model through the supporting library
   txt_json = st.text_area("Here will be the JSON version",response,height = 350)
   scol, dcol = st.columns([0.5, 0.5])
   if scol.button("submit"):
      httpresp = requests.post("https://apiv2.datadrivencooking.com/v1/company/recipes",headers={"authorization":"APIKey unox_ddc_demo"},json=json.loads(txt_json))
      if httpresp.status_code == 200:
         st.text("OK!")
      else:
         st.text(str(httpresp.status_code) + ": " + str(httpresp.content))
   dcol.download_button(
      label="Download JSON",
      data=response,
      file_name='recipe_json.csv',
      mime='application/json',
   )
