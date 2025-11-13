import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ui.modern_styles import COLORS, FONTS, LAYOUT, create_modern_button

class ProductPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLORS['background_main'])
        self.controller = controller
        self.product = None
        self.product_image = None
        
        self.create_layout()

    def create_layout(self):
        """Erstellt das Amazon-inspirierte Layout mit Scrolling und WhatsApp-Hintergrund"""
        # WhatsApp-ähnlicher Hintergrund
        self.configure(bg='#e5ddd5')  # WhatsApp heller Hintergrund
        
        # Haupt-Canvas für Scrolling mit WhatsApp-Hintergrund
        self.canvas = tk.Canvas(self, bg='#e5ddd5', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#e5ddd5')
        
        # Scrolling konfigurieren
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Canvas-Window erstellen und Größe dynamisch anpassen
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Canvas-Breite an Fenster anpassen
        def configure_canvas_width(event):
            canvas_width = event.width
            self.canvas.itemconfig(self.canvas_window, width=canvas_width)
        
        self.canvas.bind('<Configure>', configure_canvas_width)
        
        # Canvas und Scrollbar packen
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Mousewheel-Scrolling aktivieren
        def bind_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", on_mousewheel)
            
        def unbind_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")
            
        def on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        self.canvas.bind('<Enter>', bind_mousewheel)
        self.canvas.bind('<Leave>', unbind_mousewheel)
        
        # Main Container in scrollable frame mit WhatsApp-Hintergrund
        main_container = tk.Frame(self.scrollable_frame, bg='#e5ddd5')
        main_container.pack(fill="both", expand=True, padx=20, pady=10)  # Weniger Padding
        
        # Produktbild ganz oben - prominent platziert
        self.create_top_image_section(main_container)
        
        # Breadcrumb Navigation nach dem Bild
        self.create_breadcrumb(main_container)
        
        # Hauptinhalt - 1-Spalten Layout für bessere Mobilansicht
        content_frame = tk.Frame(main_container, bg='#e5ddd5')
        content_frame.pack(fill="both", expand=True, pady=10)
        
        # Produktdetails
        self.create_details_section(content_frame)

    def create_breadcrumb(self, parent):
        """Erstellt die Breadcrumb-Navigation"""
        breadcrumb_frame = tk.Frame(parent, bg='#e5ddd5')
        breadcrumb_frame.pack(fill="x", pady=(0, 20))
        
        # Home Link
        home_link = tk.Label(
            breadcrumb_frame,
            text="🏠 Startseite",
            font=FONTS['body_medium'],
            fg=COLORS['accent_blue'],
            bg='#e5ddd5',
            cursor='hand2'
        )
        home_link.pack(side="left")
        home_link.bind("<Button-1>", lambda e: self.controller.show_frame("HomePage"))
        
        # Separator
        separator = tk.Label(
            breadcrumb_frame,
            text=" > ",
            font=FONTS['body_medium'],
            fg=COLORS['text_secondary'],
            bg='#e5ddd5'
        )
        separator.pack(side="left")
        
        # Current Product
        self.product_breadcrumb = tk.Label(
            breadcrumb_frame,
            text="Produkt",
            font=FONTS['body_medium'],
            fg=COLORS['text_primary'],
            bg='#e5ddd5'
        )
        self.product_breadcrumb.pack(side="left")

    def create_top_image_section(self, parent):
        """Erstellt das Produktbild ganz oben - prominent platziert"""
        image_container = tk.Frame(parent, bg='white', relief='solid', bd=1)
        image_container.pack(fill="x", pady=(0, 20))
        
        image_frame = tk.Frame(image_container, bg='white')
        image_frame.pack(fill="x", padx=15, pady=15)
        
        self.image_label = tk.Label(
            image_frame,
            bg='white',
            text="📷 Produktbild wird geladen...",
            font=FONTS['body_large'],
            fg=COLORS['text_secondary']
        )
        self.image_label.pack(pady=20)
        
        self.name_label = tk.Label(
            image_frame,
            text="Produktname",
            font=FONTS['heading_large'],
            fg=COLORS['text_primary'],
            bg='white',
            anchor='center'
        )
        self.name_label.pack(pady=(0, 15))

    def create_details_section(self, parent):
        """Erstellt den Detailbereich - angepasst für WhatsApp-Style"""
        details_container = tk.Frame(parent, bg='white', relief='solid', bd=1)
        details_container.pack(fill="x", pady=(0, 15))
        
        details_frame = tk.Frame(details_container, bg='white')
        details_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        rating_frame = tk.Frame(details_frame, bg='white')
        rating_frame.pack(fill="x", pady=(0, 15))
        
        rating_stars = tk.Label(
            rating_frame,
            text="⭐⭐⭐⭐⭐",
            font=FONTS['body_medium'],
            fg=COLORS['accent_gold'],
            bg='white'
        )
        rating_stars.pack(side="left")
        
        rating_text = tk.Label(
            rating_frame,
            text="4.8 von 5 Sternen (127 Bewertungen)",
            font=FONTS['body_medium'],
            fg=COLORS['accent_blue'],
            bg='white',
            cursor='hand2'
        )
        rating_text.pack(side="left", padx=(10, 0))
        
        separator1 = tk.Frame(details_frame, height=1, bg=COLORS['border_light'])
        separator1.pack(fill="x", pady=15)
        
        price_frame = tk.Frame(details_frame, bg='white')
        price_frame.pack(fill="x", pady=(0, 20))
        
        self.price_label = tk.Label(
            price_frame,
            text="1,50 €",
            font=('Arial', 28, 'bold'),
            fg=COLORS['text_primary'],
            bg='white',
            anchor='w'
        )
        self.price_label.pack(anchor="w")
        
        price_details = tk.Label(
            price_frame,
            text="Inkl. MwSt. • Frisch gebacken",
            font=FONTS['caption'],
            fg=COLORS['text_secondary'],
            bg='white',
            anchor='w'
        )
        price_details.pack(anchor="w", pady=(5, 0))
        
        availability_frame = tk.Frame(details_frame, bg='white')
        availability_frame.pack(fill="x", pady=(10, 20))
        
        availability_label = tk.Label(
            availability_frame,
            text="✅ Auf Lager - sofort verfügbar",
            font=FONTS['body_medium'],
            fg=COLORS['button_success'],
            bg='white',
            anchor='w'
        )
        availability_label.pack(anchor="w")
        
        delivery_info = tk.Label(
            availability_frame,
            text="🚀 Sofortige Ausgabe nach Bezahlung",
            font=FONTS['body_medium'],
            fg=COLORS['text_secondary'],
            bg='white',
            anchor='w'
        )
        delivery_info.pack(anchor="w", pady=(5, 0))
        
        separator2 = tk.Frame(details_frame, height=1, bg=COLORS['border_light'])
        separator2.pack(fill="x", pady=20)
        
        self.create_description_section(details_frame)
        
        separator3 = tk.Frame(details_frame, height=1, bg=COLORS['border_light'])
        separator3.pack(fill="x", pady=20)
        
        self.create_purchase_section(details_frame)
        
        self.create_additional_info(parent)

    def create_description_section(self, parent):
        desc_frame = tk.Frame(parent, bg='white')
        desc_frame.pack(fill="x", pady=(0, 15))
        
        desc_title = tk.Label(
            desc_frame,
            text="Über dieses Produkt:",
            font=FONTS['heading_small'],
            fg=COLORS['text_primary'],
            bg='white',
            anchor='w'
        )
        desc_title.pack(anchor="w", pady=(0, 10))
        
        self.desc_label = tk.Label(
            desc_frame,
            text="Beschreibung wird geladen...",
            font=FONTS['body_medium'],
            fg=COLORS['text_primary'],
            bg='white',
            anchor='w',
            justify='left',
            wraplength=450
        )
        self.desc_label.pack(anchor="w", fill="x")

    def create_purchase_section(self, parent):
        purchase_frame = tk.Frame(parent, bg=COLORS['background_hover'], relief='solid', bd=1)
        purchase_frame.pack(fill="x", pady=(0, 20))
        
        purchase_content = tk.Frame(purchase_frame, bg=COLORS['background_hover'])
        purchase_content.pack(fill="both", expand=True, padx=20, pady=20)
        
        quantity_frame = tk.Frame(purchase_content, bg=COLORS['background_hover'])
        quantity_frame.pack(fill="x", pady=(0, 15))
        
        qty_label = tk.Label(
            quantity_frame,
            text="Menge:",
            font=FONTS['body_medium'],
            fg=COLORS['text_primary'],
            bg=COLORS['background_hover']
        )
        qty_label.pack(side="left")
        
        self.qty_var = tk.IntVar(value=1)
        qty_spinbox = tk.Spinbox(
            quantity_frame,
            from_=1,
            to=10,
            textvariable=self.qty_var,
            width=8,
            font=FONTS['body_medium'],
            relief='solid',
            bd=1,
            bg='white'
        )
        qty_spinbox.pack(side="left", padx=(10, 0))
        
        self.total_price_label = tk.Label(
            purchase_content,
            text="Gesamtpreis: 1,50 €",
            font=FONTS['heading_small'],
            fg=COLORS['button_success'],
            bg=COLORS['background_hover'],
            anchor='w'
        )
        self.total_price_label.pack(anchor="w", pady=(0, 20))
        
        button_frame = tk.Frame(purchase_content, bg=COLORS['background_hover'])
        button_frame.pack(fill="x")
        
        add_to_cart_btn = create_modern_button(
            button_frame,
            "🛒 In den Warenkorb",
            style='cart',
            command=self.add_to_cart
        )
        add_to_cart_btn.pack(fill="x", pady=(0, 10))
        
        buy_now_btn = create_modern_button(
            button_frame,
            "⚡ Jetzt kaufen",
            style='gold',
            command=self.buy_now
        )
        buy_now_btn.pack(fill="x")
        
        back_btn = create_modern_button(
            purchase_content,
            "← Zurück zur Übersicht",
            style='secondary',
            command=lambda: self.controller.show_frame("HomePage")
        )
        back_btn.pack(pady=(20, 0))

    def create_additional_info(self, parent):
        # (unchanged content omitted for brevity in this snippet)
        pass  # UI unchanged (keep your original implementation)

    def update_page(self, product):
        """Aktualisiert die Seite mit Produktdaten"""
        # akzeptiere sowohl Dicts (neu) als auch Tupel aus DB (falls irgendwo noch Tupel übergeben werden)
        if product is None:
            return

        # falls ein DB-Row-Tupel übergeben wurde, wandle um (id, name, preis, beschreibung)
        if isinstance(product, tuple) or isinstance(product, list):
            # hole Felder falls vorhanden
            try:
                prod_id, name, preis, beschreibung = product[0], product[1], product[2], product[3]
                product = {
                    "id": prod_id,
                    "name": name,
                    "price": float(preis),
                    "description": beschreibung if beschreibung is not None else "",
                    "image": f"assets/{name}.png"
                }
            except Exception:
                # fallback: versuche einfache Indexzugriffe
                pass

        self.product = product

        # Breadcrumb aktualisieren
        self.product_breadcrumb.configure(text=product["name"])

        # Produktbild laden
        self.load_product_image(product)

        # Produktname
        self.name_label.configure(text=product["name"])

        # Preis
        price_text = f"{product.get('price', 0):.2f} €"
        self.price_label.configure(text=price_text)

        # Beschreibung
        description = product.get('description', f'Leckere {product["name"]} – frisch gebacken!')
        self.desc_label.configure(text=description)

        # Gesamtpreis initial berechnen
        self.update_total_price()

        # Menge-Änderung überwachen
        self.qty_var.trace('w', lambda *args: self.update_total_price())

    def load_product_image(self, product):
        """Lädt und skaliert das Produktbild"""
        try:
            image_path = product.get("image", f"assets/{product['name']}.png")
            img = Image.open(image_path)
            img.thumbnail((400, 400), Image.Resampling.LANCZOS)
            self.product_image = ImageTk.PhotoImage(img)
            self.image_label.configure(
                image=self.product_image,
                text="",
                compound='center'
            )
        except Exception as e:
            print(f"Fehler beim Laden des Produktbilds: {e}")
            self.image_label.configure(
                text=f"📷\n{product['name']}\nBild nicht verfügbar",
                image="",
                font=FONTS['body_large'],
                fg=COLORS['text_secondary']
            )

    def update_total_price(self):
        """Aktualisiert den Gesamtpreis basierend auf der Menge"""
        if self.product and 'price' in self.product:
            quantity = self.qty_var.get()
            total = self.product['price'] * quantity
            self.total_price_label.configure(text=f"Gesamtpreis: {total:.2f} €")

    def add_to_cart(self):
        """Fügt Produkt zum Warenkorb hinzu"""
        if self.product:
            name = self.product["name"]
            qty = self.qty_var.get()
            
            # Zur bestehenden Menge hinzufügen
            if name in self.controller.cart:
                self.controller.cart[name] += qty
            else:
                self.controller.cart[name] = qty
            
            # Feedback anzeigen
            print(f"✅ {qty}x {name} zum Warenkorb hinzugefügt")
            
            # Warenkorb-Info aktualisieren
            if hasattr(self.controller, "update_cart_info"):
                try:
                    self.controller.update_cart_info()
                except Exception:
                    pass
            
            # Zur Startseite zurück
            self.controller.show_frame("HomePage")

    def buy_now(self):
        """Direktkauf - fügt zum Warenkorb hinzu und geht zum Checkout"""
        if self.product:
            self.add_to_cart()
            self.controller.show_frame("CartPage")
