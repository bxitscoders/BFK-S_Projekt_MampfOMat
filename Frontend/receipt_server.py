"""
Einfacher HTTP-Server für PDF-Quittungen
Stellt die Quittungen unter http://localhost:5000/receipt/{filename} bereit
"""

import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import unquote
import threading


class ReceiptHandler(SimpleHTTPRequestHandler):
    """Handler für PDF-Quittungen"""
    
    receipts_dir = os.path.join(os.path.dirname(__file__), "assets", "receipts")
    
    def do_GET(self):
        """Verarbeite GET-Anfragen für Quittungen"""
        if self.path.startswith('/receipt/'):
            filename = unquote(self.path.replace('/receipt/', ''))
            filepath = os.path.join(self.receipts_dir, filename)
            
            # Sicherheit: Nur Dateien aus dem receipts_dir
            if not os.path.abspath(filepath).startswith(os.path.abspath(self.receipts_dir)):
                self.send_error(403, "Forbidden")
                return
            
            if os.path.exists(filepath) and filepath.endswith('.pdf'):
                try:
                    with open(filepath, 'rb') as f:
                        self.send_response(200)
                        self.send_header('Content-type', 'application/pdf')
                        self.send_header('Content-Disposition', f'inline; filename="{filename}"')
                        self.end_headers()
                        self.wfile.write(f.read())
                    return
                except Exception as e:
                    print(f"Fehler beim Lesen der Datei: {e}")
                    self.send_error(500, "Internal Server Error")
                    return
            else:
                self.send_error(404, "File not found")
                return
        
        self.send_error(400, "Bad Request")
    
    def log_message(self, format, *args):
        """Stille einfache Log-Ausgaben"""
        pass


def get_local_ip():
    """Ermittle die lokale IP-Adresse des Computers"""
    try:
        # Verbinde zu einem öffentlichen DNS-Server (wird nicht tatsächlich verbunden)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def start_receipt_server(port=5000):
    """Starte den HTTP-Server für Quittungen"""
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, ReceiptHandler)
    
    local_ip = get_local_ip()
    print(f"📄 Quittungs-Server läuft auf:")
    print(f"   Lokal:  http://localhost:{port}/receipt/")
    print(f"   Netzwerk: http://{local_ip}:{port}/receipt/")
    
    # Starte Server in Thread, damit App weiterläuft
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    
    return httpd, local_ip


if __name__ == "__main__":
    httpd, ip = start_receipt_server()
    print("Drücke Ctrl+C zum Beenden")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Server beendet")
