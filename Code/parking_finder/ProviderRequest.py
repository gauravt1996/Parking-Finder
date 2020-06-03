import cgi

print("content-text:text/html\r\n\r\n")
print("<html>")
print("<form action=ProviderDisplay.py>")
print("<tr><td>Provider</td><td><select name=ppstatus>")
print("<option value=NotSeen>Not Seen</option>")
print("<option value=Pending>Pending</option>")
print("<option value=Approved>Approved</option>")
print("<option value=Disapproved>Disapproved</option>")
print("</select></td><td><input type=submit></td></tr>")
print("</form>")
print("</html>")
