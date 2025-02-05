import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fr1207ank",
  database="pylinksql"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers LIMIT 5")

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)