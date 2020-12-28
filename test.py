import mysql.connector
import dbconfig as cfg


class BookDao:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password =  '',
            database= 'datarepresentation'
        )
        print("connection made")
        
bookDao = BookDao()