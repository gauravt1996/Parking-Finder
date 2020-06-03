import cgi
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=SelectParking.py>")
print("<body>")
print("<center>")
print("<table border=1>")
res=cgi.FieldStorage()
satid=str(res.getvalue('satid'))
cityid=str(res.getvalue('cityid'))
aid=str(res.getvalue('aid'))
ueid=str(res.getvalue('ueid'))

if satid =="0" and cityid=="0" and aid=="0":
      sql="Select p.peid,p.pname,p.pmob,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved'"
elif satid =="0" and cityid=="0" and aid !="0":
      sql="Select p.pname,p.pmob,p.peid,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved' and a.aid='"+aid+"'"
elif satid=="0" and cityid !="0" and aid=="0":
      sql="Select p.pname,p.pmob,p.peid,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved' and c.cityid='"+cityid+"'"
elif satid !="0" and cityid=="0" and aid=="0":
      sql="Select p.pname,p.pmob,p.peid,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved' and s.satid='"+satid+"'"
elif satid=="0" and cityid !="0" and aid !="0":
      sql="Select p.pname,p.pmob,p.peid,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved' and a.aid='"+aid+"' and c.cityid='"+cityid+"'"
elif satid !="0" and cityid=="0" and aid !="0":
      sql="Select p.pname,p.pmob,p.peid,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved' and a.aid='"+aid+"' and s.satid='"+satid+"'"
elif satid !="0" and cityid !="0" and aid=="0":
      sql="Select p.pname,p.pmob,p.peid,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved' and c.cityid='"+cityid+"' and s.satid='"+satid+"'"
elif satid !="0" and cityid !="0" and aid !="0":
      sql="Select p.pname,p.pmob,p.peid,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved' and c.cityid='"+cityid+"' and s.satid='"+satid+"' and a.aid='"+aid+"'"


#sql="Select p.peid,p.pname,p.pmob,pp.ppadd,a.aname,pp.ppzip,c.cityname,s.satname,pp.ppbroadimg,pp.ppid,pp.bstatus,pp.ppstatus from preg p,ppreg pp,areareg  a,cityreg c,statereg s where p.peid=pp.peid and pp.aid=a.aid and pp.cityid=c.cityid and c.satid=s.satid and pp.ppstatus='Approved'"
display=a.execute(sql)
data=a.fetchall()
conn.commit()


print("<h3>Providers</h3>")
for i in data:
      if str(i[10])=="Booked":
            print("<tr><td>"+str(i[9])+"</td><td><font color=red>"+str(i[1])+"<br>Email:"+str(i[0])+"</font></td><td>"+str(i[3])+"<br>"+str(i[4])+"<br>"+str(i[6])+"("+str(i[5])+")<br>"+str(i[7])+"</td><td><img src="+str(i[8])+" height=100 width=100></td><td><a href=SelectParking.py?ppid="+str(i[9])+"&peid="+str(i[0])+"&ueid="+str(ueid)+">Select Parking</a></td></tr>")
      else:
            print("<tr><td>"+str(i[9])+"</td><td><font color=green>"+str(i[1])+"<br>Email:"+str(i[0])+"</font></td><td>"+str(i[3])+"<br>"+str(i[4])+"<br>"+str(i[6])+"("+str(i[5])+")<br>"+str(i[7])+"</td><td><img src="+str(i[8])+" height=100 width=100></td><td><a href=SelectParking.py?ppid="+str(i[9])+"&peid="+str(i[0])+"&ueid="+str(ueid)+">Select Parking</a></td></tr>")
      

print("</table>")
print("</center>")
print("</body>")
print("</form>")
print("</html>")
