import sqlite3

conn = sqlite3.connect("dabase.db")

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE cream (name text, price real, quantity integer)")
except:
    print("base already exists")

cream = [
    ('strawberry', 2.50, 100),
    ('chocolate', 2.60, 120),
    ('caramel', 2.70, 130),
]

cursor.executemany('INSERT INTO cream VALUES (?, ?, ?)', cream)

conn.commit()

conn.close()
