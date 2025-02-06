from modules.driver import Driver
Driver.set_availability(Driver.get_id('1234567890'), 1)
name, phone, car_number, availability = Driver.get_info(Driver.get_id('1234567890'))
print(name, phone, car_number, availability)

