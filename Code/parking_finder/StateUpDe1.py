import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
reg=cgi.FieldStorage()
satid=reg.getvalue('satid')
satname=reg.getvalue('satname')
satimg=reg.getvalue('satimg')
satdesc=reg.getvalue('satdesc')
btn=reg.getvalue('btn')

if btn=="Update":
    if satimg=="":
        sql="update statereg set satname='"+str(satname)+"',satimg='"+str(satimg)+"',satdesc='"+str(satdesc)+"' where satid="+str(satid)
    else:
        sql="update statereg set satname='"+str(satname)+"',satdesc='"+str(satdesc)+"' where satid="+str(satid)

    insrt=a.execute(sql)
    if insrt!=0:
        print("successfull")
    else:
        print("unsuccessfull")
    conn.commit()
elif btn=="Delete":
    sql="update statereg set status='Deleted' where satid="+satid
    insrt=a.execute(sql)
    if insrt!=0:
        print("successfull")
    else:
        print("unsuccessfull")
    conn.commit()
        
    
