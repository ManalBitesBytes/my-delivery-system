from repositories.ride_repo import RideRepo

class RideModule():
    def __init__(self, db_helper):
        self.ride_repo = RideRepo(db_helper)


    def add(self, customer_id, pickup_location, dropoff_location):
        self.ride_repo.add(customer_id, pickup_location, dropoff_location)



    def update_status(self, ride_id, status):
         self.ride_repo.update_status(ride_id, status)

    def assign(self):
        pass

    def complete(self):
        pass

    def show_info(self, ride_id):
        result = self.ride_repo.show_info(ride_id)
        return result

