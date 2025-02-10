
from repositories.customer_repo import CustomerRepo

class CustomerModule:
    def __init__(self, db_helper):
        self.customer_repo = CustomerRepo(db_helper)

    def add( self, name, phone, address):
        self.customer_repo.add_customer(name, phone, address)


    def update_info(self, name, phone, address):
         self.customer_repo.update_customer(name, phone, address)

    def add_payment(self):
         pass


    def get_id(self, phone):
            """
            Retrieves the customer ID based on the phone number.
            """
            result = self.customer_repo.get_customer_id(phone)
            return result


    def get_info(self,  customer_id):
            result = self.customer_repo.get_customer_info(customer_id)
            return result


