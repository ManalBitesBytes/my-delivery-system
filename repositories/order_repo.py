import pandas as pd


class OrderRepo:
    def __init__(self, db_helper):
        self.db_helper = db_helper


    def add(self, customer_id, amount):
        query = "INSERT INTO orders (customer_id) VALUES %s"
        self.db_helper.set(query, (customer_id,))

    def update_status(self, order_id, status):
        query = "UPDATE orders SET status = %s WHERE customer_id = %s"
        self.db_helper.set(query, (status, order_id))




