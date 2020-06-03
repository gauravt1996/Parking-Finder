import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=ProviderLoginSubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7>Provider Registration </font></caption>")
print("<tr><td>Enter Name</td><td><input type= text name=pname></td></tr>")
print("<tr><td>Enter Mobile Number</td><td><input type=text name=pmob></td></tr>")
print("<tr><td>Enter Email</td><td><input type=email name=peid></td></tr>")
print("<tr><td>Enter Password</td><td><input type=password name=ppass show=*></td></tr>")
print("<tr><td>Re Enter Password</td><td><input type=password name=repass show=*></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")
print("</html>")
