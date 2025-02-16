import psycopg2
from utils.slack_helper import SlackHelper


class PostgreSQLHelper():
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = self.connect_to_db()
        self.cursor = self.connection.cursor()

    def connect_to_db(self):
        """Establish a connection to the PostgreSQL database."""
        try:
           conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
           if conn:
                print("Connected to PostgreSQL database")
           return conn
        except psycopg2.OperationalError:
          msg = "Error connecting to PostgreSQL database"
          print(msg)
          slack_helper = SlackHelper()
          slack_helper.send_slack_notification(msg)


    def get(self, query, params=None):
        """Execute a SELECT query to fetch data from PostgreSQL."""

        try:
            # Execute the query
            self.cursor.execute(query, params)
            return self.cursor.fetchall()  # Return all results from SELECT query
        except Exception as e:
            print(f"Error fetching data from PostgreSQL: {e}")
            return None

    def set(self, query, params=None):
        """Execute an INSERT/UPDATE/DELETE query in PostgreSQL."""
        try:
            # Execute the query (INSERT/UPDATE/DELETE)
            self.cursor.execute(query, params)
            self.connection.commit()  # Commit changes to the database
        except Exception as e:
            self.connection.rollback()  # Rollback changes in case of error
            print(f"Error performing operation in PostgreSQL: {e}")
            return None

    def close(self):
        """Close the cursor and the database connection."""
        self.cursor.close()
        self.connection.close()