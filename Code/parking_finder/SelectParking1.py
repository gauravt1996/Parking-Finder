import cgi
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<form action=BookingConfirmation.py>")
res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
ppid=str(res.getvalue('ppid'))
ueid=str(res.getvalue('ueid'))
print("<center>")
print("<table border=1>")
sql="Select * from bankreg where peid='"+str(peid)+"'"
display=a.execute(sql)
data=a.fetchall()
conn.commit()

print("<tr><td>Account Number</td><td>Bank</td><td>IFSC</td></tr>")
for i in data:
    print("<tr><td><input type=text value="+str(i[1])+" readonly=true></td><td><input type=text value="+str(i[2])+" readonly=true></td><td><input type=text value="+str(i[3])+" readonly=true></td></tr>")
conn.commit()
print("</table>")
print("<table border=1>")
print("<tr><td>Account Number</td><td><input type= text name=accno></td></tr>")
print("<tr><td>Password</td><td><input type= password name=pass></td></tr>")
print("<input type=hidden name=peid value="+str(peid)+">")
print("<input type=hidden name=ueid value="+str(ueid)+">")
print("<input type=hidden name=ppid value="+str(ppid)+">")
print("<tr><td><input type=submit value=Login></td></tr>")
print("</table>")
print("</center>")
print("</body>")
print("</form>")
print("</html>")
