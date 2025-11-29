
from pymongo import MongoClient
from decouple import config
import sys

try:
    print("Attempting to load MONGO_URI from .env...")
    mongoURI = config('MONGO_URI', default=None)
    
    if not mongoURI:
        print("Error: MONGO_URI not found in .env or environment variables.")
        sys.exit(1)
        
    print(f"MONGO_URI found: {mongoURI[:10]}... (masked)")
    
    print("Attempting to connect to MongoDB...")
    client = MongoClient(mongoURI, serverSelectionTimeoutMS=5000)
    
    # Trigger a connection to verify
    server_info = client.server_info()
    print("Successfully connected to MongoDB!")
    print("Server info:", server_info)
    
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    sys.exit(1)
