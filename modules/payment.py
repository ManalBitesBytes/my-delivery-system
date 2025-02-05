from abc import ABC, abstractmethod
from modules.service import Service

class Payment(ABC):
    def __init__(self, service: Service ):
        self.amount = service.amount
        self.customer_id = service.customer_id
        self.service_type  = service.type
        self.service_id = service.id
        method = None

    @abstractmethod
    def process_payment(self):
       pass

class CreditCard(Payment):
    def __init__(self, service: Service, amount ):
        super().__init__(service, amount)
        method = "creditcard"

    def process_payment(self):
        pass


class Cash(Payment):
    def __init__(self, service: Service, amount ):
        super().__init__(service, amount)
        method = "cash"

    def process_payment(self):
        pass


