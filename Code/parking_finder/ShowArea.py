import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<center>")
print("<table border=1>")
print("<tr><td>Area ID</td><td>City Name</td><td>Area Name</td><td>Area Zip Code</td><td>Show Parkings</td></tr>")
sql="Select * from cityreg c, areareg a where c.cityid=a.cityid and c.status='Not Deleted' and a.status='Not Deleted'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
       print("<tr><td>"+str(i[6])+"</td><td>"+str(i[2])+"</td><td>"+str(i[8])+"</td><td>"+str(i[9])+"</td><td><a href=Display1.py?aid="+str(i[6])+">Select Parking</a></td></tr>")
conn.commit()
print("</table>")
print("</center>")
print("</body>")
print("</html>")
