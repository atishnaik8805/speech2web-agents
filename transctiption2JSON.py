import subprocess

import spacy

import src.schema.sample_schema_01 as sample_schema_01
import src.schema.task_schema_01 as task_schema_01
from src.db.mongoDB import insert_person_event, insert_jobs


# Function to check and download the SpaCy model
def load_spacy_model(model_name="en_core_web_md") -> spacy.language.Language:
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
text = "Nick Oberoi, a software developer from San Francisco, attended a conference on October 5, 2024."
task_text = "I'm Nick Oberoi, today I installed glass panels on the car for 5 hours for Acme Industries."

# Convert text to JSON using the schema
json_data: str = sample_schema_01.create_schema(text, nlp)
print(json_data)

task_json: str = task_schema_01.create_schema(task_text, nlp)
print(task_json)

# Store Events data in MongoDB
insert_person_event(json_data)

# Store Task data in MongoDB
insert_jobs(task_json)


def transcription2JSONmain(text: str) -> str:
  json_data: str = sample_schema_01.create_schema(text, nlp)
  print("JSON Conversion", json_data)
  return json_data
