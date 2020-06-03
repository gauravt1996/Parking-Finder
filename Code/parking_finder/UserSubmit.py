import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")

res=cgi.FieldStorage()
uname=str(res.getvalue('uname'))
umob=str(res.getvalue('umob'))
ueid=str(res.getvalue('ueid'))
uaadhar=str(res.getvalue('uaadhar'))
uaadharimg=str(res.getvalue('uaadharimg'))
upass=str(res.getvalue('upass'))
sql="insert into userreg(uname,umob,ueid,uaadhar,uaadharimg,upass)values('"+str(uname)+"','"+str(umob)+"','"+str(ueid)+"','"+str(uaadhar)+"','"+str(uaadharimg)+"','"+str(upass)+"')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
