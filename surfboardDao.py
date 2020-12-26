import mysql.connector
import dbConfig as cfg
#nextId=5

class SurfboardDao:
    db=""
    
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql["host"],
            username = cfg.mysql["username"],
            password = cfg.mysql["password"],
            database = cfg.mysql["database"]
        )

    def __init__(self):
        self.connectToDB() 
        #db=self.initConnectToDB()
        #db.close()

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()  

    def create(self, surfboard):
        #global nextId
        cursor = self.getCursor()
        sql = "insert into surfboards (ID, make, model, type, price) values (%s, %s,%s,%s,%s)"
        values = [
            surfboard["ID"],
            surfboard["make"],
            surfboard["model"],
            surfboard["type"],
            surfboard["price"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        lastRowId = cursor.lastrowid
        cursor.close()

        return lastRowId

    def getAll(self):
        cursor = self.getCursor()

        sql = "select * from surfboards"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray

        
    def findById(self, ID):
        cursor = self.getCursor()

        sql = "select * from surfboards where ID = %s"
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        surfboard = self.convertToDict(result)
        cursor.close() 
        return surfboard

    def update(self, surfboard):
        cursor = self.getCursor()

        sql = "update surfboards set make = %s, model = %s, type = %s, price = %s WHERE ID = %s"
        values = [
            surfboard["make"],
            surfboard["model"],
            surfboard["type"],
            surfboard["price"],
            surfboard["ID"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close() 
        return surfboard
        
    
    def delete(self, ID):
        cursor = self.getCursor()

        sql = "delete from surfboards where ID = %s"
        values = [ID]
        cursor.execute(sql, values)  
        self.db.commit()
        cursor.close()    
        return {}

    def convertToDict(self, result):
        colNames = ["ID", "make", "model", "type", "price"]
        surfboard = {}

        if result:
            for i, colName in enumerate(colNames):
                value = result[i]
                surfboard[colName] = value
        return surfboard
        

surfboardDao = SurfboardDao()