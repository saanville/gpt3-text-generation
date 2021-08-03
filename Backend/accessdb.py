import sqlite3

conn = sqlite3.connect('res.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

cursor = conn.execute("SELECT * FROM RESPONSES")
    

for row in cursor:
    print("ID = ", row[0])
    print("ENTRY = ", row[1])
    print("RESPONSE = ", row[2], "\n")
conn.close()
