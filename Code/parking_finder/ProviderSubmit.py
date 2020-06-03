import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
print("<html>")

res=cgi.FieldStorage()
ppadd=str(res.getvalue('ppadd'))
cityid=str(res.getvalue('cityid'))
aid=str(res.getvalue('aid'))
ppzip=str(res.getvalue('ppzip'))
ppa=str(res.getvalue('ppaadhar'))
ppai=str(res.getvalue('ppaadharimg'))
ppsi=str(res.getvalue('ppspotimg'))
ppbi=str(res.getvalue('ppbroadimg'))
ppvnum=str(res.getvalue('ppvnum'))
peid=str(res.getvalue('peid'))
sql="insert into ppreg(ppadd,cityid,aid,ppzip,ppaadhar,ppaadharimg,ppspotimg,ppstatus,ppbroadimg,ppvnum,peid,bstatus)values('"+str(ppadd)+"','"+str(cityid)+"','"+str(aid)+"','"+str(ppzip)+"','"+str(ppa)+"','"+str(ppai)+"','"+str(ppsi)+"','Pending','"+str(ppbi)+"','"+str(ppvnum)+"','"+str(peid)+"','NotBooked')"
insert=a.execute(sql)
if insert!=0:
    print("successful")
else:
    print("failed")
conn.commit()
