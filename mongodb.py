from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.encoders import jsonable_encoder


class MongoDB:
    def __init__(self, mongo_url: str = "mongodb://localhost:27017", db_name: str = "scrapper"):
        """ Initialize the MongoDB connection with default values. """
        self.client = AsyncIOMotorClient(mongo_url)  # Create MongoDB client
        self.db = self.client[db_name]  # Access the database
    
    def get_db(self):
        """ Returns the database object. """
        return self.db

    def get_collection(self, collection_name: str):
        """ Get a specific collection from the database. """
        return self.db[collection_name]

    async def fetch_all(self, collection_name: str, limit: int = 10, skip: int = 0) -> list:
        """ Fetch all documents from a given collection with optional pagination. """
        collection = self.get_collection(collection_name)
        cursor = collection.find().skip(skip).limit(limit)
        documents = []
        async for document in cursor:
            documents.append(document)
        return documents
    
    async def insert_many(self, collection_name: str, data: list):
        serializable_data = jsonable_encoder(data)
        return self.db[collection_name].insert_many(serializable_data)
        