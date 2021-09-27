import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__),'car.db')

def db_connect(db_path = DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

def car_info(con,id,car_name,car_owner):
    car_sql = """
    INSERT INTO cars (id,car_name,car_owner) VALUES (?,?,?)"""
    cur = con.cursor()
    cur.execute(car_sql,(id,car_name,car_owner))

