import pymysql
import cgi
import datetime
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
print("content-text:text/html\r\n\r\n")
res=cgi.FieldStorage()
btn=res.getvalue('btn')
ppid=str(res.getvalue('ppid'))
message=str(res.getvalue('message'))
now=datetime.datetime.now()
if btn=="Approval":
       sql="update ppreg set ppstatus='Approved' where ppid="+str(ppid)
       insrt=a.execute(sql)
       sql1="insert into conversation(ppid,message,date)values('"+str(ppid)+"','"+str(message)+"','"+str(now)+"')"
       insert=a.execute(sql1)
       if insrt!=0:
              print("successfull")
       else:
              print("unsuccessfull")
       conn.commit()
elif btn=="Disapproval":
       sql="update ppreg set ppstatus='Disapproved'"
       insrt=a.execute(sql)
       sql1="insert into conversation(ppid,message,date)values('"+str(ppid)+"','"+str(message)+"','"+str(now)+"')"
       insert=a.execute(sql1)
       if insrt!=0:
              print("successfull")
       else:
              print("unsuccessfull")
       conn.commit()
