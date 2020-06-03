import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
reg=cgi.FieldStorage()
aid=reg.getvalue('aid')
cityid=reg.getvalue('cityid')
aname=reg.getvalue('aname')
azip=reg.getvalue('azip')
btn=reg.getvalue('btn')

if btn=="Update":
       sql="update areareg set cityid='"+str(cityid)+"',aname='"+str(aname)+"',azip='"+str(azip)+"' where aid="+str(aid)
       print(sql)
       insrt=a.execute(sql)
       if insrt!=0:
              print("successfull")
       else:
              print("unsuccessfull")
       conn.commit()
elif btn=="Delete":
    sql="update areareg set status='Deleted' where aid="+str(aid)
    insrt=a.execute(sql)
    if insrt!=0:
        print("successfull")
    else:
        print("unsuccessfull")
    conn.commit()
        
    
