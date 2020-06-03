import cgi
print("content-text:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<center>")
res=cgi.FieldStorage()
aid=str(res.getvalue('aid'))
apass=str(res.getvalue('apass'))
if aid=="admin" and apass=="admin":
      print("<table border=1>")
      print("<caption><font size=7> Admin Home </font></caption>")
      print("<tr><td>Header</td><td>Header</td></tr>")
      print("<tr><td><a href=StateInterface.py target=aa>State Registration</a><br><a href=CityInterface.py target=aa>City Registration</a><br><a href=AreaInterface.py target=aa>Area Registration</a><br><a href=ProviderRequest.py target=aa>Provider Request</a><br></td><td><iframe name=aa height=500 width=500></iframe></td></tr>")
      print("<tr><td>Footer</td><td>Footer</td></tr>")
      print("</table>")
else:
      print("ID and Password not matched")
print("</center>")
print("</body>")
print("</html>")
      
      
