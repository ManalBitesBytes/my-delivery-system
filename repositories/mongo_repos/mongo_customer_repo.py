import pandas as pd
from db_manager.mongodb_helper import MongoDBHelper

class MongoDBCustomerRepo:
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add_customer(self, name, phone, address):
        data = {'name': name, 'phone': phone, 'address': address}
        self.db_helper.insert("customers", data)

    def update_customer(self, customer_id, name, phone, address):
        data = {'name': name, 'phone': phone, 'address': address}
        query = {'_id': customer_id}
        self.db_helper.update("customers", query, data)

    def get_customer_id(self, phone):
        query = {'phone': phone}
        projection = {'_id': 1}
        customer_id = self.db_helper.get("customers", query, projection)
        customer_id = list(customer_id)
        return customer_id[0]['_id'] if customer_id else None

    def get_customer_info(self, customer_id):
        query = {'_id': customer_id}
        projection = {'_id': 0, 'name': 1, 'phone': 1, 'address': 1}
        result = self.db_helper.get("customers", query, projection)
        customer_info = list(result)
        return pd.DataFrame(customer_info, columns=['name', 'phone', 'address']) if customer_info else None

    def get_customer_orders(self, customer_id):
        query = {'customer_id': customer_id}
        projection = {'_id': 0, 'order_id': 1, 'status': 1}
        result = self.db_helper.get("orders", query, projection)
        orders = list(result)
        return pd.DataFrame(orders, columns=['order_id', 'status']) if orders else pd.DataFrame(columns=['order_id', 'status'])

    def get_customer_rides(self, customer_id):
        query = {'customer_id': customer_id}
        projection = {'_id': 0, 'ride_id': 1, 'status': 1, 'pick_up_location': 1, 'drop_off_location': 1}
        result = self.db_helper.get("rides", query, projection)
        rides = list(result)
        return pd.DataFrame(rides, columns=['ride_id', 'status', 'pick_up_location', 'drop_off_location']) if rides else pd.DataFrame(columns=['ride_id', 'status', 'pick_up_location', 'drop_off_location'])

    def get_customer_payments(self, customer_id):
        query = {'customer_id': customer_id}
        projection = {'_id': 0, 'payment_id': 1, 'service_type': 1, 'amount': 1}
        result = self.db_helper.get("payments", query, projection)
        payments = list(result)
        return pd.DataFrame(payments, columns=['payment_id', 'service_type', 'amount']) if payments else pd.DataFrame(columns=['payment_id', 'service_type', 'amount'])
