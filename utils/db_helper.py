import os
import psycopg2
from psycopg2 import OperationalError

class DBHelper:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                dbname='delivery',
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'),
                host='localhost',
                port='5432'
            )
            print("Connection established")
        except OperationalError as e:
            print(f"Error {e} occurred while connecting to PostgreSQL")

    def get(self, query, params=None):
        cursor = None
        """
        Executes a SELECT query and returns the results.
        """
        try:
            cursor = self.conn.cursor()

            # Execute the query with or without parameters

            cursor.execute(query, params)


            # Fetch results for SELECT query
            result = cursor.fetchall()
            cursor.close()

            return result

        except Exception as e:
            print(f"Error executing SELECT query: {e}")
            return []
        finally:
          if cursor:
                cursor.close()

    def set(self, query, params=None):
        cursor = None
        """
        Executes INSERT, UPDATE, DELETE queries and commits the changes.
        """
        try:
            cursor = self.conn.cursor()

            # Execute the query with or without parameters
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            # Commit the changes (for INSERT, UPDATE, DELETE queries)
            self.conn.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()  # Rollback if there's an error
            return 0
        finally:
            if cursor:
                cursor.close()
