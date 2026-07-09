#!/usr/bin/env python3
"""Server statico per l'anteprima locale.
Serve una directory ESPLICITA per evitare os.getcwd() (bloccato dal sandbox)."""
import http.server
import socketserver

DIRECTORY = "/Users/giulioboscaro/Desktop/solpower_local"
PORT = 4321


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {DIRECTORY} at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
