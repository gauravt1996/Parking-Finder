import cgi
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<center>")

res=cgi.FieldStorage()
ueid=str(res.getvalue('ueid'))
upass=str(res.getvalue('upass'))
sql="Select * from userreg where ueid='"+str(ueid)+"' and upass='"+str(upass)+"'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
      print("<table border=1>")
      print("<caption><font size=7> User Home </font></caption>")
      print("<tr><td>Header</td><td>Header</td></tr>")
      print("<tr><td><a href=Search.py?ueid="+str(ueid)+" target=aa>Select Parking</a><br><a href=CPIUser.py?ueid="+str(ueid)+" target=aa>Change Password</a></td><td><iframe name=aa height=500 width=500></iframe></td></tr>")
      print("<tr><td>Footer</td><td>Footer</td></tr>")
      print("</table>")
print("</center>")
print("</body>")
print("</form>")
print("</html>")
      
      
