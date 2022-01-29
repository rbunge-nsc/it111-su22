
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO CONTACTS (ID,NAME,AGE,ADDRESS) \
      VALUES (10, 'Polly', 32, 'Seattle')");

conn.execute('INSERT INTO CONTACTS (ID,NAME,AGE,ADDRESS) \
      VALUES (11, \'Roger\', 28, \'Bainbridge\')');


conn.commit()
print("Records created successfully")
conn.close()
