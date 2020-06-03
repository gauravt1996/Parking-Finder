import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<form action=ProviderDisplayApproval.py>")
print("<center>")
print("<table border=1>")
res=cgi.FieldStorage()
status=str(res.getvalue('ppstatus'))
print("<tr><td>Provider ID</td><td>Provider Name</td><td>Provider Mobile</td><td>Provider Email</td><td>Provider Status</td></tr>")
sql="Select pp.ppid,p.pname,p.pmob,p.peid,pp.ppstatus from preg p,ppreg pp where pp.peid=p.peid and pp.ppstatus='"+str(status)+"' order by pp.ppid asc"
display=a.execute(sql)
data=a.fetchall()
for i in data:
    print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td><a href=ProviderDisplayApproval.py?ppid="+str(i[0])+">"+str(i[4])+"</td></tr>")
conn.commit()
print("</table>")
print("</center>")
print("</body>")
print("</html>")
