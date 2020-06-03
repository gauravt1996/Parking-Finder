import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<form action=CitySubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> City Registration </font></caption>")
print("<tr><td>State</td><td><select name=satid>")
print("<option>-Select State-</option>")
sq="select *from statereg where status='Not Deleted'"
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[1])+"</option>")
print("</select></td></tr>")
print("<tr><td>Enter City Name</td><td><input type= text name=cityname></td></tr>")
print("<tr><td>Enter City Image</td><td><input type= file name=cityimg placeholder=uploadimg></td></tr>")
print("<tr><td>Enter Description</td><td><textarea name=citydesc rows=4 cols=30></textarea></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")

print("<center>")
print("<table border=1>")
print("<tr><td>City ID</td><td>State Name</td><td>City Name</td><td>City Image</td><td>City Description</td><td>Status</td><td>update/delete</td></tr>")
sql="Select * from statereg s , cityreg c where s.satid=c.satid"
display=a.execute(sql)
data=a.fetchall()
for i in data:
    print("<tr><td>"+str(i[5])+"</td><td>"+str(i[1])+"</td><td>"+str(i[7])+"</td><td><img src=myimg/"+str(i[8])+" height=100 width=100></td><td>"+str(i[9])+"</td><td>"+str(i[10])+"</td><td><a href=CityUpDe.py?cityid="+str(i[5])+">update/delete</a></td></tr>")

conn.commit()
print("</table>")
print("</center>")
print("</body>")
print("</html>")
