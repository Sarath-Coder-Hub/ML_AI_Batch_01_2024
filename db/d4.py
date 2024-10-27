import sqlite3
conn = sqlite3.connect('test.db')
query = 'SELECT * FROM emp WHERE  id<3'

cursor = conn.execute(query)
#print(cursor)
for row in cursor:
    print(row[0], row[1], row[2])
conn.close()
