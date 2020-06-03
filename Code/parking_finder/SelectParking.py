import cgi
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<form action=SelectParking1.py>")
res=cgi.FieldStorage()
ppid=str(res.getvalue('ppid'))
ueid=str(res.getvalue('ueid'))
print("<center>")
print("<table border=1>")
sql="Select p.peid,p.pname,p.pmob,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppid='"+str(ppid)+"'"
display=a.execute(sql)
data=a.fetchall()
conn.commit()

print("<h3>Providers</h3>")
for i in data:
    print("<tr><td>"+str(i[1])+"<br>Mob: "+str(i[2])+"<br>Email: "+str(i[0])+"</td><td>"+str(i[3])+"<br>"+str(i[4])+"<br>"+str(i[6])+"("+str(i[5])+")<br>"+str(i[7])+"</td><td><img src="+str(i[8])+" height=100 width=100></td></tr><tr><td><a href=SelectParking1.py?ppid="+str(ppid)+"&peid="+str(i[0])+"&ueid="+str(ueid)+">Select Parking</a></td></tr>")
conn.commit()
print("</table>")
print("</center>")
print("</body>")
print("</form>")
print("</html>")
