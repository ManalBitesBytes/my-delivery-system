from modules.service import Service

class Ride(Service):
    def __init__(self, customer_id, status, pick_up_location, delivery_location):
        super().__init__(customer_id, status)
        self.pick_up_location = None
        self.delivery_location = None

    def place(self):
        pass

    def pay(self):
        pass

    def assign(self):
        pass

    def complete(self):
        pass

    def show_info(self):
        pass