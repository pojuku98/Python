import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fr1207ank",
  database="pylinksql"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

mycursor.execute("SELECT name, address FROM customers")

"""
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
"""

myresult = mycursor.fetchone()
print(myresult)