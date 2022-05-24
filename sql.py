import sqlite3
conn = sqlite3.connect('b.db')
c = conn.cursor()
c.execute("""CREATE TABLE c (a text, b text)""")
c.execute("""INSERT INTO c VALUES ('a','b')""")
c.execute("""SELECT * FROM c""")
print(c.fetchall())
conn.commit()
conn.close()
