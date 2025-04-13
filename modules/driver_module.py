
from repositories.driver_repo import DriverRepo

class DriverModule:
    def __init__(self, db_handler):
        self.driver_repo = DriverRepo(db_handler)

    def add(self, name, phone, car_number):
        self.driver_repo.add_driver(name, phone,car_number)

    def update_info(self,driver_id, name, phone, car_number):
        self.driver_repo.update_driver(driver_id, name, phone, car_number)


    def get_id( self, phone):
        driver_id = self.driver_repo.get_driver_id(phone)
        return driver_id

    def get_info(self, driver_id):
        result = self.driver_repo.get_driver_info(driver_id)
        return result

    def set_availability(self, driver_id, is_available):
        if is_available not in [0, 1]:
            print("Invalid availability status. Must be 0 or 1.")
            return 0
        else:
            self.driver_repo. set_driver_availability(driver_id, is_available)

    def get_available_driver(self):
       return self.driver_repo.get_available_driver()

    def assign_to_driver(self, service_type, service_id):
        driver_id = self.get_available_driver()
        driver_id = driver_id
        self.driver_repo.assign_to_driver(driver_id, service_type, service_id)
        self.set_availability(driver_id, 0)

    def get_driver_history(self, driver_id):
        return self.driver_repo.get_driver_history(driver_id)

