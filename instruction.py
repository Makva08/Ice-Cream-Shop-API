import sqlite3
conn=sqlite3.connect("dabase.db")
cursor=conn.cursor()

def names():
    results = cursor.execute("SELECT * FROM cream")
    return results

def price():
    name = input("Name of the item: ")
    param = (name,)
    result=cursor.execute("SELECT * FROM cream where name=?", param)
    return result

print("Hello")

result=names()

for row in result:
    print(row[0])

while True:
    result=price()
    print(list(result)[0][1])

#for result in results:
#    print(f"{result[0]} - {result[1]} GEL")
