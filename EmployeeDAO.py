import mysql.connector
from mysql.connector import cursor


class EmployeeDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='datarepresentation'
        )
        print ("connection made")

    def create(self, employee):
        cursor = self.db.cursor()
        sql = "insert into employees (EMPID, FirstName, LastName, DEPCODE, ADDR1, CITY, STATE, ZIP) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = [
            employee['EMPID'],
            employee['FirstName'],
            employee['LastName'],
            employee['DEPCODE'],
            employee['ADDR1'],
            employee['CITY'],
            employee['STATE'],
            employee['ZIP']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from employees'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, EMPID):
        cursor = self.db.cursor()
        sql = 'select * from employees where EMPID = %s'
        values = [ EMPID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, employee):
       cursor = self.db.cursor()
       sql = "update employees set FirstName = %s, LastName = %s, DEPCODE = %s, ADDR1 = %s, CITY = %s, STATE = %s, ZIP = %s where EMPID = %s"
       values = [
           employee['FirstName'],
           employee['LastName'],
           employee['DEPCODE'],
           employee['ADDR1'],
           employee['CITY'],
           employee['STATE'],
           employee['ZIP'], 
           employee['EMPID']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return employee

    def delete(self, EMPID):
       cursor = self.db.cursor()
       sql = 'delete from employees where EMPID = %s'
       values = [EMPID]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['EMPID','FirstName', 'LastName', 'DEPCODE', 'ADDR1', 'CITY', 'STATE', 'ZIP']
        employee = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                employee[colName] = value
        return employee

employeeDao = EmployeeDao()