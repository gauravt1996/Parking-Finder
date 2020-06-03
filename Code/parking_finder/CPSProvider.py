import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")

res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
op=str(res.getvalue('op'))
np=str(res.getvalue('np'))
cp=str(res.getvalue('cp'))
if np == cp:
    sql="update preg set ppass='"+np+"' where peid='"+peid+"' and ppass='"+op+"'"
    display=a.execute(sql)
else :
    print("failed")
conn.commit()
