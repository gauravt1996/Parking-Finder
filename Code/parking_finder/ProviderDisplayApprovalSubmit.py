import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")

res=cgi.FieldStorage()
ppid=str(res.getvalue('ppid'))
message=str(res.getvalue('message'))
sql="insert into conversation(ppid,message)values('"+str(ppid)+"','"+str(message)+"')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
