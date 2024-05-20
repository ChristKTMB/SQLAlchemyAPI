from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from json import dumps, loads
import sys
import os
from config import Config
from src.controllers.ApiController import ApiController

database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)

conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

# Créer une instance de ApiController
api = ApiController(session)

class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.path == '/api':
            if 'method' in query_params:
                method = query_params['method'][0]

                if method == 'getUsers':
                    response, status_code = api.get_users()
                elif method == 'getUserByField':
                    if 'field' in query_params and 'value' in query_params:
                        field = query_params['field'][0]
                        value = query_params['value'][0]
                        response, status_code = api.get_user_by_field(field, value)
                    else:
                        response = {'success': False, 'message': 'Champ ou valeur manquant'}
                        status_code = 400
                else:
                    response = {'success': False, 'message': 'Méthode non supportée'}
                    status_code = 405
                
                # Fermer la session
                session.close()
                
                # Envoi de la réponse
                self.send_response(status_code)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(dumps(response).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(dumps({'message': 'Paramètre "method" manquant'}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(dumps({'message': 'Endpoint non trouvé'}).encode())

    def do_POST(self):
        if self.path == '/api':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = loads(post_data)  # Convertir les données JSON en un dictionnaire Python
            
            method = data.get('method', '')
            if method == 'login':
                name = data.get('name', '')
                password = data.get('password', '')
                
                response, status_code = api.login(name, password)

            else:
                response = {'message': 'Méthode non supportée'}
                status_code = 405

            session.close()

        else:
            response = {'message': 'Endpoint non trouvé'}
            status_code = 404

        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(dumps(response).encode())

def run_server():
    try:
        port = 5000
        server_address = ('', port)
        httpd = HTTPServer(server_address, APIHandler)
        print(f"Serveur démarré sur le port {port}...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur...")
        httpd.server_close()
        sys.exit()

if __name__ == "__main__":
    run_server()
    