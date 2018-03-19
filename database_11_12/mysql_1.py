import pymysql
conn = pymysql.connect(
    host = 'localhost',
    port = 3307,
    user = 'dlh',
    passwd = '123456',
    db = 'python',
)
cur = conn.cursor()
# cur.execute("create table movie(name varchar(20),url varchar(50))")
# cur.execute("drop table movie")
cur.close()
conn.commit()
conn.close()