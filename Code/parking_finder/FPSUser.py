import smtplib
import pymysql
import cgi
conn=pymysql.connect(host='localhost',user='root',password='1234',db='parking_finder')
a=conn.cursor()
res=cgi.FieldStorage()
ueid=str(res.getvalue('ueid'))
sql="Select upass from userreg where ueid='"+str(ueid)+"'"
display=a.execute(sql)
data=a.fetchall()
for i in data:
       msg = str(i[0])
try:
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls()
       server.login("gauravtaluja96@gmail.com","INSHE4EVR")
       server.sendmail("gauravtaluja96@gmail.com", ueid, msg)
       server.quit()
except:
       print("error")
