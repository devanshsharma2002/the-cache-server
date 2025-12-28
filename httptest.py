import requests
from cachemanager import CacheManager

from http.server import HTTPServer, BaseHTTPRequestHandler


class ProxyHandler(BaseHTTPRequestHandler):
    igin_url = None  # We'll set this from outside

    def do_GET(self):
        # Python automatically gives you:
        # - self.path (the URL path)
        # - self.headers (request headers)
        # - self.send_response() (send response)
        # All this comes FREE from BaseHTTPRequestHandler!

        # Build full target URL
        target_url = self.origin_url + self.path
        print(f"Forwarding to: {target_url}")
        
        # Send simple response for now
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Will forward to origin soon!")



# At bottom
ProxyHandler.origin_url = "http://dummyjson.com"
server = HTTPServer(('', 3000), ProxyHandler)
print("Proxy running on 3000")
server.serve_forever()
