import pymysql 
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")

res=cgi.FieldStorage()
cityid=str(res.getvalue('cityid'))
aname=str(res.getvalue('aname'))
azip=str(res.getvalue('azip'))
sql="insert into areareg(cityid,aname,azip,status)values('"+str(cityid)+"','"+str(aname)+"','"+str(azip)+"','Not Deleted')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
