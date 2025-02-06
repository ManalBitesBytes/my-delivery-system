from utils.db_helper import DBHelper

def add_customer(name, phone, address):
    query = " INSERT INTO customers( name, phone, address) VALUES (%s, %s, %s)"
    db_helper = DBHelper()
    db_helper.set(query, (name, phone, address))

def update_customer(customer_id ,name, phone, address):
    query = " UPDATE customers SET name = %s, phone = %s, address = %s WHERE customer_id = %s"
    db_helper = DBHelper()
    db_helper.set(query, (customer_id , name, phone, address))

def get_customer_id(phone):
    query = "SELECT customer_id FROM customers WHERE phone = %s"
    db_helper = DBHelper()
    customer_id = db_helper.get(query, (phone,))
    return customer_id[0][0]

def get_customer_info(customer_id):
    query = "SELECT name, phone, address from customers WHERE customer_id = %s"
    db_helper = DBHelper()
    customer_info = db_helper.get(query, (customer_id,))
    return customer_info






