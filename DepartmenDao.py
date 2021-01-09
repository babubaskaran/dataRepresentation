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

    def create(self, departmen):
        cursor = self.db.cursor()
        sql = "insert into department (DEPCODE, DEPTNAME, MGR_Name) values (%s,%s,%s)"
        values = [
            departmen['DEPCODE'],
            departmen['DEPTNAME'],
            departmen['MGR_Name']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from department'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, DEPCODE):
        cursor = self.db.cursor()
        sql = 'select * from department where DEPCODE = %s'
        values = [ DEPCODE ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, departmen):
       cursor = self.db.cursor()
       sql = "update department set DEPTNAME = %s, MGR_Name = %s where DEPCODE = %s"
       values = [
           departmen['DEPTNAME'],
           departmen['MGR_Name'],
           departmen['DEPCODE'],
        ]
       cursor.execute(sql, values)
       self.db.commit()
       return departmen

    def delete(self, DEPCODE):
       cursor = self.db.cursor()
       sql = 'delete from department where DEPCODE = %s'
       values = [DEPCODE]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['DEPCODE','DEPTNAME', 'MGR_Name']
        departmen = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                departmen[colName] = value
        return departmen

departmenDao = DepartmenDao()