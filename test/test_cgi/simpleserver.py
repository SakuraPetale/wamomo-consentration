# このスクリプトを実行して、'http://127.0.0.1:8000'
import http.server

server_address = ("", 8000)
# handler_class = http.server.SimpleHTTPRequestHandler
handler_class = http.server.CGIHTTPRequestHandler
# simple_server = http.server.HTTPServer(server_address, handler_class)
#simple_server.serve_forever()
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()


