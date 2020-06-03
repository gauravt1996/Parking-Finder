import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
print("<form action=ProviderSubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> Sign UP</font></caption>")
print("<tr><td>State</td><td><select name=satid>")
print("<option>-Select State-</option>")
sq="select *from statereg where status='Not Deleted'"
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[1])+"</option>")
print("</select></td></tr>")


print("<tr><td>City</td><td><select name=cityid>")
print("<option>-Select City-</option>")
sq="select *from cityreg where status='Not Deleted'"
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[2])+"</option>")
print("</select></td></tr>")

print("<tr><td>Area</td><td><select name=aid>")
print("<option>-Select Area-</option>")
sq="select * from areareg where status='Not Deleted'"
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[2])+"</option>")
print("</select></td></tr>")
print("<tr><td>Address</td><td><input type= textarea name=ppadd rows=8 cols=6></td></tr>")
print("<tr><td>Zip Code</td><td><input type= number name=ppzip></td></tr>")
print("<tr><td>Aadhar Number</td><td><input type=text name=ppaadhar></td></tr>")
print("<tr><td>Aadhar Image</td><td><input type= file name=ppaadharimg placeholder=uploadimg></td></tr>")
print("<tr><td>Spot Image</td><td><input type= file name=ppspotimg placeholder=uploadimg></td></tr>")
print("<tr><td>Broad View Location Image</td><td><input type= file name=ppbroadimg placeholder=uploadimg></td></tr>")
print("<tr><td>Number of Vehicles can be Parked</td><td><input type=number name=ppvnum></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("<input type=hidden value="+str(peid)+" name=peid >")
print("</table>")
print("</center>")
print("</form>")
print("</html>")
