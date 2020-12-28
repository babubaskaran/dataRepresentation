import mysql.connector
from mysql.connector import cursor

class BookDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'datarepresentation'
        )
        #print("connection made")

    def create(self, book):
        cursor = self.db.cursor()
        sql = "insert into books (ISBN, title, author, price) values (%s,%s,%s,%s)"
        values = [
            book['ISBN'],
            book['title'],
            book['author'],
            book['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid     
bookDao = BookDao()