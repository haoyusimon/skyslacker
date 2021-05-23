from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


httpd = HTTPServer(('', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="172.20.10.5-key.pem", 
        certfile='172.20.10.5.pem', server_side=True)

httpd.serve_forever()