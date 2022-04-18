import sqlite3

class ItemModel:
    TABLE_NAME="cream"
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name":self.name, "price":self.price}

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('dabase.db')
        cursor = conn.cursor()

        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        conn.close()

        if row:
            #return {'item': {'name': row[0], 'price': row[1]}}
            return cls(name, row[1])

    @classmethod
    def insert(cls, item):
        conn = sqlite3.connect('dabase.db')

        cursor = conn.cursor()
        query = f'INSERT INTO {cls.TABLE_NAME} VALUES (?,?,100)'

        cursor.execute(query, (item['name'], item['price']))

        conn.commit()
        conn.close()


    @classmethod
    def update(cls, item):
        conn = sqlite3.connect("dabase.db")
        cursor = conn.cursor()
        query = f'UPDATE {cls.TABLE_NAME} SET price=? WHERE name=?'
        cursor.execute(query, (item['price'], item['name']))

        conn.commit()
        conn.close()

    @classmethod
    def delete(cls,name):
        conn = sqlite3.connect('dabase.db')
        cursor = conn.cursor()
        query = f'DELETE FROM {ItemModel.TABLE_NAME} WHERE name=?'
        cursor.execute(query, (name,))

        conn.commit()
        conn.close()


