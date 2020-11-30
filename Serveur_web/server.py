#!/usr/bin/python3
import http.server
server = http.server.HTTPServer
PORT = 8888
server_adresss = ("",PORT)
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Server listenning on :",PORT)

httpd = server(server_adresss,handler)
httpd.serve_forever()