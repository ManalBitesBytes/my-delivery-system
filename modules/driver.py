from modules.user import User

class Driver(User):
    def __init__(self, name, phone, car_number):
        super().__init__(name, phone)
        self._car_number = car_number
        self.is_available = 1

    def add(self):
        pass

    def update_info(self):
        pass

    def show_info(self):
        pass

    def update_availability(self):
        pass

