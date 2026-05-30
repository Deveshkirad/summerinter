import sqlite3

conn = sqlite3.connect('example.db')
sql='''insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)'''
c = conn.cursor()

c.execute(sql)

conn.commit()
conn.close()