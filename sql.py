import sqlite3
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configuración de la base de datos
DATABASE = 'users.db'

def initialize_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def store_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"User {username} already exists.")
    conn.close()

def validate_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password_hash=?', (username, password_hash))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Configuración del servidor web
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, world!")

def run_server():
    server_address = ('', 7500)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running server on port 7500...')
    httpd.serve_forever()

if __name__ == "__main__":
    # Inicializar la base de datos y almacenar usuarios
    initialize_db()
    store_user('integrante1', 'password1')
    store_user('integrante2', 'password2')
    store_user('integrante3', 'password3')
    
    # Validar usuarios
    print(validate_user('integrante1', 'password1'))  # Debería devolver True
    print(validate_user('integrante2', 'wrongpassword'))  # Debería devolver False

    # Correr el servidor web
    run_server()
