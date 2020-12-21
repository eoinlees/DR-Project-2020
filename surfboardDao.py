import mysql.connector
import dbConfig as cfg
#nextId=5

class SurfboardDao:

    def initConnectToDB(self):
        db = mysql.connector.connect(
            host = cfg.mysql["host"],
            username = cfg.mysql["username"],
            password = cfg.mysql["password"],
            database = cfg.mysql["database"],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    #def connectToDB(self):
    #    self.db = mysql.connector.connect(
    #      host = cfg.mysql["host"],
    #      username = cfg.mysql["username"],
    #      password = cfg.mysql["password"],
    #      database = cfg.mysql["database"]
    #    )

    def __init__(self): 
        db=self.initConnectToDB()
        db.close()
   
    #def getCursor(self):
    #    if not self.db.is_connected():
    #        self.connectToDB()
    #    return self.db.cursor()  

    def create(self, surfboard):
        #global nextId
        db = self.getConnection()
        cursor = db.cursor()
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
        db.close()

        return lastRowId

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from surfboards"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

        
    def findById(self, ID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from surfboards where ID = %s"
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        surfboard = self.convertToDict(result)
        db.close()
        return surfboard

    def update(self, surfboard):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "UPDATE surfboards set make = %s, model = %s, type = %s, price = %s WHERE ID = %s"
        values = [
            surfboard["make"],
            surfboard["model"],
            surfboard["type"],
            surfboard["price"],
            surfboard["ID"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        db.close()
        return surfboard
        
    
    def delete(self, ID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "delete from surfboards where ID = %s"
        values = [ID]
        cursor.execute(sql, values)  
        self.db.commit()
        db.close()    
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