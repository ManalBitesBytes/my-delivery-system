
from repositories.postgres_repos.postgresql_customer_repo import PostgreSQLCustomerRepo
from repositories.mongo_repos.mongo_customer_repo import MongoDBCustomerRepo
from db_manager.mongodb_helper import MongoDBHelper
from db_manager.postgresql_helper import PostgreSQLHelper

class CustomerModule:
    def __init__(self):
        # Constructor does not initialize the repo anymore.
        pass

    def add(self, db_helper, name, phone, address):
        # Create the appropriate repository inside the method
        if isinstance(db_helper, PostgreSQLHelper):
            customer_repo = PostgreSQLCustomerRepo(db_helper)
        elif isinstance(db_helper, MongoDBHelper):
            customer_repo = MongoDBCustomerRepo(db_helper)

        customer_repo.add_customer(name, phone, address)

    def update_info(self, db_helper, name, phone, address):
        # Create the appropriate repository inside the method
        customer_id = self.get_id(db_helper, phone)
        if isinstance(db_helper, PostgreSQLHelper):
            customer_repo = PostgreSQLCustomerRepo(db_helper)
        elif isinstance(db_helper, MongoDBHelper):
            customer_repo = MongoDBCustomerRepo(db_helper)

        customer_repo.update_customer(customer_id, name, phone, address)

    def get_id(self, db_helper, phone):
        # Create the appropriate repository inside the method
        if isinstance(db_helper, PostgreSQLHelper):
            customer_repo = PostgreSQLCustomerRepo(db_helper)
        elif isinstance(db_helper, MongoDBHelper):
            customer_repo = MongoDBCustomerRepo(db_helper)

        result = customer_repo.get_customer_id(phone)
        return result

    def get_info(self, db_helper, phone):
        # Create the appropriate repository inside the method
        customer_id = self.get_id(db_helper, phone)
        if isinstance(db_helper, PostgreSQLHelper):
            customer_repo = PostgreSQLCustomerRepo(db_helper)
        elif isinstance(db_helper, MongoDBHelper):
            customer_repo = MongoDBCustomerRepo(db_helper)

        result = customer_repo.get_customer_info(customer_id)
        return result

    def get_customer_orders(self, db_helper, phone):
        customer_id = self.get_id(db_helper, phone)
        # Create the appropriate repository inside the method
        if isinstance(db_helper, PostgreSQLHelper):
            customer_repo = PostgreSQLCustomerRepo(db_helper)
        elif isinstance(db_helper, MongoDBHelper):
            customer_repo = MongoDBCustomerRepo(db_helper)

        result = customer_repo.get_customer_orders(customer_id)
        return result

    def get_customer_rides(self, db_helper, phone):
        customer_id = self.get_id(db_helper, phone)
        # Create the appropriate repository inside the method
        if isinstance(db_helper, PostgreSQLHelper):
            customer_repo = PostgreSQLCustomerRepo(db_helper)
        elif isinstance(db_helper, MongoDBHelper):
            customer_repo = MongoDBCustomerRepo(db_helper)

        result = customer_repo.get_customer_rides(customer_id)
        return result

    def get_customer_payments(self, db_helper, phone):
        customer_id = self.get_id(db_helper, phone)
        # Create the appropriate repository inside the method
        if isinstance(db_helper, PostgreSQLHelper):
            customer_repo = PostgreSQLCustomerRepo(db_helper)
        elif isinstance(db_helper, MongoDBHelper):
            customer_repo = MongoDBCustomerRepo(db_helper)

        result = customer_repo.get_customer_payments(customer_id)
        return result
