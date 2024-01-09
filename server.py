import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)

def rele_on():
    print("Rele ON")
    GPIO.output(23, GPIO.HIGH)

def rele_off():
    print("Rele OFF")
    GPIO.output(23, GPIO.LOW)

class MyHandler(BaseHTTPRequestHandler):
    html_page = """
    <html>
    <head>
        <title>Control de Relé</title>
    </head>
    <body>
        <h1>Control de Relé</h1>
        <button onclick="sendCommand('on')">ON</button>
        <button onclick="sendCommand('off')">OFF</button>

        <script>
            function sendCommand(command) {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "/" + command, true);
                xhr.send();
            }
        </script>
    </body>
    </html>
    """

    def do_GET(self):
        if self.path == '/on':
            rele_on()
        elif self.path == '/off':
            rele_off()

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.html_page.encode())

def run(server_class=HTTPServer, handler_class=MyHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor iniciado en el puerto {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    setupGPIO()
    run()
