from utils.db_helper import DBHelper

def add_driver(name, phone, car_number):
    query = " INSERT INTO drivers( name, phone, car_number) VALUES (%s, %s, %s)"
    db_helper = DBHelper()
    db_helper.set(query, (name, phone, car_number))

def update_driver(driver_id, name, phone, car_number):
    query = " UPDATE drivers SET name = %s, phone = %s, car_number = %s WHERE driver_id = %s"
    db_helper = DBHelper()
    db_helper.set(query, (driver_id, name, phone, car_number))

def get_driver_id(phone):
    query = "SELECT driver_id FROM drivers WHERE phone = %s"
    db_helper = DBHelper()
    driver_id = db_helper.get(query, (phone,))
    return driver_id[0][0]

def get_driver_info(driver_id):
    query = "SELECT name, phone, car_number, availability from drivers WHERE driver_id = %s"
    db_helper = DBHelper()
    driver_info = db_helper.get(query, (driver_id,))
    return driver_info

def set_driver_availability(driver_id, availability):
    if availability not in [0, 1]:
        print("Invalid availability status. Must be 0 or 1.")
        return 0
    else:
        query = "UPDATE drivers SET availability = %s WHERE driver_id = %s"
        db_helper = DBHelper()
        db_helper.set(query, (availability, driver_id))
