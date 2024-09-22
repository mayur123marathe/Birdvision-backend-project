import sqlite3

conn = sqlite3.connect('products.sqlite')

cursor = conn.cursor()
sql_query = """ CREATE TABLE product ( 
    id integer PRIMARY KEY,
    price text NOT NULL,
    title text NOT NULL


)"""
cursor.execute(sql_query)