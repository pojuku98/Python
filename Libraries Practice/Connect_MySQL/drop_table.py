import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fr1207ank",
  database="pylinksql"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE customers"

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)