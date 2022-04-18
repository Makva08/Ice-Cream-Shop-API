from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

import sqlite3

class Item(Resource):
    TABLE_NAME = 'cream'

    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type = float,
                        required=True,
                        help = "please enter the price")

    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item

        return{'message': f'could not find {name} in the base'}, 404

    def post(self, name):
        if self.find_by_name(name):
            return {'message': f'could not find {name} in the base'}, 404

        data= (Item).parser.parse_args()

        item = {'name': name, 'price' : data['price']}
        try:
            Item.insert(item)
        except Exception as e:
            return {"message" : f"{e}"}
        else:
            return item


    def put(self, name):
        item = self.find_by_name(name)
        data= Item.parser.parse_args()
        new_item = {'name':name, "price":data['price'] }
        if item is None:
            Item.insert(new_item)
        else:
            Item.update(new_item)
        return {"item": new_item}

    def delete(self, name):
        conn = sqlite3.connect('dabase.db')
        cursor = conn.cursor()
        query = f'DELETE FROM {Item.TABLE_NAME} WHERE name=?'
        cursor.execute(query, (name,))

        conn.commit()
        conn.close()
        return {"message":"the item is deleted"}

    @classmethod
    def update(cls,item):
        conn = sqlite3.connect("dabase.db")
        cursor = conn.cursor()
        query = f'UPDATE {cls.TABLE_NAME} SET price=? WHERE name=?'
        cursor.execute(query, (item['price'], item['name']))

        conn.commit()
        conn.close()

    @classmethod
    def insert(cls, item):
        conn = sqlite3.connect('dabase.db')

        cursor = conn.cursor()
        query = f'INSERT INTO {cls.TABLE_NAME} VALUES (?,?,100)'

        cursor.execute(query, (item['name'], item['price']))

        conn.commit()
        conn.close()

    @classmethod
    def find_by_name(cls,name):
        conn = sqlite3.connect('dabase.db')
        cursor = conn.cursor()

        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        conn.close()

        if row:
            return {'item': {'name': row[0], 'price':row[1]}}


