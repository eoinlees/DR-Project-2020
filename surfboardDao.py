import mysql.connector

class SurfboardDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
          host = "localhost",
          username = 'root',
          password = 'Lahinch1991',
          database = 'datarepresentation'
        )
        #print("Connection made")

    def create(self, surfboard):
        cursor = self.db.cursor()
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
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from surfboards"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

        
    def findById(self, ID):
        cursor = self.db.cursor()
        sql = "select * from surfboards where ID = %s"
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        
        return self.convertToDict(result)

    def update(self, surfboard):
        cursor = self.db.cursor()
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
        return surfboard
        
    
    def delete(self, ID):
        cursor = self.db.cursor()
        sql = "delete from surfboards where ID = %s"
        values = [ID]
        cursor.execute(sql, values)  
        self.db.commit()    
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