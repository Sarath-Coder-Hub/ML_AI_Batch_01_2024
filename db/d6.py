import sqlite3
conn = sqlite3.connect('test.db')
query = "DELETE FROM emp  WHERE id=2"
conn.execute(query)
conn.commit()
conn.close()