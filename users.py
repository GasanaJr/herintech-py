import sqlite3

## Creating a connection and a cursor
conn = sqlite3.connect("Users.db")
cur = conn.cursor()

## Create a table
# CREATE TABLE Users(fname,lname,email)
cur.execute("DROP TABLE IF EXISTS Users")
cur.execute("CREATE TABLE Users(fname VARCHAR(128),lname VARCHAR(128),email VARCHAR(128))")

## INSERT INTO Users('Junior', 'Didas', 'd.gasana@alustudent.com')
fname = input("Enter FirstName: ")
lname = input("Enter LastName: ")
email = input("Enter Email: ") 
cur.execute('''
            INSERT INTO Users(fname,lname,email) VALUES (?,?,?)''',
            (fname,lname,email,))
conn.commit()
cur.close()

