import sqlite3
from db_utils_cars import db_connect,car_info

con = db_connect()
cur = con.cursor()

'''
CREATING A TABLE CAR
'''

car_sql = """
CREATE TABLE cars(
    id integer PRIMARY KEY,
    car_name char(20) NOT NULL,
    car_owner char(20) NOT NULL)"""
cur.execute(car_sql)


'''
Loading DATA via function'''

try:
    car1 = car_info(con, 1, "Mercedes-Benz S", "Jose Homes")
    car2 = car_info(con, 2, "Rolls Royce Ghost Series II", "Edward Right")
    car3 = car_info(con, 3, "Ferrari 458 ", "Oliver Hangrid")
    car5 = car_info(con, 5, "Ferrari California", "Jane Preston")
    car6 = car_info(con, 6, "Audi R8 ", "Lucas North")
    car7 = car_info(con, 7, "Audi Skysphere", "Abhijit Madhu")
    car8 = car_info(con, 8, "TESLA MODEL 3", "Nole Ksum")
    car9 = car_info(con, 9, "Ford GT", "Ken Miles")
    car10 = car_info(con, 10, "Land Rover Defender", "Arthur West")
    con.commit()
except:
    con.rollback()
    raise  RuntimeError("Sorry an Error Occured!")


'''
Printing the TABLE
'''

cur.execute("SELECT id,car_name,car_owner FROM cars")
formatted_result = [f"{id:<10}{car_name:<35}{car_owner:<35}" for id, car_name, car_owner in cur.fetchall()]
id,car_name,car_owner = "SL.no","CAR NAME" , "CAR OWNER"
print('\n'.join([f"{id:<10}{car_name:<35}{car_owner:<35}"] + formatted_result))