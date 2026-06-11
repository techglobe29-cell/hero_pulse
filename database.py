import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pxt49@NT",
    database="maintenance_system"
)

cursor = conn.cursor()

print("Connected Successfully")