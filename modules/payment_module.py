from repositories.payment_repo import PaymentRepo
from repositories.ride_repo import RideRepo
from repositories.order_repo import OrderRepo

class PaymentModule:
    def __init__(self, db_helper):
       self.payment_repo = PaymentRepo(db_helper)
       self.ride_repo = RideRepo(db_helper)
       self.order_repo = OrderRepo(db_helper)

    def add(self, customer_id, service_type, service_id, amount):
        self.payment_repo.add(customer_id, service_type, service_id, amount)
        if service_type == 'order':
            self.order_repo.update_status(service_id, 'paid')
        elif service_type == 'ride':
            self.ride_repo.update_status(service_id, 'completed')


