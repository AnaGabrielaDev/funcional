import mysql.connector

def mydb():
    return mysql.connector.connect(
        host="host.docker.internal",
        user="ana",
        password="gabriela",
        database="functional"
    )

conn = mydb()
mycursor = conn.cursor()

createDatabase = lambda tableName, properties: mycursor.execute("CREATE TABLE IF NOT EXISTS " + tableName + " (" + properties + ")")
addRecord = lambda tableName, columns, values: mycursor.execute("INSERT INTO " + tableName + " (" + columns + ") VALUES (" + values + ")")
queryRecord = lambda tableName, condition: mycursor.execute("SELECT * FROM " + tableName + " WHERE " + condition)
deleteRecord = lambda tableName, condition: mycursor.execute("DELETE FROM " + tableName + " WHERE " + condition)

tables = lambda: [
        {
            "tableName": "users",
            "properties": "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255), id_console INT"
        },
        {
            "tableName": "videogames",
            "properties": "id_console INT, name VARCHAR(255), id_company INT, release_date DATE"
        },
        {
            "tableName": "games",
            "properties": "id_game INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), genre VARCHAR(255), release_date DATE, id_console INT"
        },
        {
            "tableName": "companies",
            "properties": "id_company INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), country VARCHAR(255)"
        }
]

def create_tables(tables):
    return lambda: [createDatabase(table["tableName"], table["properties"]) for table in tables]

def create_tables(tables):
    return [createDatabase(table["tableName"], table["properties"]) for table in tables]

create = lambda : create_tables(tables())

add = lambda : addRecord("users", "id, name, country", "1, 'Ana Gabriela', 'BR'")
search = lambda : queryRecord("users", "id = 1")
delete = lambda : deleteRecord("users", "id = 1")

q3 = lambda: (create(), search())
