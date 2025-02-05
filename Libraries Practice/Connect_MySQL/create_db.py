import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fr1207ank"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE pylinksql")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)