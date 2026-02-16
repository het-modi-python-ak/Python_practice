from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class rquesthandeling(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message body
        message = "Hello! This is a python server"
        self.wfile.write(bytes(message, "utf8"))
        logging.info(f"GET request,\nPath: {str(self.path)}\nHeaders:\n{str(self.headers)}\n")

def run_server(server_class=HTTPServer, handler_class=rquesthandeling, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    logging.basicConfig(level=logging.INFO)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping server...')

if __name__ == '__main__':
    run_server()
