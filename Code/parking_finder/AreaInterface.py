import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<form action=AreaSubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> Area Registration </font></caption>")
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
print("<tr><td>Enter Area Name</td><td><input type= text name=aname></td></tr>")
print("<tr><td>Enter Area Zip Code</td><td><input type= number name=azip ></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")

print("<center>")
print("<table border=1>")
print("<tr><td>Area ID</td><td>City Name</td><td>Area Name</td><td>Area Zip Code</td><td>update/delete</td><td>Status</td></tr>")
sql="Select * from cityreg c, areareg a where c.cityid=a.cityid"
display=a.execute(sql)
data=a.fetchall()
for i in data:
    print("<tr><td>"+str(i[6])+"</td><td>"+str(i[2])+"</td><td>"+str(i[8])+"</td><td>"+str(i[9])+"</td><td>"+str(i[10])+"</td><td><a href=AreaUpDe.py?aid="+str(i[6])+">update/delete</a></td></tr>")

conn.commit()
print("</table>")
print("</center>")
print("</body>")
print("</html>")
