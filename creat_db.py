import MySQLdb

mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="root",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS crs_flask_db")
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)