import pandas as pd
from db_manager.postgresql_helper import PostgreSQLHelper
from db_manager.mongodb_helper import MongoDBHelper

class CustomerRepo:
    def __init__(self, db_helper):
        self.db_helper= db_helper


    def add_customer(self, name, phone, address):
        if isinstance(self.db_helper, PostgreSQLHelper):
            query = " INSERT INTO customers( name, phone, address) VALUES (%s, %s, %s)"
            self.db_helper.set(query, (name, phone, address))
        elif isinstance(self.db_helper, MongoDBHelper):
            data = {'name': name, 'phone': phone, 'address': address}
            self.db_helper.insert("customers", data)



    def update_customer(self, customer_id, name, phone, address):
        if isinstance(self.db_helper, PostgreSQLHelper):
            query = " UPDATE customers SET name = %s, phone = %s, address = %s WHERE customer_id = %s"
            self.db_helper.set(query, (customer_id, name, phone, address))
        elif isinstance(self.db_helper, MongoDBHelper):
            data = {'name': name, 'phone': phone, 'address': address}
            query = {'_id': customer_id}  # Assuming customer_id is the MongoDB document _id
            self.db_helper.update("customers", query, data)


    def get_customer_id(self,phone):
        if isinstance(self.db_helper, PostgreSQLHelper):
            query = "SELECT customer_id FROM customers WHERE phone = %s"
            customer_id = self. db_helper.get(query, (phone,))
            customer_id[0][0]
            return pd.DataFrame(customer_id, columns=['customer_id'])
        elif isinstance(self.db_helper, MongoDBHelper):
            query = {'phone': phone}
            projection = {'_id': 1}
            customer_id = self.db_helper.get("customers", query, projection)
            customer_id = list(customer_id)
            return customer_id[0]['_id']


    def get_customer_info(self, customer_id):
        if isinstance(self.db_helper, PostgreSQLHelper):
            query = "SELECT name, phone, address from customers WHERE customer_id = %s"
            customer_info = self.db_helper.get( query, (customer_id,))
            return pd.DataFrame(customer_info, columns=['name', 'phone', 'address'])
        elif isinstance(self.db_helper, MongoDBHelper):
            query = {'_id': customer_id}  # Assuming _id is the unique identifier for MongoDB
            projection = {'_id': 0, 'name': 1, 'phone': 1, 'address': 1}  # Only return name, phone, address
            result = self.db_helper.get("customers", query, projection)

            customer_info = list(result)  # Convert cursor to list
            if customer_info:
                # Return the data in a clean format, with a dictionary structure
                return pd.DataFrame(customer_info, columns=['name', 'phone', 'address'])
            else:
                return None


    def get_customer_orders(self, customer_id):
        if isinstance(self.db_helper, PostgreSQLHelper):
            query = "SELECT order_id, status FROM orders WHERE customer_id = %s"
            orders = self.db_helper.get(query, (customer_id,))
            return pd.DataFrame(orders, columns=['order_id', 'status'])
        elif isinstance(self.db_helper, MongoDBHelper):
            query = {'customer_id': customer_id}
            projection = {'_id': 0, 'order_id': 1, 'status': 1}  # Only return order_id and status
            result = self.db_helper.get("orders", query, projection)

            orders = list(result)  # Convert cursor to list
            if orders:
                return pd.DataFrame(orders, columns=['order_id', 'status'])
            else:
                return pd.DataFrame(columns=['order_id', 'status'])


    def get_customer_rides(self, customer_id):
        if isinstance(self.db_helper, PostgreSQLHelper):
            query = "SELECT ride_id, status, pick_up_location, drop_of_location FROM rides where ride_id = %s"
            orders = self.db_helper.get(query, (customer_id,))
            return pd.DataFrame(orders, columns=['ride_id', 'status', 'pick_up_location', 'drop_of_location'])
        elif isinstance(self.db_helper, MongoDBHelper):
            query = {'customer_id': customer_id}
            projection = {'_id': 0, 'ride_id': 1, 'status': 1, 'pick_up_location': 1,
                          'drop_off_location': 1}  # Include necessary fields
            result = self.db_helper.get("rides", query, projection)

            rides = list(result)  # Convert cursor to list
            if rides:
                return pd.DataFrame(rides, columns=['ride_id', 'status', 'pick_up_location', 'drop_off_location'])
            else:
                return pd.DataFrame(columns=['ride_id', 'status', 'pick_up_location',
                                             'drop_off_location'])  # Empty DataFrame if no rides


    def get_customer_payments(self, customer_id):
        if isinstance(self.db_helper, PostgreSQLHelper):
            query = "SELECT payment_id, service_type, amount FROM payment WHERE customer_id = %s"
            payments = self.db_helper.get(query, (customer_id,))
            return pd.DataFrame(payments, columns=['payment_id', 'service_type', 'amount'])