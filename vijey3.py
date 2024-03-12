from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
   <head>
      <title>Top software companies</title>
   </head>
<body bgcolor='orange' align='center'>
<caption>
     <h3>Top 5 revenue generating software companies</h3>
</caption>
<table border='3' align='center'>
<tr>
<th>sno.</th>
<th>company</th>
<th>revenue</th>
</tr>
<tr>
<td>1.</td>
<td>Microsoft</td>
<td>203.08 billion</td>
</tr>
<tr>
<td>2.</td>
<td>oracle</td>
<td>46.07 billion</td>
</tr>
<tr>
<td>3.</td>
<td>SAP SE(SAP)</td>
<td>32.97 billion</td>
</tr>
<tr>
<td>4.</td>
<td>Salesforce</td>
<td>30.29 billion</td>
</tr>
<tr>
<td>5.</td>
<td>Adobe</td>
<td>17.61 billion</td>
</tr>
</table>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()