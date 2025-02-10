import pandas as pd

class RideRepo:
    def __init__(self, db_helper):
        self.db_helper = db_helper

    def add(self, customer_id, pickup_location, dropoff_location):
        query = "INSERT INTO rides (customer_id, pick_up_location, drop_off_location) VALUES (%s, %s, %s)"
        self.db_helper.set(query, (customer_id, pickup_location, dropoff_location))

    def update_status(self, ride_id, status):
        query = "UPDATE rides SET status = %s WHERE ride_id = %s"
        self.db_helper.set(query, (status, ride_id))

    def show_info(self, ride_id):
        query = "SELECT customer_id, status, pick_up_location, drop_off_location FROM rides where ride_id = %s"
        result = self.db_helper.get(query, (ride_id,))
        return  pd.DataFrame(result, columns=['customer_id', 'status', 'pick_up_location', 'drop_off_location'])