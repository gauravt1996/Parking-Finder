import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")

res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
pbaccno=str(res.getvalue('pbaccno'))
pbname=str(res.getvalue('pbname'))
pbifsc=str(res.getvalue('pbifsc'))
sql="insert into bankreg(peid,pbaccno,pbname,pbifsc)values('"+str(peid)+"','"+str(pbaccno)+"','"+str(pbname)+"','"+str(pbifsc)+"')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
