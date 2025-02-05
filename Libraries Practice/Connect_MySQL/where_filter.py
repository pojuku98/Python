import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fr1207ank",
  database="pylinksql"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)