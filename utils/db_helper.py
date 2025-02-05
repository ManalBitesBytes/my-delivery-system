import os
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

import psycopg2
from psycopg2 import OperationalError
class DBHelper:
    def __init__(self):
        self.conn = None
        try:
             self.conn = psycopg2.connect(dbname='delivery',
                                user=db_username,
                                password = db_password,
                                host='localhost',
                                port='5432'
                                )

        except OperationalError as e:
             print(f"Error {e} occurred while connecting to PostgreSQL")

    def get(self, query, params=None):
        """
        Handles SELECT queries, fetches data and returns a list of results.
        """
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            # Fetch results for SELECT query
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(f"Error executing SELECT query: {e}")
            return []
        finally:
            cursor.close()

    def set(self, query, params=None):
        """
        Handles INSERT, UPDATE, DELETE queries, executes them and returns the number of rows affected.
        """
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            # Commit the changes (for INSERT, UPDATE, DELETE queries)
            self.conn.commit()

            # Return the number of rows affected (e.g., for UPDATE or INSERT queries)
            return cursor.rowcount

        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()  # Rollback if there's an error
            return 0
        finally:
            cursor.close()
