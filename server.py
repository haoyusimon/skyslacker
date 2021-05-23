'''
import http.server
import socketserver
import ssl

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="192.168.31.132-key.pem", 
        certfile="192.168.31.132.pem", server_side=True, ssl_version=ssl.PROTOCOL_TLS)

httpd.serve_forever()
'''

import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl
import sys

#This class will handles any incoming request from the browser

class myHandler(BaseHTTPRequestHandler):
        #Handler for the GET requests
        
        def do_GET(self):
                print(self.requestline)
                #print(self.rfile.read(content_length))
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write("Hello World !".encode())
                return

try:
        separator = "-" * 80
        server_address = ('', 4443)
        # server_address = ('localhost', 8000)
        #httpd = http.server.HTTPServer(server_address, myHandler)
        httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,
                            server_side=True,
                            certfile="172.20.10.5.pem",
                            keyfile="172.20.10.5-key.pem")        
        print(separator)
        print("Server running on https://localhost:4443")
        print(separator)

        # Wait forever for incoming http requests
        httpd.serve_forever()

except KeyboardInterrupt:
        print ('^C received, shutting down the web server')
        httpd.socket.close()