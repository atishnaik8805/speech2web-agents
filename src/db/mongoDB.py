import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


MONGO_URI = os.getenv("DB_URL")
client = MongoClient(MONGO_URI)
db = client.EventsDB

try:
  client.admin.command("ping")
  print("You successfully connected to MongoDB!")
except Exception as e:
  print(e)


def insert_person_event(json_data: str):
  eventsCollection = db["PersonEvents"]
  personDocument = json.loads(json_data)
  return eventsCollection.insert_one(personDocument)


def insert_jobs(json_data: str):
  taskCollection = db["Jobs"]
  taskDocument = json.loads(json_data)
  return taskCollection.insert_one(taskDocument)
