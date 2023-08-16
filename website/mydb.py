import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user='admin',
    passwd='Sheikh@282898'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE mydb ")

print('db running successfully ')
