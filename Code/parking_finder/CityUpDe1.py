import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
reg=cgi.FieldStorage()
cityid=reg.getvalue('cityid')
satid=reg.getvalue('satid')
cityname=reg.getvalue('cityname')
cityimg=reg.getvalue('cityimg')
citydesc=reg.getvalue('citydesc')
btn=reg.getvalue('btn')

if btn=="Update":
    if cityimg=="":
        sql="update cityreg set cityname='"+str(cityname)+"',cityname='"+str(cityname)+"',cityimg='"+str(cityimg)+"',citydesc='"+str(citydesc)+"' where cityid="+str(cityid)
    else:
        sql="update cityreg set cityname='"+str(cityname)+"',citydesc='"+str(citydesc)+"' where cityid="+str(cityid)


    insrt=a.execute(sql)
    if insrt!=0:
        print("successfull")
    else:
        print("unsuccessfull")
    conn.commit()
elif btn=="Delete":
    sql="update cityreg set status='Deleted' where cityid="+cityid
    insrt=a.execute(sql)
    print(sql)
    if insrt!=0:
        print("successfull")
    else:
        print("unsuccessfull")
    conn.commit()
        
    
