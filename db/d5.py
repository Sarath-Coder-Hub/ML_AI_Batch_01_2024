import sqlite3
conn = sqlite3.connect('test.db')
query = "UPDATE emp SET phone='111222' WHERE id=1"
conn.execute(query)

conn.commit()
conn.close()