import os,sqlite3
db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
    pass

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002','Blus',74)")
cursor.execute(r"insert into user values ('A-003','Cindy',69)")
cursor.close()
conn.commit()
# cursor = cursor.execute('select * from user')
# values = cursor.fetchall()

def get_score_in(low,high):
    L=[]
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    #sqlite的筛选及升降序(asc,desc)
    cursor.execute('select name from user where ?<=score and score<=? order by score desc',(low,high))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    print(values)
get_score_in(60,100)