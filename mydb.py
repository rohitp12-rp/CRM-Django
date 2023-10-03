import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = ''
)

#creating cursor object
cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE finco")

print("created database finco")

