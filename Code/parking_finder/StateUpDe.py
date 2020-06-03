import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")
print("<center>")
print("<form action=StateUpDe1.py>")
print("<table border=1>")
reg=cgi.FieldStorage()
satid=reg.getvalue('satid')
sql="select * from statereg where satid="+str(satid)
a.execute(sql)
data=a.fetchall()
for i in data:
    
    print("<tr><td>State ID</td><td><input type=text name=satid value="+str(i[0])+" readonly=true></td></tr>")
    print("<tr><td>State Name</td><td><input type=text name=satname value="+str(i[1])+"></td></tr>")
    print("<tr><td>State Image</td><td><img src=myimg/"+str(i[2])+"height=200 width=200><input type=file ></td></tr>")
    print("<tr><td>State Description</td><td><textarea rows=5 cols=30 name=satdesc>"+str(i[3])+"</textarea></td></tr>")
    print("<tr><td><input type=submit value=Update name=btn></td><td><input type=submit value=Delete name=btn></td></tr>")

print("</table>")
print("</form>")
print("</center>")
conn.commit()
print("</html>")
