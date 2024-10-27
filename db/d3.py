import sqlite3
conn = sqlite3.connect('test.db')
query1 = "INSERT INTO emp(id, name, phone) VALUES (1, 'Abcd', '123456')"
query2 = "INSERT INTO emp(id, name, phone) VALUES (2, 'Xyz', '000000')"

conn.execute(query1)
conn.execute(query2)
print('Record inserted')
conn.commit()
conn.close()

