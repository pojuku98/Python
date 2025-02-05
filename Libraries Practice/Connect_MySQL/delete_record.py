import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fr1207ank",
  database="pylinksql"
)

mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")