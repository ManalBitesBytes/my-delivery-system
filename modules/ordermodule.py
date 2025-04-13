from repositories.order_repo import OrderRepo


class OrderModule():
    def __init__(self, db_helper):
        self.order_repo = OrderRepo(db_helper)


    def add(self, customer_id):
        self.order_repo.add(customer_id)


    def update_status(self, order_id, status):
        self.order_repo.update_status(order_id, status)


    def pay(self):
        pass

    def assign(self):
        pass

    def complete(self):
        pass

    def show_info(self, order_id):
        return  self.order_repo.show_info(order_id)
