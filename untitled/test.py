import sqlite3

# create the db and open the connection
connection = sqlite3.connect('data.sqlite')
cursor = connection.cursor()

# create table
create_table = "CREATE TABLE IF NOT EXISTS users(id INT,user TEXT,password TEXT)"
cursor.execute(create_table)

# insert a row
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

# insert many row
users = {
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
}
cursor.executemany(insert_query, users)

# query
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# close the connection
connection.commit()
connection.close()
