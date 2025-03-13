from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # En-têtes de réponse
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Contenu de la réponse
        message = """
        <html>
            <body>
                <h1>Hello, Docker!</h1>
            </body>
        </html>
        """
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)
    
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()


# commende pour la creation de l'image: docker build -t mon_server
# commende pour demarrer sans blocker compose le terminal : docker run -d -p 8000:8000 mon_server
# commende pour arreter le server:  docker stop 99ab59d4dc2e
# commende pour demarrer avec docker compose: docker-compose up --build
# commende pour arreter avec docker compose: docker-compose down