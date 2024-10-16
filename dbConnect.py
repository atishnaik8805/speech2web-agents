from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongoURL = api_key = os.getenv("DB_URL")
client = MongoClient(mongoURL)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.EventsDB
    eventsCollection = db['PersonEvents']

    document = {
        "Person": {
        "Name": "Atish Naik"
        },
        "Location": {
        "City": "Hyderabad"
        },
        "Event": {
        "Date": "20th October 2025"
        }
    }

    result = eventsCollection.insert_one(document)
    print(f"Document inserted with _id: {result.inserted_id}")
except Exception as e:
    print(e)