from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import json
from datetime import datetime

# Define authorized users and their passwords
USERS = {
    'teamarun': 'The_number_one', # Arun
    'strategicfuhad': '8.toastcrunch', #Fuhad
    'estherlady': 'Nadia-Seymour84vYTx', #Esther
    'namitahyundai': '19.as.ducks', #Namita
    'brettonblazer': '41.bread_pitt', #Bretton
}

# Keep track of connected users
connected_users = []

class AuthHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.headers.get('Authorization') == None:
            self.send_auth_request()
            return

        auth_type, auth_string = self.headers.get('Authorization').split(' ')
        auth_string = base64.b64decode(auth_string).decode()
        username, password = auth_string.split(':')

        if auth_type == 'Basic' and USERS.get(username) == password:
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                connected_users.append(username)
                response = {'message': f'Hello {username}, today is a nice day.'}
                self.wfile.write(json.dumps(response).encode())
                print(f"Currently connected users: {', '.join(connected_users)}")
        else:
            self.send_auth_request()

    def send_auth_request(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Restricted\"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'error': 'Authentication required'}
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=AuthHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
