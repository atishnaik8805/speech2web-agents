# import openai
# import json

# # Set your OpenAI API key
# openai.api_key = 'your_openai_api_key_here'

# def convert_text_to_json(text):
#     # Define the prompt for the model
#     prompt = f"Convert the following text into a JSON object:\n{text}\nReturn only the JSON object."
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # or another model of your choice
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0,
#         max_tokens=1500
#     )
    
#     # Extract the content from the response
#     json_text = response['choices'][0]['message']['content']
    
#     # Attempt to parse the response as JSON
#     try:
#         json_result = json.loads(json_text)
#         return json_result
#     except json.JSONDecodeError as e:
#         print("Error decoding JSON:", e)
#         return None

# # Example usage
# text_input = "Your input text goes here."
# json_output = convert_text_to_json(text_input)
# print(json_output)


## Run this python -m spacy download en_core_web_sm

import spacy
import subprocess
import os
import json  # Add this import

# Function to check and download the SpaCy model
def load_spacy_model(model_name="en_core_web_sm"):
    try:
        # Try to load the model
        nlp = spacy.load(model_name)
    except OSError:
        # Model not found, download it
        print(f"Model {model_name} not found. Downloading now...")
        subprocess.run(["python", "-m", "spacy", "download", model_name])
        nlp = spacy.load(model_name)
    return nlp

# Load the SpaCy model
nlp = load_spacy_model()

# Define schema
def create_schema(text):
    doc = nlp(text)
    data = {
        "Person": {},
        "Location": {},
        "Event": {}
    }

    # Extract entities and fill the schema
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            data["Person"]["Name"] = ent.text
        elif ent.label_ == "GPE":
            data["Location"]["City"] = ent.text
        elif ent.label_ == "DATE":
            data["Event"]["Date"] = ent.text
        elif ent.label_ == "ORG":
            data["Person"]["Occupation"] = ent.text
    
    return json.dumps(data, indent=4)

# Sample text
text = "John Doe, a software developer from San Francisco, attended a conference on October 5, 2024."

# Convert text to JSON using the schema
json_data = create_schema(text)
print(json_data)


