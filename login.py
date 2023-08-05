import sqlite3

## Creating a connection and a cursor
conn = sqlite3.connect("Users.db")
cur = conn.cursor()
## INSERT INTO Users('Junior', 'Didas', 'd.gasana@alustudent.com')
fname = input("Enter FirstName: ")
email = input("Enter Email: ") 
row = cur.execute(f'''
SELECT * FROM Users WHERE email = "{email}"
''')
data = row.fetchone()
if not data:
    print("The email is invalid")
else:
    if fname == data[0]:
        print("Login Successful")
    else:
        print("Invalid Password")
cur.close()

