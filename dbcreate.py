import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE sent (ip TEXT, msg TEXT, algo TEXT, key TEXT)')
print ("Table created successfully")
conn.execute('CREATE TABLE received (sender TEXT, msg TEXT, algo TEXT, key TEXT)')
print ("Table created successfully")
conn.close()