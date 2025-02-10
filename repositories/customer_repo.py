import pandas as pd

class CustomerRepo:
    def __init__(self, db_helper):
        self.db_helper= db_helper


    def add_customer(self, name, phone, address):
            query = " INSERT INTO customers( name, phone, address) VALUES (%s, %s, %s)"
            self.db_helper.set(query, (name, phone, address))


    def update_customer(self, customer_id, name, phone, address):
        query = " UPDATE customers SET name = %s, phone = %s, address = %s WHERE customer_id = %s"
        self.db_helper.set(query, (customer_id, name, phone, address))


    def get_customer_id(self,phone):
        query = "SELECT customer_id FROM customers WHERE phone = %s"
        customer_id = self. db_helper.get(query, (phone,))
        customer_id[0][0]
        return pd.DataFrame(customer_id, columns=['customer_id'])


    def get_customer_info(self, customer_id):
        query = "SELECT name, phone, address from customers WHERE customer_id = %s"
        customer_info = self.db_helper.get( query, (customer_id,))
        return pd.DataFrame(customer_info, columns=['name', 'phone', 'address'])

    def get_customer_orders(self, customer_id):
        query = "SELECT order_id, status FROM orders WHERE customer_id = %s"
        orders = self.db_helper.get(query, (customer_id,))
        return pd.DataFrame(orders, columns=['order_id', 'status'])

    def get_customer_rides(self, customer_id):
        query = "SELECT ride_id, status, pick_up_location, drop_of_location FROM rides where ride_id = %s"
        orders = self.db_helper.get(query, (customer_id,))
        return pd.DataFrame(orders, columns=['ride_id', 'status', 'pick_up_location', 'drop_of_location'])

    def get_customer_payments(self, customer_id):
        query = "SELECT payment_id, service_type, amount FROM payment WHERE customer_id = %s"
        payments = self.db_helper.get(query, (customer_id,))
        return pd.DataFrame(payments, columns=['payment_id', 'service_type', 'amount'])