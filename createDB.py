import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lahinch1991"
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
)

cursor = db.cursor()

cursor.execute("create DATABASE datarepresentation")


# Possibly not needed. Here for now