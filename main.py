import os
from db_manager.postgresql_helper import PostgreSQLHelper
from db_manager.mongodb_helper import MongoDBHelper
from modules.customer_module import CustomerModule
from modules.driver_module import DriverModule


if __name__ == "__main__":
    db_type = os.getenv("DB_TYPE")
    if db_type == 'POSTGRES':
        print(os.getenv('POSTGRES_HOST'),
                                           os.getenv('POSTGRES_DATABASE'),
                                           os.getenv('POSTGRES_USERNAME'),
                                           os.getenv('POSTGRES_PASSWORD')

              )
        postgres_helper = PostgreSQLHelper(os.getenv('POSTGRES_HOST'),
                                           os.getenv('POSTGRES_DATABASE'),
                                           os.getenv('POSTGRES_USERNAME'),
                                           os.getenv('POSTGRES_PASSWORD'))

        customer_module = CustomerModule(postgres_helper)
        driver_module = DriverModule(postgres_helper)

        print(customer_module.get_id('050000000'))
        print(driver_module.get_info( 1))











