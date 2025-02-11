from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBHelper():
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.client = self.connect_to_db()
        self.db = self.client[self.database]

    def connect_to_db(self):
        """Establish a connection to the MongoDB database."""
        try:
            return MongoClient(self.host, self.port)
            print("Connected to MongoDB")
        except ConnectionFailure:
            print("Could not connect to MongoDB")

    def insert(self, collection_name, data):
        """Insert a document into the specified MongoDB collection."""
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(data)
            print(f"Inserted document with id: {result.inserted_id}")
            return result
        except Exception as e:
            print(f"Error inserting data: {e}")
            return None

    def update(self, collection_name, query, data):
        """Update a document in the specified MongoDB collection."""
        try:
            collection = self.db[collection_name]
            result = collection.update_one(query, {"$set": data})
            if result.modified_count > 0:
                print(f"Updated document with query: {query}")
            else:
                print(f"No document matched the query: {query}")
            return result
        except Exception as e:
            print(f"Error updating data: {e}")
            return None

    def delete(self, collection_name, query):
        """Delete a document from the specified MongoDB collection."""
        try:
            collection = self.db[collection_name]
            result = collection.delete_one(query)
            if result.deleted_count > 0:
                print(f"Deleted document with query: {query}")
            else:
                print(f"No document matched the query to delete: {query}")
            return result
        except Exception as e:
            print(f"Error deleting data: {e}")
            return None

    def get(self, collection_name, query, projection=None):
        """Retrieve data from the database (MongoDB find)."""
        try:
            collection = self.db[collection_name]
            return collection.find(query, projection)
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def close(self):
        """Close the connection to MongoDB."""
        self.client.close()