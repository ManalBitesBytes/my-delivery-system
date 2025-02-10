import os
from db_manager.postgresql_helper import PostgreSQLHelper
from db_manager.mongodb_helper import MongoDBHelper
from modules.customer_module import CustomerModule
from modules.driver_module import DriverModule
from modules.order_module import Order_Module
from modules.ride_module import RideModule
from modules.payment_module import PaymentModule


def display_main_menu():
    print("\nWelcome to the Delivery System!")
    print("1. Customer Operations")
    print("2. Driver Operations")
    print("3. Order Operations")
    print("4. Ride Operations")
    print("5. Payment Operations")
    print("6. Exit")


def display_customer_menu():
    print("\nCustomer Menu:")
    print("1. Add Customer")
    print("2. Update Customer Info")
    print("3. Get Customer Info")
    print("4. Get Customer Orders")
    print("5. Get Customer Rides")
    print("6. Back to Main Menu")


def display_driver_menu():
    print("\nDriver Menu:")
    print("1. Add Driver")
    print("2. Update Driver Info")
    print("3. Get Driver Info")
    print("4. Set Driver Availability")
    print("5. Assign Driver to Service")
    print("6. Get Driver History")
    print("7. Back to Main Menu")


def display_order_menu():
    print("\nOrder Menu:")
    print("1. Add Order")
    print("2. Update Order Status")
    print("3. Show Order Info")
    print("4. Back to Main Menu")


def display_ride_menu():
    print("\nRide Menu:")
    print("1. Add Ride")
    print("2. Update Ride Status")
    print("3. Show Ride Info")
    print("4. Back to Main Menu")


def display_payment_menu():
    print("\nPayment Menu:")
    print("1. Add Payment")
    print("2. Back to Main Menu")


def main():
    db_type = os.getenv("DB_TYPE", "POSTGRES")

    # Initialize the appropriate database helper based on the environment variable
    if db_type == 'POSTGRES':
        postgres_helper = PostgreSQLHelper(
            os.getenv('POSTGRES_HOST'),
            os.getenv('POSTGRES_DATABASE'),
            os.getenv('POSTGRES_USERNAME'),
            os.getenv('POSTGRES_PASSWORD')
        )
    else:
        raise ValueError("Unsupported DB Type")

    # Initialize modules with the DB helper
    customer_module = CustomerModule(postgres_helper)
    driver_module = DriverModule(postgres_helper)
    order_module = Order_Module(postgres_helper)
    ride_module = RideModule(postgres_helper)
    payment_module = PaymentModule(postgres_helper)

    while True:
        # Show the main menu
        display_main_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            while True:
                # Customer Menu
                display_customer_menu()
                customer_choice = input("Choose an action: ")

                if customer_choice == "1":
                    name = input("Enter name: ")
                    phone = input("Enter phone: ")
                    address = input("Enter address: ")
                    customer_module.add(name, phone, address)
                elif customer_choice == "2":
                    customer_id = input("Enter customer ID: ")
                    name = input("Enter name: ")
                    phone = input("Enter phone: ")
                    address = input("Enter address: ")
                    customer_module.update_info(customer_id, name, phone, address)
                elif customer_choice == "3":
                    phone = input("Enter phone number: ")
                    customer_info = customer_module.get_info(phone)
                    print(customer_info)
                elif customer_choice == "4":
                    customer_id = input("Enter customer ID: ")
                    orders = customer_module.get_customer_orders(customer_id)
                    print(orders)
                elif customer_choice == "5":
                    customer_id = input("Enter customer ID: ")
                    rides = customer_module.get_customer_rides(customer_id)
                    print(rides)
                elif customer_choice == "6":
                    break  # Return to the Main Menu
                else:
                    print("Invalid option. Try again.")

        elif choice == "2":
            while True:
                # Driver Menu
                display_driver_menu()
                driver_choice = input("Choose an action: ")

                if driver_choice == "1":
                    name = input("Enter name: ")
                    phone = input("Enter phone: ")
                    car_number = input("Enter car number: ")
                    driver_module.add(name, phone, car_number)
                elif driver_choice == "2":
                    driver_id = input("Enter driver ID: ")
                    name = input("Enter name: ")
                    phone = input("Enter phone: ")
                    car_number = input("Enter car number: ")
                    driver_module.update_info(driver_id, name, phone, car_number)
                elif driver_choice == "3":
                    driver_id = input("Enter driver ID: ")
                    driver_info = driver_module.get_info(driver_id)
                    print(driver_info)
                elif driver_choice == "4":
                    driver_id = input("Enter driver ID: ")
                    is_available = int(input("Set availability (1 for available, 0 for not available): "))
                    driver_module.set_availability(driver_id, is_available)
                elif driver_choice == "5":
                    service_type = input("Enter service type (order/ride): ")
                    service_id = input("Enter service ID: ")
                    driver_module.assign_to_driver(service_type, service_id)
                elif driver_choice == "6":
                    driver_id = input("Enter driver ID: ")
                    history = driver_module.get_driver_history(driver_id)
                    print(history)
                elif driver_choice == "7":
                    break  # Return to the Main Menu
                else:
                    print("Invalid option. Try again.")

        elif choice == "3":
            while True:
                # Order Menu
                display_order_menu()
                order_choice = input("Choose an action: ")

                if order_choice == "1":
                    customer_id = input("Enter customer ID: ")
                    order_module.add(customer_id)
                elif order_choice == "2":
                    order_id = input("Enter order ID: ")
                    status = input("Enter new status: ")
                    order_module.update_status(order_id, status)
                elif order_choice == "3":
                    order_id = input("Enter order ID: ")
                    order_info = order_module.show_info(order_id)
                    print(order_info)
                elif order_choice == "4":
                    break  # Return to the Main Menu
                else:
                    print("Invalid option. Try again.")

        elif choice == "4":
            while True:
                # Ride Menu
                display_ride_menu()
                ride_choice = input("Choose an action: ")

                if ride_choice == "1":
                    customer_id = input("Enter customer ID: ")
                    pickup_location = input("Enter pickup location: ")
                    dropoff_location = input("Enter dropoff location: ")
                    ride_module.add(customer_id, pickup_location, dropoff_location)
                elif ride_choice == "2":
                    ride_id = input("Enter ride ID: ")
                    status = input("Enter new status: ")
                    ride_module.update_status(ride_id, status)
                elif ride_choice == "3":
                    ride_id = input("Enter ride ID: ")
                    ride_info = ride_module.show_info(ride_id)
                    print(ride_info)
                elif ride_choice == "4":
                    break  # Return to the Main Menu
                else:
                    print("Invalid option. Try again.")

        elif choice == "5":
            while True:
                # Payment Menu
                display_payment_menu()
                payment_choice = input("Choose an action: ")

                if payment_choice == "1":
                    customer_id = input("Enter customer ID: ")
                    service_type = input("Enter service type (order/ride): ")
                    service_id = input("Enter service ID: ")
                    amount = float(input("Enter payment amount: "))
                    payment_module.add(customer_id, service_type, service_id, amount)
                elif payment_choice == "2":
                    break  # Return to the Main Menu
                else:
                    print("Invalid option. Try again.")

        elif choice == "6":
            print("Exiting... Goodbye!")
            break  # Exit the program

        else:
            print("Invalid option. Try again.")




if __name__ == "__main__":
    main()


