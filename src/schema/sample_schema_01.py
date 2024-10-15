import json

import spacy
from spacy.tokens.doc import Doc


def create_schema(text: str, nlp: spacy.language.Language) -> str:
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
