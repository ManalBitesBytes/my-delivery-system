from repositories.order_repo import OrderRepo


class Order_Module():
    def __init__(self, db_helper):
        self.order_repo = OrderRepo(db_helper)


    def place(self, customer_id, amount):
        self.order_repo.add(customer_id, amount)


    def update_status(self, order_id, status):
        self.order_repo.update_status(order_id, status)


    def pay(self):
        pass

    def assign(self):
        pass

    def complete(self):
        pass

    def show_info(self):
        pass