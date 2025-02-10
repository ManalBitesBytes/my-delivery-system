import pandas as pd


class OrderRepo:
    def __init__(self, db_helper):
        self.db_helper = db_helper


    def add(self, customer_id):
        query = "INSERT INTO orders (customer_id) VALUES (%s)"
        self.db_helper.set(query, (customer_id,))


    def update_status(self, order_id, status):
        query = "UPDATE orders SET status = %s WHERE order_id = %s"
        self.db_helper.set(query, (status, order_id))

    def show_info(self, order_id):
        query = "SELECT customer_id, status FROM orders where order_id = %s"
        result = self.db_helper.get(query, (order_id,))
        return pd.DataFrame(result, columns=['customer_id', 'status'])





