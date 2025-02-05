import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fr1207ank",
    database="pylinksql"
)

mycursor = mydb.cursor()

"""
sql_creat_table_users = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)"

mycursor.execute(sql_creat_table_users)
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
"""
    
sql_insert_into_users = """INSERT INTO users (name, fav) 
                                        VALUES (%s, %s)"""
sql_users_values = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah', 0),
    ('Michael', 0)
]

mycursor.executemany(sql_insert_into_users, sql_users_values)
# 修改資料要commit才會存進去
mydb.commit()
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

