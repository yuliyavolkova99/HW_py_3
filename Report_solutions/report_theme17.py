'''Доклад тема 17'''

import urllib.request
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
from io import BytesIO

#Задание 1-2
test = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F_%D0%B6%D0%B8%D0%B2%D0%BE%D0%BF%D0%B8%D1%81%D1%8C')
headers = test.info()
print(headers)

#Задание 3
html = test.read()
encode = base64.b64encode(html)
print(encode)

#Задание 4
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(base64.b64decode(encode))

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
