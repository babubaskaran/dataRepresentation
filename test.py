import mysql.connector
from mysql.connector import cursor

class DepartmenDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='datarepresentation'
        )
        print ("connection made")
