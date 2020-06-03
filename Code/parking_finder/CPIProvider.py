import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=CPSProvider.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7>Change Password</font></caption>")
print("<tr><td>Old Pass</td><td><input type=password name=op></td></tr>")
print("<tr><td>New Pass</td><td><input type=password name=np></td></tr>")
print("<tr><td>Confirm Pass</td><td><input type=password name=cp></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("<input type=hidden value="+str(peid)+" name=peid>")
print("</table>")
print("</center>")
print("</form>")
print("</html>")
