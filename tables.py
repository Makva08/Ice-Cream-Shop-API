import sqlite3

connection = sqlite3.connect("dabase.db")

cursor = connection.cursor()

create_table='CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'

cursor.execute(create_table)

user = (1, "makashka", "aa34")

insert = ('INSERT INTO users VALUES (?, ?, ?)')

cursor.execute(insert, user)

connection.commit()

connection.close()