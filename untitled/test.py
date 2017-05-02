import sqlite3

connection = sqlite3.connect('data.sqlite')
cursor = connection.cursor()
create_table = "CREATE TABLE users(id INT,user TEXT,password TEXT)"

cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

connection.commit()
connection.close()
