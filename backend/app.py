"""Simple HTTP server for Effective Mobile test assignment."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = int(os.environ.get("APP_PORT", 8080))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"ok")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {args[0]}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Backend listening on port {PORT}")
    server.serve_forever()
