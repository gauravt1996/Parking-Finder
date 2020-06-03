import smtplib
import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
res=cgi.FieldStorage()
peid=str(res.getvalue('peid'))
sql="Select ppass from preg where peid='"+str(peid)+"'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
       msg = str(i[0])
try:
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls()
       server.login("gauravtaluja96@gmail.com","INSHE4EVR")
       server.sendmail("gauravtaluja96@gmail.com", peid, msg)
       server.quit()
except:
       print("error")
