import _mysql_connector
database = _mysql_connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS cliente")
print("Database created successfully")
