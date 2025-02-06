from modules.user import User
from repoitories.driver_repo import *

class Driver(User):
    def __init__(self, name, phone, car_number):
        super().__init__(name, phone)
        self._car_number = car_number
        self.is_available = 1

    def add(self):
       add_driver(self.name, self.phone, self._car_number)

    def update_info(self,driver_id, name, phone, car_number):
       update_driver(driver_id, name, phone, car_number)

    @staticmethod
    def get_id( phone):
        driver_id = get_driver_id(phone)
        return driver_id
    @staticmethod
    def get_info(driver_id):
        result = get_driver_info(driver_id)
        name = result[0][0]
        phone = result[0][1]
        car_number = result[0][2]
        is_available = result[0][3]
        return name, phone, car_number, is_available == 1
    @staticmethod
    def set_availability(driver_id, is_available):
        set_driver_availability(driver_id, is_available)


