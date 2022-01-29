import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT * from CONTACTS")
for row in cursor:
   print ("ID = " + str(row[0]))
   print ("NAME = " + row[1])
   print("AGE = " + str(row[2]))
   print ("ADDRESS = " + str(row[3]) + "\n")

print ("Operation done successfully")
conn.close()