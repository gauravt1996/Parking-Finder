import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<center>")
print("<form action=CityUpDe1.py>")
print("<table border=1>")
reg=cgi.FieldStorage()
cityid=reg.getvalue('cityid')
sql="select * from cityreg where cityid="+str(cityid)
a.execute(sql)
data=a.fetchall()
for i in data:
      satid=str(i[1])
      cityid=str(i[0])
      cityname=str(i[2])
      cityimg=str(i[3])
      citydesc=str(i[4])


print("<tr><td>State</td><td><select name=satid>")
sq="select *from statereg where satid="+str(satid)
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[1])+"</option>");
conn.commit()
sq="select *from statereg where satid<>"+str(satid)
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[1])+"</option>");
print("</select></td></tr>")
conn.commit()

print("<tr><td>City ID</td><td><input type=text name=cityid value="+cityid+" readonly=true></td></tr>")
print("<tr><td>City Name</td><td><input type=text name=cityname value="+cityname+"></td></tr>")
print("<tr><td>City Image</td><td><img src=myimg/"+cityimg+"height=100 width=100><input type=file name=cityimg></td></tr>")
print("<tr><td>City Description</td><td><textarea rows=5 cols=30 name=citydesc>"+citydesc+"</textarea></td></tr>")
print("<tr><td><input type=submit value=Update name=btn></td><td><input type=submit value=Delete name=btn></td></tr>")
print("</table>")
print("</form>")
print("</center>")
conn.commit()
print("</body>")
print("</html>")
