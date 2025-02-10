import pandas as pd

class PaymentRepo:
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add(self, customer_id, service_type, service_id, amount):
        query = "INSERT INTO payment (customer_id, service_type, service_id, amount) VALUES (%s, %s, %s, %s)"
        self.db_helper.set(query, (customer_id, service_type, service_id, amount))
