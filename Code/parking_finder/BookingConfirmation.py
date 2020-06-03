import cgi
import pymysql
import datetime
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<center>")

res=cgi.FieldStorage()
accno=str(res.getvalue('accno'))
bpass=str(res.getvalue('pass'))
peid=str(res.getvalue('peid'))
ppid=str(res.getvalue('ppid'))
ueid=str(res.getvalue('ueid'))
now=datetime.datetime.now()
sql="Select * from bank where accno='"+str(accno)+"' and pass='"+str(bpass)+"'"
display=a.execute(sql)
data=a.fetchall()
conn.commit()

for sql in data:
       print("Payment Done Successfully")
       sql="insert into bookinginfo(ppid,ueid,dt)values('"+str(ppid)+"','"+str(ueid)+"','"+str(now)+"')"
       display=a.execute(sql)
       conn.commit()
       print("</center>")
       print("<center>")
       print("<table border=1>")
       sql="Select * from bookinginfo b , ppreg pp, preg p where b.ppid=pp.ppid and p.peid=pp.peid order by b.bookingid desc"
       display=a.execute(sql)
       data=a.fetchall()
       conn.commit()
       for i in data:
              print("<tr><td>Booking ID</td><td>"+str(i[0])+"</td></tr><tr><td>Provider Name</td><td>"+str(i[17])+"</td></tr><tr><td>Provider Mob</td><td>"+str(i[18])+"</td><tr><td>Provider Email</td><td>"+str(i[19])+"</td></tr><tr><td>Provider Add</td><td>"+str(i[7])+"</td></tr>")
              sql="Update ppreg set bstatus='Booked' where ppid="+str(ppid)
              display=a.execute(sql)
              data=a.fetchall()
              conn.commit()
              break
       
print("</table>")
print("</body>")
print("</form>")
