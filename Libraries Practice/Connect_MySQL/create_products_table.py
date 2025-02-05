import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fr1207ank",
    database="pylinksql"
)

mycursor = mydb.cursor()

"""
sql_create_table_products = "CREATE TABLE products (id INT, name VARCHAR(255))"

mycursor.execute(sql_create_table_products)
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
"""
    
sql_insert_into_products = "INSERT INTO products (id, name) VALUES (%s, %s)"
sql_products_values = [
    (154, 'Chocolate Heaven'), 
    (155, 'Tasty Lemons'), 
    (156, 'Vanilla Dreams')
]
mycursor.executemany(sql_insert_into_products, sql_products_values)
# 修改資料要commit才會存進去
mydb.commit()
mycursor.execute("SELECT * FROM products")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)