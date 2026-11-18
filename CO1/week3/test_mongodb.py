
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    print("ERROR: MONGODB_URI not found in .env file")
    exit()

if not uri.startswith("mongodb+srv://"):
    print("ERROR: Your connection string is not an Atlas SRV URI.")
    print("Check your .env file.")
    exit()

print("MongoDB URI loaded successfully!")
print("Atlas connection string detected.")

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=10000)

    client.admin.command("ping")

    print("MongoDB Atlas Connected Successfully!")

    db = client["genai_database"]
    print("Database Name:", db.name)

    client.close()

except Exception as e:
    print("MongoDB Connection Error:", e)
