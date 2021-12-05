import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'jirgi',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS book(
        ID INT NOT NULL AUTO_INCREMENT,
        book_name VARCHAR(255),
        address VARCHAR(255),
        phone INT,
        time INT,
        PRIMARY KEY(ID)
    )
    """
)
