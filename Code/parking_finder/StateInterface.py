import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=StateSubmit.py>")
print("<center>")
print("<table border=1>")
print("<caption><font size=7> State Registration </font></caption>")
print("<tr><td>enter state name</td><td><input type= text name=satname></td></tr>")
print("<tr><td>enter state image</td><td><input type= file name=satimg placeholder=uploadimg></td></tr>")
print("<tr><td>enter description</td><td><textarea name=satdesc rows=4 cols=30></textarea></td></tr>")
print("<tr><td><input type= submit ></td><td><input type= reset></td></tr>")
print("</table>")
print("</center>")
print("</form>")

print("<center>")
print("<table border=1>")
print("<tr><td>State ID</td><td>State Name</td><td>State Image</td><td>State Description</td><td>Status</td><td>update/delete</td></tr>")
sql="Select * from statereg";
display=a.execute(sql)
data=a.fetchall()
for i in data:
    print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td><img src=myimg/"+str(i[2])+" height=200 width=200></td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td><a href=StateUpDe.py?satid="+str(i[0])+">update/delete</a></td></tr>")

conn.commit()
print("</table>")
print("</center>")
print("</html>")
