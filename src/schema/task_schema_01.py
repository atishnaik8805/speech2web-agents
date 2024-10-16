import json

import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens.doc import Doc

from src.helper.date import SUPPORTED_DATE_TOKENS, parse_date_from_token
from src.helper.userIdGenerator import generate_user_id


def create_schema(text: str, nlp: spacy.language.Language, debug: bool = False) -> str:
  doc: Doc = nlp(text)
  data: dict = {"Person": {}, "Task": {}}

  if debug:
    displacy.serve(doc, style="ent", host="localhost")

  # Matcher to extract task performed
  matcher = Matcher(nlp.vocab)
  pattern: list[dict[str, str]] = [
    {"POS": "VERB"},  # Action (Verb)
    {"POS": "NOUN", "OP": "+"},  # Object of the action (Nouns)
    {"LOWER": "on", "OP": "?"},  # Preposition (e.g., "on the car")
    {"POS": "NOUN", "OP": "?"},  # Prepositional object (e.g., "car")
  ]

  matcher.add("TASK_PATTERN", [pattern])
  matches: list[tuple] = matcher(doc)

  longest_matched_task: str = ""
  for match_id, start, end in matches:
    matched_span = doc[start:end]
    if len(matched_span.text) > len(longest_matched_task):
      longest_matched_task = matched_span.text

  # Extract entities and fill the schema
  data["Task"]["Description"] = longest_matched_task
  for ent in doc.ents:
    if ent.label_ == "PERSON":
      data["Person"]["UserID"] = generate_user_id(ent.text)
      data["Person"]["Name"] = ent.text
    if ent.label_ == "TIME":
      data["Task"]["Duration"] = ent.text
    elif ent.label_ == "ORG":
      data["Task"]["Client"] = ent.text
    elif ent.label_ == "DATE":
      if ent.text.lower() in SUPPORTED_DATE_TOKENS:
        parsed_date: str = parse_date_from_token(ent.text)
        data["Task"]["Date"] = parsed_date
      else:
        data["Task"]["Date"] = ent.text

  return json.dumps(data, indent=4)
