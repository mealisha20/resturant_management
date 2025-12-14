# Starts the API server and initializes the database

from http.server import HTTPServer, BaseHTTPRequestHandler
from router.billingRouter import billingRouter
from router.menuRouter import menuRouter
from router.staffRouter import staffRouter
from database.connection import init_database

class MainRouter(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/billings"):
            billingRouter(self)
        elif self.path.startswith("/menus"):
            menuRouter(self)
        elif self.path.startswith("/staffs"):
            staffRouter(self)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found")
            
def run_server(port=8000):
    init_database()
    server = HTTPServer(("", port), MainRouter)
    print(f"🚀 Server running at http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()