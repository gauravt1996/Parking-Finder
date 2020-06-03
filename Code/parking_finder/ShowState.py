import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<center>")
print("<table border=1>")
print("<tr><td>State ID</td><td>State Name</td><td>State Image</td><td>State Description</td><td>Show City</td></tr>")
sql="Select * from statereg where status='Not Deleted'";
display=a.execute(sql)
data=a.fetchall()
for i in data:
    print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td><img src=myimg/"+str(i[2])+" height=200 width=200></td><td>"+str(i[3])+"</td><td><a href=ShowCity.py?satid="+str(i[0])+">Select City</a></td></tr>")

conn.commit()
print("</table>")
print("</center>")
print("</html>")
