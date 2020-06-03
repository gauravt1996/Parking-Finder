import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
print("<form action=ProviderBankSubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> Bank Information</font></caption>")
print("<tr><td>Account Number</td><td><input type= text name=pbaccno></td></tr>")
print("<tr><td>Bank Name</td><td><input type=text name=pbname></td></tr>")
print("<tr><td>IFSC</td><td><input type=text name=pbifsc></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("<input type=hidden value="+str(peid)+" name=peid >")
print("</table>")
print("</center>")
print("</form>")
print("</html>")
