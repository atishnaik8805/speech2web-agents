import json

import spacy
from spacy import displacy
from spacy.tokens.doc import Doc
from src.helper.userIdGenerator import generate_user_id


def create_schema(text: str, nlp: spacy.language.Language, debug: bool = False) -> str:
  doc: Doc = nlp(text)
  data: dict = {"Person": {}, "Location": {}, "Event": {}}

  if debug:
    displacy.serve(doc, style="ent", host="localhost")

  # Extract entities and fill the schema
  for ent in doc.ents:
    if ent.label_ == "PERSON":
      data["Person"]["UserID"] = generate_user_id(ent.text)
      data["Person"]["Name"] = ent.text
    elif ent.label_ == "GPE":
      data["Location"]["City"] = ent.text
    elif ent.label_ == "DATE":
      data["Event"]["Date"] = ent.text
    elif ent.label_ == "ORG":
      data["Person"]["Occupation"] = ent.text

  return json.dumps(data, indent=4)
