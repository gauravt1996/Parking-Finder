import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

res=cgi.FieldStorage()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=FPSUser.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> Forget Password</font></caption>")
print("<tr><td>Enter Email</td><td><input type=text name=ueid></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")
print("</html>")
