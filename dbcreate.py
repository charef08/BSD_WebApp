import sqlite3



# MESSAGE CHAREFEDDINE : CREATED A DATABASE, BCUZ I WANTED TO SAVE THE COMMUNICATION HISTORY AND THEN RENDER IT ON THE FRONT BUT DIDN'T HAVE ENOUGH TIME


conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE sent (ip TEXT, msg TEXT, algo TEXT, key TEXT)')
print ("Table created successfully")
conn.execute('CREATE TABLE received (sender TEXT, msg TEXT, algo TEXT, key TEXT)')
print ("Table created successfully")
conn.close()