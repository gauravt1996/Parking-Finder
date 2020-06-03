import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")

res=cgi.FieldStorage()
satid=str(res.getvalue('satid'))
cityname=str(res.getvalue('cityname'))
cityimg=str(res.getvalue('cityimg'))
citydesc=str(res.getvalue('citydesc'))
sql="insert into cityreg(satid,cityname,cityimg,citydesc,status)values('"+str(satid)+"','"+str(cityname)+"','"+str(cityimg)+"','"+str(citydesc)+"','Not Deleted')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
