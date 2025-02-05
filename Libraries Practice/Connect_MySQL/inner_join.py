import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="fr1207ank", 
    database="pylinksql"
)

mycursor = mydb.cursor()

sql_inner_join = """SELECT users.name AS user, 
                            products.name AS favorite
                    FROM users
                    INNER JOIN products 
                    ON users.fav = products.id"""
# mycursor.execute(sql_inner_join)

sql_left_join = """SELECT users.name AS user, 
                            products.name AS favorite
                    FROM users
                    LEFT JOIN products 
                    ON users.fav = products.id"""
mycursor.execute(sql_left_join)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
