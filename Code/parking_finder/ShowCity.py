import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<center>")
print("<table border=1>")
print("<tr><td>City ID</td><td>State Name</td><td>City Name</td><td>City Image</td><td>City Description</td><td>Show Area</td></tr>")
sql="Select * from statereg s , cityreg c where s.satid=c.satid and s.status='Not Deleted' and c.status='Not Deleted'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
    print("<tr><td>"+str(i[5])+"</td><td>"+str(i[1])+"</td><td>"+str(i[7])+"</td><td><img src=myimg/"+str(i[8])+" height=100 width=100></td><td>"+str(i[9])+"</td><td><a href=ShowArea.py?cityid="+str(i[5])+">Show Area</a></td></tr>")

conn.commit()
print("</table>")
print("</center>")
print("</html>")
