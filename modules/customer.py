from modules.user import User

class Customer(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address

    def add(self):
        pass

    def update_info(self):
        pass

    def show_info(self):
        pass

    def update_availability(self):
        pass

    def add_payment(self):
        pass