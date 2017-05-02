import sqlite3

connection = sqlite3.connect('data.sqlite')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT ,username TEXT,password TEXT)";
cursor.execute(create_table)
connection.commit()
connection.close()
