import mysql.connector
from mysql.connector import cursor


class DepartmenDao:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='datarepresentation'
        )
        print("connection made")

    def create2Dept(self, department):
        cursor = self.db.cursor()
        sql = "insert into department (`DeptName`, `MGR_Name`) values (%s,%s)"
        values = [
            # department['DEPCODE'],
            department['DeptName'],
            department['MGR_Name']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAllDept(self):
        cursor = self.db.cursor()
        sql = 'select * from department'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById2Dept(self, DEPCODE):
        cursor = self.db.cursor()
        sql = 'select * from department where DEPCODE = %s'
        values = [DEPCODE]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def updateDept(self, department):
        cursor = self.db.cursor()
        sql = "update department set DeptName = %s, MGR_Name = %s where DEPCODE = %s"
        values = [
            department['DeptName'],
            department['MGR_Name'],
            department['DEPCODE']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return department

    def deleteDept(self, DEPCODE):
        cursor = self.db.cursor()
        sql = 'delete from department where DEPCODE = %s'
        values = [DEPCODE]
        cursor.execute(sql, values)

        return {}

    def convertToDict(self, result):
        colnames = ['DEPCODE', 'DeptName', 'MGR_Name']
        department = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                department[colName] = value
        return department


departmenDao = DepartmenDao()