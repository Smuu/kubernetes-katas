from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading, os
import random
import logging
import signal
import sys

hostName = "0.0.0.0"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/livez":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("{}", "utf-8"))
        elif self.path == "/readyz":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("{}", "utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Troubleshooting</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>If you read this in your browser you fixed all bugs.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

def crash_server():
    time.sleep(random.randint(120, 360))
    logging.error("Server is crashed. Update to 'v1.0.1'.")
    os._exit(1)

if __name__ == "__main__":
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    logging.info("Starting server on http://%s:%s" % (hostName, serverPort))
    time.sleep(5)
    webServer = HTTPServer((hostName, serverPort), MyServer)
    logging.info("Server started")

    daemon = threading.Thread(name='daemon_server', target=crash_server)
    daemon.setDaemon(True)
    daemon.start()

    def signal_handler(signal, frame):
        logging.info('Exiting http server (Received SIGTERM)')
        try:
            if(webServer):
                webServer.server_close()
        finally:
            sys.exit(0)

    signal.signal(signal.SIGTERM, signal_handler)

    try:
        while True:
            sys.stdout.flush()
            webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    logging.info("Server stopped.")
