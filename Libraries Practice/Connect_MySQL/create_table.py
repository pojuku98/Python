import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fr1207ank",
  database="pylinksql"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)