from surfboardDao import surfboardDao

surfboard1 = {
    "ID" : 2,
    "make" : "Firewire",
    "model" : "The Gem: 10'0",
    "type" : "Longboard",
    "price" : 1000
}

surfboard2 = {
    "ID" : 2,
    "make" : "Firewire",
    "model" : "Long",
    "type" : "Longboard",
    "price" : 1000
}


#Create new value in sql db
#returnValue = surfboardDao.create(surfboard2)
#print(returnValue)

#Get all values in surfboards
returnValue = surfboardDao.getAll()
print(returnValue)

# Find by ID 2
returnValue = surfboardDao.findById(surfboard2["ID"])
print("Find by ID initial", returnValue)

# Update surfboard 2
returnValue = surfboardDao.update(surfboard2)
print("Updated surfboard: ", returnValue)

# Find by ID 2
returnValue = surfboardDao.findById(surfboard2["ID"])
print("Find by ID updated", returnValue)

# Delete surfboard 2 id
returnValue = surfboardDao.delete(surfboard2["ID"])
print(returnValue)

#Get all values in surfboards
returnValue = surfboardDao.getAll()
print("Final DB values: ", returnValue)

print("ok")