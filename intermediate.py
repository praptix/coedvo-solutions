import http.server
import socketserver
import pyqrcode
import png
import os
import socket

# Define the port number
PORT = 8000

# Create the 'files' directory if it doesn't exist
if not os.path.exists('files'):
    os.makedirs('files')

# Get the IP address of the machine
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Generate the URL for sharing files
url = f"http://{IPAddr}:{PORT}"

# Generate a QR code for the URL
qr = pyqrcode.create(url)
qr.png("qr_code.png", scale=6)

# Create a custom handler to serve files from the 'files' directory
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/files'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Change working directory to 'files' so that the server serves files from there
os.chdir('files')

# Start the HTTP server
Handler = CustomHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at {url}")
    print("Scan the QR code (qr_code.png) to access the files.")
    httpd.serve_forever()

