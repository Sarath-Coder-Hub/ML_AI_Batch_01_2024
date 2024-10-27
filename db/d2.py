import sqlite3
conn =sqlite3.connect('test.db')
query = '''
CREATE TABLE IF NOT EXISTS emp(
    id INT,
    name TEXT,
    phone TEXT
)
'''
conn.execute(query)
print('Table Created')
conn.close()