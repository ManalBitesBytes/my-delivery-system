from modules.user import User
from repoitories import customer_repo
from utils.db_helper import DBHelper

class Customer(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address


    def add(self, name, phone, address):
        customer_repo.add_customer(name, phone, address)


    def update_info(self, name, phone, address):
        customer_repo.update_customer(name, phone, address)

    def add_payment(self):
        pass

    @staticmethod
    def get_id(phone):
        """
        Retrieves the customer ID based on the phone number.
        """
        result = customer_repo.get_customer_id(phone)
        # If result exists, extract the customer_id
        if result:

            return result
        else:
            return None

    @staticmethod
    def get_info( customer_id):
        result = customer_repo.get_customer_info(customer_id)
        name = result[0][0]
        phone = result[0][1]
        address = result[0][2]
        return name, phone, address


