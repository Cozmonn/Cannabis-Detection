import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", password="", database="login_dj")

mycursor =mydb.cursor()
mycursor.execute("show databases")
for db in mycursor:
    print(db)