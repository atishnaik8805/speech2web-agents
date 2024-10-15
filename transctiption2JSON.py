import subprocess

import spacy

import src.schema.sample_schema_01 as sample_schema_01


# Function to check and download the SpaCy model
def load_spacy_model(model_name="en_core_web_sm") -> spacy.language.Language:
  try:
    # Try to load the model
    nlp = spacy.load(model_name)
  except OSError:
    # Model not found, download it
    print(f"Model {model_name} not found. Downloading now...")
    subprocess.run(["python", "-m", "spacy", "download", model_name])
    nlp: spacy.language.Language = spacy.load(model_name)
  return nlp


# Load the SpaCy model
nlp: spacy.language.Language = load_spacy_model()

# Sample text
text = "John Doe, a software developer from San Francisco, attended a conference on October 5, 2024."

# Convert text to JSON using the schema
json_data: str = sample_schema_01.create_schema(text, nlp)
print(json_data)


def transcription2JSONmain(text: str) -> str:
  json_data: str = sample_schema_01.create_schema(text, nlp)
  print("JSON Conversion", json_data)
  return json_data
