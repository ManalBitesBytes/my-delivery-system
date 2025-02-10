import pandas as pd

class DriverRepo:
    def __init__(self,db_helper ):
        self.db_helper = db_helper

    def add_driver(self, name, phone, car_number):
        query = " INSERT INTO drivers( name, phone, car_number) VALUES (%s, %s, %s)"
        self.db_helper.set(query, (name, phone, car_number))

    def update_driver(self, driver_id, name, phone, car_number):
        query = " UPDATE drivers SET name = %s, phone = %s, car_number = %s WHERE driver_id = %s"
        self.db_helper.set(query, (driver_id, name, phone, car_number))

    def get_driver_id(self, phone):
        query = "SELECT driver_id FROM drivers WHERE phone = %s"
        driver_id = self.db_helper.get(query, (phone,))
        return pd.DataFrame(driver_id, columns=['driver_id'])

    def get_driver_info(self,driver_id):
        query = "SELECT name, phone, car_number, availability from drivers WHERE driver_id = %s"
        driver_info = self.db_helper.get(query, (driver_id,))
        return pd.DataFrame(driver_info, columns=['name', 'phone', 'car_number', 'availability'])

    def set_driver_availability(self, driver_id, availability):
        if availability not in [0, 1]:
            print("Invalid availability status. Must be 0 or 1.")
            return 0
        else:
            query = "UPDATE drivers SET availability = %s WHERE driver_id = %s"

            self.db_helper.set(query, (availability, driver_id))
