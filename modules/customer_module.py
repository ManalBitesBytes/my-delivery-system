
from repositories.customer_repo import CustomerRepo
import pandas as pd


class CustomerModule:
    def __init__(self, db_helper):
        self.db_helper = db_helper
        self.customer_repo = CustomerRepo(db_helper)

    def add( self, name, phone, address):
        self.customer_repo.add_customer(name, phone, address)


    def update_info(self, name, phone, address):
         customer_id = self.customer_repo.get_customer_id(phone)
         self.customer_repo.update_customer(customer_id, name, phone, address)


    def get_id(self, phone):
            """
            Retrieves the customer ID based on the phone number.
            """
            result = self.customer_repo.get_customer_id(phone)
            return result


    def get_info(self,  phone):
       customer_id = self.customer_repo.get_customer_id(phone)
       result = self.customer_repo.get_customer_info(customer_id)
       print(customer_id)
       return result

    def get_customer_orders(self, customer_id):
        result = self.customer_repo.get_customer_orders(customer_id)
        return result

    def get_customer_rides(self, customer_id):
        result = self.customer_repo.get_customer_rides(customer_id)
        return result

    def get_customer_payments(self, customer_id):
        result = self.customer_repo.get_customer_payments(customer_id)
        return result


