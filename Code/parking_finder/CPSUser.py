import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")

res=cgi.FieldStorage()
ueid=str(res.getvalue('ueid'))
op=str(res.getvalue('op'))
np=str(res.getvalue('np'))
cp=str(res.getvalue('cp'))
if np == cp:
    sql="update userreg set upass='"+np+"' where ueid='"+ueid+"'and upass='"+op+"'"
    display=a.execute(sql)
    print(sql)
else:
    print("failed")
conn.commit()
