import boto3
import json


def ask_question(user_question, modelId='anthropic.claude-v2', max_tokens_to_sample=2048, temperature=0, top_p=0.5):

    
    predetermined_question = ("You are a customer service agent tasked with classifying emails by type, summarize the content and provide a response for than email. "
                          "These are the categories"
                          "Technical Support including topic as Installation Assistance, Troubleshooting, Warranty Queries; "
                          "Billing and Pricing including topic as Invoice Clarification, Payment Issues, Pricing Information; "
                          "General Inquiry including topic as Company Information, Partnership Opportunities, Feedback and Suggestions; "
                          "Order Status including topic as Order Confirmation, Shipment Tracking, Delivery Issues. "
                          "The response should not include informations about your reasoning be as complete as possible but also writted in a concise way "
                          "Provide your answer in a JSON format reporting a 'Category' field, a 'Summary' a 'Response' field like this:{ \"Category\": \"\", \"Summary\": \"\", \"Response\": \"\" }"
                          "use these informations in the answer: ")
    
    #response_content = gapp.get_rag_response(index=gapp.st.session_state.vector_index, question=gapp.input_text) #call the model through the supporting library
    
    final_question = f"{predetermined_question} {user_question}"
    brt = boto3.client(service_name='bedrock-runtime')

  

    body = json.dumps({
        "prompt": f"\n\nHuman: {final_question}\n\nAssistant:",
        "max_tokens_to_sample": max_tokens_to_sample,
        "temperature": temperature,
        "top_p": top_p,
    })

    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    # text
    return response_body.get('completion')

# Usage
user_input = input("Please enter your question: ")
print(ask_question(user_input))