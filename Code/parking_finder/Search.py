import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=Search1.py>")
res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
ueid=str(res.getvalue('ueid'))
print("<center>")
print("<table border=1>")
print("<tr><td><select name=satid>")
print("<option value=0>-Select State-</option>")
sq="select *from statereg"
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[1])+"</option>")
print("</select></td>")
conn.commit()
print("<td><select name=cityid>")
print("<option value=0>-Select City-</option>")
sq="select *from cityreg"
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[2])+"</option>")
print("</select></td>")
conn.commit()
print("<td><select name=aid>")
print("<option value=0>-Select Area-</option>")
sq="select *from areareg"
display=a.execute(sq)
data=a.fetchall()
for i in data:
      print("<option value="+str(i[0])+">"+str(i[2])+"</option>")
print("</select></td>")
conn.commit()
print("<td><input type=submit value=Search></td></tr>")
print("<tr><td colspan=4><iframe name=aa height=400 width=400></iframe></td></tr>")
print("<input type=hidden value="+str(peid)+" name=peid>")
print("<input type=hidden value="+str(ueid)+" name=ueid>")
print("</table>")
print("</center>")
print("</body>")
print("</form>")
print("</html>")

