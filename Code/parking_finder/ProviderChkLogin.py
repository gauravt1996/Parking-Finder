import cgi
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=ProviderDisplay1.py>")
print("<body>")
print("<center>")

res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
ppass=str(res.getvalue('ppass'))
sql="Select * from preg where peid='"+str(peid)+"' and ppass='"+str(ppass)+"'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
      print("<table border=1>")
      print("<caption><font size=7> Provider Home </font></caption>")
      print("<tr><td>Header</td><td>Header</td></tr>")
      print("<tr><td><a href=ProviderDisplay1.py?peid="+str(peid)+" target=aa>Provider Display</a><br><a href=ProviderInterface.py?peid="+str(peid)+" target=aa>Parking Registration</a><br><a href=ProviderBankInterface.py?peid="+str(peid)+" target=aa>Parking Bank Registration</a><br><a href=CPIProvider.py?peid="+str(peid)+" target=aa>Change Password</a></td><td><iframe name=aa height=500 width=500></iframe></td></tr>")
      print("<tr><td>Footer</td><td>Footer</td></tr>")
      print("</table>")
print("</center>")
print("</body>")
print("</form>")
print("</html>")
      
      
