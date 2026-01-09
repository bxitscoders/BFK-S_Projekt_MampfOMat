import tkinter as tk
import os
import io
import time
import base64
import qrcode
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from ui.modern_styles import COLORS, FONTS, LAYOUT, create_modern_button

class ThankYouPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS['background_main'])
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        """Erstellt die moderne Danke-Seite"""
        # Hauptcontainer
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Zentrierter Container
        center_frame = tk.Frame(self, bg=COLORS['background_main'])
        center_frame.grid(row=0, column=0)

        # Zwei-spaltiges Layout: links Text, rechts QR
        content_h = tk.Frame(center_frame, bg=COLORS['background_main'])
        content_h.pack()

        left_frame = tk.Frame(content_h, bg=COLORS['background_main'])
        left_frame.pack(side='left', padx=(0, 30))

        right_frame = tk.Frame(content_h, bg=COLORS['background_main'])
        right_frame.pack(side='right')

        # Großes Erfolgs-Icon
        icon_label = tk.Label(
            left_frame,
            text="✅",
            font=('Segoe UI', 72, 'normal'),
            fg=COLORS['button_success'],
            bg=COLORS['background_main']
        )
        icon_label.pack(pady=(LAYOUT['padding_xlarge'], LAYOUT['padding_medium']))

        # Haupttitel
        title_label = tk.Label(
            left_frame,
            text="Vielen Dank für Ihre Bestellung!",
            font=FONTS['heading_large'],
            fg=COLORS['text_primary'],
            bg=COLORS['background_main']
        )
        title_label.pack(pady=(0, LAYOUT['padding_medium']))

        # Untertitel
        subtitle_label = tk.Label(
            left_frame,
            text="Ihre frischen Backwaren werden gerade zubereitet.",
            font=FONTS['body_large'],
            fg=COLORS['text_secondary'],
            bg=COLORS['background_main']
        )
        subtitle_label.pack(pady=(0, LAYOUT['padding_large']))

        # Wartungshinweis
        info_label = tk.Label(
            left_frame,
            text="Bitte warten Sie einen Moment...",
            font=FONTS['body_medium'],
            fg=COLORS['text_accent'],
            bg=COLORS['background_main']
        )
        info_label.pack(pady=(0, LAYOUT['padding_xlarge']))

        # Zurück-Button
        back_btn = create_modern_button(
            left_frame,
            "Neue Bestellung starten",
            style='primary',
            command=self.start_new_order
        )
        back_btn.pack(pady=LAYOUT['padding_medium'])

        # QR-Placeholder rechts
        self.qr_label = tk.Label(right_frame, bg=COLORS['background_main'])
        self.qr_label.pack()
        self.pdf_path = None
    
    def start_new_order(self):
        """Startet eine neue Bestellung (leert Warenkorb)"""
        # Warenkorb leeren
        if hasattr(self.controller, 'clear_cart'):
            self.controller.clear_cart()
        
        # Zur Homepage zurückkehren
        self.controller.show_frame("HomePage")
    
    def update_page(self, **kwargs):
        """Wird aufgerufen wenn die Seite angezeigt wird"""
        # Falls Bestelldaten übergeben wurden, PDF erzeugen und QR anzeigen
        order = kwargs.get('order')
        if order:
            try:
                pdf_path = self._generate_receipt_pdf(order)
                self.pdf_path = pdf_path
                
                # Erstelle auch eine Download-HTML-Seite
                html_path = self._generate_download_html(pdf_path)
                
                # QR-Code mit HTML-Download-Link
                qr_img = self._generate_qr_for_pdf(html_path)
                self.qr_photo = ImageTk.PhotoImage(qr_img)
                self.qr_label.configure(image=self.qr_photo)

                # Öffnen-Button unterhalb des QR-Codes
                if not hasattr(self, 'open_btn'):
                    def open_pdf():
                        if self.pdf_path and os.path.exists(self.pdf_path):
                            try:
                                os.startfile(self.pdf_path)
                            except Exception as e:
                                print(f"Fehler beim Öffnen der PDF: {e}")
                    
                    open_btn = create_modern_button(
                        self.qr_label.master,
                        "📄 Quittung öffnen",
                        style='primary',
                        command=open_pdf
                    )
                    open_btn.pack(pady=(10, 0))
                    self.open_btn = open_btn
            except Exception as e:
                print(f"Fehler beim Erzeugen der Quittung: {e}")

        try:
            youtube_url = "https://www.youtube.com/watch?v=Aq5WXmQQooo&list=RDAq5WXmQQooo&start_radio=1"
            youtube_qr_img = self._generate_simple_qr(youtube_url, size=120)
            self.youtube_qr_photo = ImageTk.PhotoImage(youtube_qr_img)
            self.youtube_qr_label.configure(image=self.youtube_qr_photo)
        except Exception as e:
            print(f"Fehler beim Erzeugen des YouTube QR-Codes: {e}")

        # Automatisches Leeren des Warenkorbs bei Bestellabschluss (falls noch nicht geschehen)
        if hasattr(self.controller, 'clear_cart'):
            self.controller.clear_cart()

        """Erzeugt ein einfaches QR-Bild für URLs (z.B. YouTube)"""
        qr = qrcode.QRCode(box_size=10, border=2, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        return img

    def _generate_qr_for_pdf(self, html_path, size=220):
        """Erzeugt ein QR-Bild (PIL.Image) mit Link zur Download-HTML"""
        # Nutze file:// URL für lokale HTML-Datei
        file_url = f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
        
        qr = qrcode.QRCode(box_size=10, border=2, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(file_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        return img

    def _generate_receipt_pdf(self, order):
        """Erzeugt eine einfache PDF-Quittung mit Logo, Artikelliste und MwSt-Berechnung."""
        receipts_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "receipts")
        receipts_dir = os.path.abspath(receipts_dir)
        os.makedirs(receipts_dir, exist_ok=True)

        timestamp = int(time.time())
        filename = f"receipt_{timestamp}.pdf"
        pdf_path = os.path.join(receipts_dir, filename)

        c = canvas.Canvas(pdf_path, pagesize=A4)
        width, height = A4

        margin = 20 * mm
        y = height - margin

        # Header: Logo (falls vorhanden) und Firmenname
        logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
        if os.path.exists(logo_path):
            try:
                # skaliere Logo
                c.drawImage(logo_path, margin, y-30*mm, width=40*mm, preserveAspectRatio=True, mask='auto')
            except Exception:
                pass
        c.setFont("Helvetica-Bold", 18)
        c.drawString(margin + 45*mm, y - 10*mm, "MAMPFOMAT")
        c.setFont("Helvetica", 10)
        c.drawString(margin + 45*mm, y - 16*mm, "Ihre frischen Backwaren")

        y -= 35 * mm

        # Bestelldatum
        c.setFont("Helvetica", 9)
        c.drawString(margin, y, f"Datum: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        y -= 8 * mm

        # Tabellen-Header
        c.setFont("Helvetica-Bold", 10)
        c.drawString(margin, y, "Artikel")
        c.drawString(margin + 90*mm, y, "Menge")
        c.drawString(margin + 110*mm, y, "Einzelpreis")
        c.drawString(margin + 140*mm, y, "Gesamt")
        y -= 6 * mm
        c.line(margin, y, width - margin, y)
        y -= 6 * mm

        c.setFont("Helvetica", 10)
        for it in order.get('items', []):
            if y < margin + 40*mm:
                c.showPage()
                y = height - margin

            c.drawString(margin, y, it['name'])
            c.drawString(margin + 90*mm, y, str(it['quantity']))
            c.drawRightString(margin + 135*mm + 20*mm, y, f"{it['unit_price']:.2f} €")
            c.drawRightString(width - margin, y, f"{it['total_price']:.2f} €")
            y -= 6 * mm

        y -= 6 * mm
        c.line(margin, y, width - margin, y)
        y -= 8 * mm

        # Summen
        c.setFont("Helvetica-Bold", 11)
        c.drawRightString(width - margin, y, f"Zwischensumme: {order.get('subtotal',0):.2f} €")
        y -= 6 * mm
        c.drawRightString(width - margin, y, f"MwSt ({int(order.get('vat_rate',0)*100)}%): {order.get('vat_amount',0):.2f} €")
        y -= 6 * mm
        c.drawRightString(width - margin, y, f"Gesamt: {order.get('total',0):.2f} €")

        c.showPage()
        c.save()

        return pdf_path

    def _generate_download_html(self, pdf_path):
        """Erzeugt eine HTML-Datei mit eingebetteter PDF zum Download"""
        receipts_dir = os.path.dirname(pdf_path)
        html_filename = os.path.basename(pdf_path).replace('.pdf', '.html')
        html_path = os.path.join(receipts_dir, html_filename)
        
        pdf_filename = os.path.basename(pdf_path)
        
        # Lese PDF und encode als base64
        with open(pdf_path, 'rb') as f:
            pdf_data = base64.b64encode(f.read()).decode('utf-8')
        
        html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MAMPFOMAT - Quittung</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
            padding: 40px;
            text-align: center;
            max-width: 500px;
            width: 100%;
        }}
        .header {{
            margin-bottom: 30px;
        }}
        .logo {{
            font-size: 48px;
            margin-bottom: 15px;
        }}
        h1 {{
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 28px;
        }}
        .subtitle {{
            color: #7f8c8d;
            font-size: 14px;
            margin-bottom: 5px;
        }}
        .receipt-id {{
            color: #3498db;
            font-weight: bold;
            margin-top: 15px;
            font-size: 16px;
        }}
        .download-btn {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 16px;
            font-weight: bold;
            margin-top: 30px;
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
            border: none;
        }}
        .download-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        }}
        .download-btn:active {{
            transform: translateY(0);
        }}
        .info {{
            margin-top: 25px;
            padding-top: 25px;
            border-top: 1px solid #ecf0f1;
            color: #7f8c8d;
            font-size: 13px;
            line-height: 1.6;
        }}
        .check-icon {{
            font-size: 60px;
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="check-icon">✅</div>
            <h1>Danke für Ihre Bestellung!</h1>
            <p class="subtitle">Ihre frischen Backwaren werden gerade zubereitet.</p>
            <div class="receipt-id">Quittungs-ID: {os.path.basename(pdf_path).replace('receipt_', '').replace('.pdf', '')}</div>
        </div>
        
        <button class="download-btn" onclick="downloadPDF()">📥 Quittung herunterladen</button>
        
        <div class="info">
            <p>👉 Klicken Sie auf den Button, um Ihre Quittung zu speichern.</p>
            <p>💾 Die PDF wird auf Ihrem Gerät gespeichert.</p>
            <p>📱 Sie können die Quittung jederzeit anzeigen oder ausdrucken.</p>
        </div>
    </div>

    <script>
        // PDF als base64 (eingebettet)
        const pdfBase64 = "{pdf_data}";
        
        function downloadPDF() {{
            // Konvertiere base64 zu binary
            const byteCharacters = atob(pdfBase64);
            const byteNumbers = new Array(byteCharacters.length);
            for (let i = 0; i < byteCharacters.length; i++) {{
                byteNumbers[i] = byteCharacters.charCodeAt(i);
            }}
            const byteArray = new Uint8Array(byteNumbers);
            
            // Erstelle Blob und Download-Link
            const blob = new Blob([byteArray], {{ type: 'application/pdf' }});
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = '{pdf_filename}';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            window.URL.revokeObjectURL(url);
        }}
    </script>
</body>
</html>"""
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return html_path
