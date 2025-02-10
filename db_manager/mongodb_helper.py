from pymongo import MongoClient
from db_manager.database_helper import DatabaseHelper

class MongoDBHelper(DatabaseHelper):
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.client = self.connect_to_db()
        self.db = self.client[self.database]

    def connect_to_db(self):
        """Establish a connection to the MongoDB database."""
        return MongoClient(self.host, self.port)

    def get(self, collection_name, query, params=None):
        """Retrieve data from the database (MongoDB find)."""
        try:
            collection = self.db[collection_name]
            return collection.find(query)  # Use collection_name dynamically
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def set(self, collection_name, query, data=None):
        """Perform an insert, update, or delete operation on MongoDB."""
        try:
            collection = self.db[collection_name]
            if query.get('action') == 'insert':
                result = collection.insert_one(data)  # Insert data
            elif query.get('action') == 'update':
                result = collection.update_one(query, {"$set": data})  # Update data
            elif query.get('action') == 'delete':
                result = collection.delete_one(query)  # Delete data
            else:
                raise ValueError("Unsupported action for set method")
            return result
        except Exception as e:
            print(f"Error performing operation: {e}")
            return None

    def close(self):
        """Close the MongoDB client connection."""
        self.client.close()