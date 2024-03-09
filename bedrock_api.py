import os
import json
import boto3

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def text_to_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    textobject = c.beginText()
    textobject.setTextOrigin(50, 750)  # Adjust position as needed
    textobject.setFont("Helvetica", 12)  # Adjust font and size as needed
    lines = text.split('\n')
    for line in lines:
        textobject.textLine(line)
    c.drawText(textobject)
    c.save()

session = boto3.Session(
    profile_name="default"
)  # sets the profile name to use for AWS credentials

bedrock = session.client(
    service_name='bedrock-runtime',  # creates a Bedrock client
    region_name="us-east-1",
    # endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
)

#
bedrock_model_id = "ai21.j2-mid-v1"  # set the foundation model
# read all the json files in the directory
doc_folder = "./data/recipe/"
file_list = []

for root, dirs, files in os.walk(doc_folder):
    for file in files:
        if file.endswith(".json"):
            file_list.append(os.path.join(root, file))


for json_file in file_list:
    with open(json_file, "r") as f:
        data = json.load(f)
    prompt = f"""Instructions: 
keep all the numbers related to cooking and be specific about the steps that are provided and limit the number of ingredients to 10, and stick to the recipe provided.
Try to convert this json file to recipe text:

The json file is:
{data}
"""  # the prompt to send to the model

    body = json.dumps({
        "prompt": prompt,  # AI21
        "maxTokens": 2048,
        "temperature": 0,
        "topP": 0.5,
        "stopSequences": [],
        "countPenalty": {"scale": 0},
        "presencePenalty": {"scale": 0},
        "frequencyPenalty": {"scale": 0}
    })  # build the request payload

    #
    response = bedrock.invoke_model(body=body, modelId=bedrock_model_id, accept='application/json',
                                    contentType='application/json')  # send the payload to Bedrock

    #
    response_body = json.loads(response.get('body').read())  # read the response

    response_text = response_body.get("completions")[0].get("data").get("text")  # extract the text from the JSON response

    text_to_pdf(response_text, f"{json_file}.pdf")  # convert the text to a PDF file
