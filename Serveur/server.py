#!/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler

# PORT = 8888
# server_address = ("127.0.0.1", PORT)

# server = http.server.HTTPServer
# handler = http.server.CGIHTTPRequestHandler
# handler.cgi_directories = ["/"]
# print("Serveur actif sur le port :", PORT)

# httpd = server(server_address, handler)
# httpd.serve_forever()

import webbrowser


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
webbrowser.open("http://localhost:"+str(8000))
httpd.serve_forever()
