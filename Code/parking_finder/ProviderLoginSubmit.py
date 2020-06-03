import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
pname=str(res.getvalue('pname'))
pmob=str(res.getvalue('pmob'))
peid=str(res.getvalue('peid'))
ppass=str(res.getvalue('ppass'))
sql="insert into preg(pname,pmob,peid,ppass)values('"+str(pname)+"','"+str(pmob)+"','"+str(peid)+"','"+str(ppass)+"')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
