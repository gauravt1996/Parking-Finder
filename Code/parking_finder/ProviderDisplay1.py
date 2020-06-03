import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<center>")
print("<table border=1>")
res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
print("<tr><td>Provider ID</td><td>Provider Name</td><td>Provider Mobile</td><td>Provider Email</td><td>Provider Status</td></tr>")
sql="Select * from ppreg pp , preg p where pp.peid=p.peid and p.peid='"+str(peid)+"'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
    print("<tr><td>"+str(i[0])+"</td><td>"+str(i[13])+"</td><td>"+str(i[14])+"</td><td>"+str(i[11])+"</td><td>"+str(i[8])+"</td></tr>")

conn.commit()
print("</table>")
print("</center>")
print("</body>")
print("</html>")
