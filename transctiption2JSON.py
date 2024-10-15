import json
import subprocess

import spacy
from spacy.tokens.doc import Doc


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
def create_schema(text) -> str:
  doc: Doc = nlp(text)
  data: dict = {"Person": {}, "Location": {}, "Event": {}}

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
json_data: str = create_schema(text)


def transcription2JSONmain(text) -> str:
  json_data: str = create_schema(text)
  print("JSON Conversion", json_data)
  return json_data


print(json_data)
