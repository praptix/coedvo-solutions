import http.server
import socketserver
import pyqrcode
import png
import os
import socket
import webbrowser

# Define port number and user name
PORT = 8000  # Change this if needed
USER_NAME = "Prapti"  # Replace with your name

# Step 1: Get IP address of the machine
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Connect to a remote host to get the local IP address
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  # Default to localhost if there's an error
    finally:
        s.close()
    return ip

# Step 2: Generate QR code for easy access
def generate_qr_code(ip, port):
    url = f"http://{ip}:{port}"
    qr = pyqrcode.create(url)
    qr.png("qrcode.png", scale=6)  # Save QR code as an image
    print(f"QR code generated: {url}")
    return url

# Step 3: HTTP Request Handler to handle file sharing
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Display custom message in the browser
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>File Sharing App</h1>", "utf-8"))
        self.wfile.write(bytes(f"<p>Welcome, {USER_NAME}! You can share your files here.</p>", "utf-8"))
        super().do_GET()  # Call the default GET handler to list files

# Step 4: Set up the HTTP server
def run_server():
    handler = CustomHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

# Step 5: Open the QR code image in a web browser
def open_qr_code():
    webbrowser.open("qrcode.png")

# Step 6: Main function to run the entire application
if __name__ == "__main__":
    ip = get_ip()  # Get the local IP address of the machine
    url = generate_qr_code(ip, PORT)  # Generate and display QR code
    open_qr_code()  # Open the generated QR code image in the default web browser
    run_server()  # Start the HTTP server to share files
