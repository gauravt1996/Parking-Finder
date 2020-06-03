import pymysql
import cgi

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()


print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<form action=ProviderApprovalUpdate.py>")
print("<center>")
print("<table border=1>")
res=cgi.FieldStorage()
status=str(res.getvalue('ppstatus'))
ppid=str(res.getvalue('ppid'))
print("<tr><td>Provider ID</td><td>Provider Name</td><td>Provider Mobile</td><td>Provider Email</td><td>Parking Location</td><td>Area</td><td>City</td><td>Zip Code</td><td>Provider Aadhar Number</td><td>Provider Aadhar Image</td><td>Provider Spot Image</td><td>Provider Status</td><td>Provider Broad Image</td><td>number of Parking Spaces</td></tr>")
sql="Select pp.ppid,p.pname,p.pmob,p.peid,pp.ppadd,a.aname,c.cityname,pp.ppzip,pp.ppaadhar,pp.ppaadharimg,pp.ppspotimg,pp.ppstatus,pp.ppbroadimg,pp.ppvnum from ppreg pp,preg p,cityreg c,areareg a where pp.peid=p.peid and pp.cityid=c.cityid and pp.aid=a.aid and pp.ppid='"+str(ppid)+"'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
       print("<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td>"+str(i[7])+"</td><td>"+str(i[8])+"</td><td>"+str(i[9])+"</td><td>"+str(i[10])+"</td><td>"+str(i[11])+"</td><td>"+str(i[12])+"</td><td>"+str(i[13])+"</td></tr>")

print("<tr><td>Conversation</td><td><textarea name=message placeholder=TypeHere.... rows=15 cols=50></textarea><input type=hidden value="+ppid+" name=ppid></td></tr>")

print("<tr><td><input type=submit value=Approval name=btn></td><td><input type=submit value=Disapproval name=btn></td></tr>")
conn.commit()
print("</table>")
print("</center>")
print("</form>")
print("</body>")
print("</html>")
