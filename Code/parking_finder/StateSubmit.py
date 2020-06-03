import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
satname=str(res.getvalue('satname'))
satimg=str(res.getvalue('satimg'))
satdesc=str(res.getvalue('satdesc'))
sql="insert into statereg(satname,satimg,satdesc,status)values('"+satname+"','"+satimg+"','"+satdesc+"','Not Deleted')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
