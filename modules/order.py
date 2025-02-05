from modules.service import Service

class Order(Service):
    def __init__(self, customer_id, status):
        super().__init__(customer_id, status)
        self.type = "order"

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