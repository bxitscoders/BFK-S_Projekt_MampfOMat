from ui.app import App
from receipt_server import start_receipt_server

if __name__ == "__main__":
    # Starte den Quittungs-Server
    httpd, local_ip = start_receipt_server(port=5000)
    
    # Starte die App
    app = App()
    app.mainloop()