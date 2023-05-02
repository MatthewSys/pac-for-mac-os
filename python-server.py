#!/opt/homebrew/bin/python3

import http.server
import socketserver

ADDR = "127.0.0.1"
PORT = 8443
DIRECTORY = '/Users/matthew/.proxy/'

class quietServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

with socketserver.TCPServer((ADDR, PORT), quietServer) as httpd:
    try:
       httpd.serve_forever()
    except KeyboardInterrupt: 
       print("\nRecive keyboard interrapt,closing...") 
       httpd.server_close()
