import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from ui.product_data import get_all_products
from ui.modern_styles import COLORS, FONTS, LAYOUT, create_modern_button, create_modern_card, apply_hover_effect

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#ffffff')  # Zurück zu elegantem Weiß
        self.controller = controller
        self.images = []
        self.product_cards = []
        
        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        """Erstellt die moderne Homepage-UI"""
        # Hauptcontainer mit Grid-Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Hero-Sektion
        self.create_hero_section()
        
        # Produktbereich
        self.create_products_section()
        
        # Footer mit Admin-Login
        self.create_footer()

    def create_hero_section(self):
        """Erstellt den Hero-Bereich mit Premium-Design"""
        hero_frame = tk.Frame(
            self,
            bg=COLORS['background_main'],
            height=120
        )
        hero_frame.grid(row=0, column=0, sticky="ew", padx=LAYOUT['padding_large'], pady=LAYOUT['padding_large'])
        hero_frame.grid_propagate(False)
        hero_frame.grid_columnconfigure(0, weight=1)
        
        # Haupttitel
        title_label = tk.Label(
            hero_frame,
            text="Frische Backwaren",
            font=FONTS['heading_large'],
            fg=COLORS['text_primary'],
            bg=COLORS['background_main']
        )
        title_label.grid(row=0, column=0, pady=(LAYOUT['padding_medium'], 0))
        
        # Untertitel
        subtitle_label = tk.Label(
            hero_frame,
            text="Wählen Sie aus unserer exquisiten Auswahl an frisch gebackenen Produkten",
            font=FONTS['body_large'],
            fg=COLORS['text_secondary'],
            bg=COLORS['background_main']
        )
        subtitle_label.grid(row=1, column=0, pady=(LAYOUT['padding_small'], 0))

    def create_products_section(self):
        """Erstellt den modernen Produktbereich"""
        # Container für Produktkarten
        products_container = tk.Frame(self, bg='#ffffff')  # Elegantes Weiß
        products_container.grid(row=1, column=0, sticky="nsew", padx=LAYOUT['padding_large'])
        products_container.grid_columnconfigure(0, weight=1)
        products_container.grid_rowconfigure(0, weight=1)
        
        # Scrollbarer Bereich - verbessertes Scrolling
        canvas = tk.Canvas(
            products_container,
            bg='#ffffff',
            highlightthickness=0,
            bd=0
        )
        scrollbar = tk.Scrollbar(
            products_container,
            orient="vertical",
            command=canvas.yview,
            bg=COLORS['accent_silver'],
            width=12
        )
        
        self.products_frame = tk.Frame(canvas, bg='#ffffff')
        
        # Scrollbar konfigurieren
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Layout
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Frame im Canvas platzieren
        self.canvas_window = canvas.create_window((0, 0), window=self.products_frame, anchor="nw")
        
        # Verbesserte Scroll-Konfiguration
        def configure_scroll_region(event=None):
            # Scroll-Region aktualisieren
            canvas.configure(scrollregion=canvas.bbox("all"))
            
            # Frame-Breite an Canvas anpassen für responsives Verhalten
            if canvas.winfo_width() > 1:
                canvas.itemconfig(self.canvas_window, width=canvas.winfo_width())
        
        # Event-Bindings
        self.products_frame.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", configure_scroll_region)
        
        # Verbessertes Mausrad-Scrolling
        def on_mousewheel(event):
            # Nur scrollen wenn Maus über Canvas ist
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            return "break"  # Event nicht weiterleiten
        
        # Mausrad-Events besser binden
        def bind_mousewheel(event):
            canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        def unbind_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
        
        # Nur bei Mouse-Over scrollen aktivieren
        canvas.bind('<Enter>', bind_mousewheel)
        canvas.bind('<Leave>', unbind_mousewheel)
        
        # Speichere Canvas-Referenz für andere Methoden
        self.canvas = canvas

    def create_footer(self):
        """Erstellt den Footer mit Admin-Login"""
        footer_frame = tk.Frame(
            self,
            bg=COLORS['background_main'],
            height=80
        )
        footer_frame.grid(row=2, column=0, sticky="ew", padx=LAYOUT['padding_large'], pady=LAYOUT['padding_medium'])
        footer_frame.grid_propagate(False)
        footer_frame.grid_columnconfigure(1, weight=1)
        
        # Admin-Login Button (links)
        admin_btn = create_modern_button(
            footer_frame,
            "Administrator Anmeldung",
            style='secondary',
            command=self.open_login
        )
        admin_btn.grid(row=0, column=0, sticky="w")

    def load_products(self):
        """Lädt alle Produkte mit modernem Card-Design"""
        # Bestehende Cards entfernen
        for card in self.product_cards:
            card.destroy()
        self.product_cards.clear()
        self.images.clear()

        # Aktuelle Produktliste laden
        products = get_all_products()
        
        # Grid-Layout für Produktkarten (responsive)
        cols = 3  # Anzahl Spalten
        for i, product in enumerate(products):
            row = i // cols
            col = i % cols
            
            # Produktkarte erstellen (gibt jetzt Container zurück)
            card_container = self.create_product_card(product)
            card_container.grid(
                row=row,
                column=col,
                padx=LAYOUT['padding_medium'],
                pady=LAYOUT['padding_medium'],
                sticky="ew"
            )
            self.product_cards.append(card_container)
        
        # Spalten gleichmäßig verteilen
        for col in range(cols):
            self.products_frame.grid_columnconfigure(col, weight=1, uniform="product_col")

    def create_product_card(self, product):
        """Erstellt eine moderne Produktkarte mit flüssigem Schatten-Hover-Effekt"""
        card = create_modern_card(self.products_frame)
        
        # Card-Layout konfigurieren - optimierte Größe für bessere Proportionen
        card.configure(width=320, height=380)
        card.grid_propagate(False)
        card.grid_columnconfigure(0, weight=1)
        
        # Animation-Eigenschaften für Schatten-Effekt
        card.shadow_intensity = 0
        card.max_shadow_intensity = 8
        card.animation_id = None
        card.is_hovering = False
        
        try:
            # Produktbild laden und optimieren
            image_path = product.get("image", f"assets/{product['name']}.png")
            img = Image.open(image_path)
            
            # Bessere Proportionen - quadratischer Ansatz
            img_width, img_height = img.size
            target_ratio = 1.2  # Leicht rechteckig für natürlicheren Look
            current_ratio = img_width / img_height
            
            if current_ratio > target_ratio:
                new_width = int(img_height * target_ratio)
                left = (img_width - new_width) // 2
                img = img.crop((left, 0, left + new_width, img_height))
            else:
                new_height = int(img_width / target_ratio)
                top = (img_height - new_height) // 2
                img = img.crop((0, top, img_width, top + new_height))
            
            # Größeres Bild für bessere Darstellung
            img_resized = img.resize((280, 220), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img_resized)
            
            self.images.append(tk_img)
            
            # Speichere Bild für Hover-Effekt
            card.product_image = tk_img
            
            # Bild-Label
            img_label = tk.Label(
                card,
                image=tk_img,
                bg=COLORS['background_card'],
                bd=0,  # Kein Border für smootheren Look
                relief='flat'
            )
            img_label.grid(row=0, column=0, pady=(LAYOUT['padding_medium'], LAYOUT['padding_small']))
            card.img_label = img_label  # Referenz speichern
            
        except Exception as e:
            print(f"Fehler beim Laden des Produktbilds {product['name']}: {e}")
            placeholder_label = tk.Label(
                card,
                text="📷",
                font=FONTS['heading_medium'],
                fg=COLORS['text_secondary'],
                bg=COLORS['background_hover'],
                width=35,
                height=8
            )
            placeholder_label.grid(row=0, column=0, pady=(LAYOUT['padding_medium'], LAYOUT['padding_small']))
            card.img_label = placeholder_label
            card.product_image = None
        
        # Produktname
        name_label = tk.Label(
            card,
            text=product["name"],
            font=FONTS['heading_small'],
            fg=COLORS['text_primary'],
            bg=COLORS['background_card']
        )
        name_label.grid(row=1, column=0, pady=(0, LAYOUT['padding_small']))
        
        # Preis
        if 'price' in product:
            price_frame = tk.Frame(card, bg=COLORS['background_card'])
            price_frame.grid(row=2, column=0, pady=(0, LAYOUT['padding_small']))
            
            price_label = tk.Label(
                price_frame,
                text=f"{product['price']:.2f} €",
                font=FONTS['heading_small'],
                fg=COLORS['button_success'],
                bg=COLORS['background_card']
            )
            price_label.pack()
            
            price_hint = tk.Label(
                price_frame,
                text="pro Stück",
                font=FONTS['caption'],
                fg=COLORS['text_secondary'],
                bg=COLORS['background_card']
            )
            price_hint.pack()
        
        # Beschreibung
        if 'description' in product and product['description']:
            desc_text = product['description']
            if len(desc_text) > 60:
                desc_text = desc_text[:57] + "..."
            
            desc_label = tk.Label(
                card,
                text=desc_text,
                font=FONTS['body_medium'],
                fg=COLORS['text_secondary'],
                bg=COLORS['background_card'],
                wraplength=280,
                justify='center'
            )
            desc_label.grid(row=3, column=0, pady=(0, LAYOUT['padding_medium']))
        
        # Auswählen-Button - Premium Gold Style
        select_btn = tk.Button(
            card,
            text="AUSWÄHLEN",
            font=FONTS['button'],
            bg=COLORS['button_gold'],
            fg=COLORS['primary_dark'],
            relief='raised',
            bd=2,
            padx=30,
            pady=14,
            cursor='hand2',
            activebackground=COLORS['button_gold_hover'],
            activeforeground=COLORS['text_light'],
            command=lambda: self.controller.show_frame("ProductPage", product=product)
        )
        select_btn.grid(row=4, column=0, pady=(LAYOUT['padding_small'], LAYOUT['padding_medium']))
        
        # Button Hover-Effekt - vereinfacht
        def on_btn_enter(event):
            select_btn.configure(
                bg=COLORS['button_gold_hover'], 
                fg=COLORS['text_light'],
                relief='raised',
                bd=3
            )
        
        def on_btn_leave(event):
            select_btn.configure(
                bg=COLORS['button_gold'], 
                fg=COLORS['primary_dark'],
                relief='raised',
                bd=2
            )
        
        select_btn.bind("<Enter>", on_btn_enter)
        select_btn.bind("<Leave>", on_btn_leave)
        
        # Events binden - vereinfacht für bessere Performance
        def card_hover_in(event):
            if not card.is_hovering:
                card.is_hovering = True
                # Einfacher visueller Effekt ohne Animation
                card.configure(
                    bg=COLORS['background_hover'],
                    highlightbackground=COLORS['button_gold'],
                    highlightthickness=2,
                    relief='raised'
                )
                self.update_card_background(card, COLORS['background_hover'])
        
        def card_hover_out(event):
            if card.is_hovering:
                card.is_hovering = False
                # Zurücksetzen ohne Animation
                card.configure(
                    bg=COLORS['background_card'],
                    highlightbackground=COLORS['border_light'],
                    highlightthickness=1,
                    relief='flat'
                )
                self.update_card_background(card, COLORS['background_card'])
        
        # Direkte Event-Bindung ohne komplexe Weiterleitung
        card.bind("<Enter>", card_hover_in)
        card.bind("<Leave>", card_hover_out)
        
        # Klick-Event für sofortige Responsivität - NACH allen Element-Erstellungen
        def card_click(event):
            # Sofort zur Produktseite ohne Verzögerung
            self.controller.show_frame("ProductPage", product=product)
            return "break"  # Event nicht weiterleiten
        
        # Alle Elemente der Karte klickbar machen für beste Performance
        clickable_elements = [card]
        
        # Bild klickbar machen
        if hasattr(card, 'img_label'):
            clickable_elements.append(card.img_label)
        
        # Name klickbar machen
        clickable_elements.append(name_label)
        
        # Preis klickbar machen falls vorhanden
        if 'price' in product and 'price_label' in locals():
            clickable_elements.extend([price_label, price_hint])
            
        # Beschreibung klickbar machen falls vorhanden
        if 'description' in product and product['description'] and 'desc_label' in locals():
            clickable_elements.append(desc_label)
        
        # Click-Events und Cursor für alle Elemente setzen
        for element in clickable_elements:
            try:
                element.bind("<Button-1>", card_click)
                element.configure(cursor='hand2')
            except:
                pass  # Ignoriere Elemente die cursor nicht unterstützen
        
        return card
    
    def update_card_background(self, widget, color):
        """Aktualisiert den Hintergrund aller Widgets in einer Karte"""
        try:
            if hasattr(widget, 'configure'):
                widget.configure(bg=color)
            for child in widget.winfo_children():
                self.update_card_background(child, color)
        except:
            pass  # Ignoriere Widgets die bg nicht unterstützen

    def open_login(self):
        """Öffnet das moderne Login-Fenster"""
        popup = tk.Toplevel(self)
        popup.title("Administrator Anmeldung")
        popup.geometry("450x350")
        popup.resizable(False, False)
        popup.configure(bg=COLORS['background_main'])
        popup.grab_set()
        popup.transient(self.controller)
        
        # Zentriere das Popup
        popup.update_idletasks()
        x = (popup.winfo_screenwidth() // 2) - (450 // 2)
        y = (popup.winfo_screenheight() // 2) - (350 // 2)
        popup.geometry(f"450x350+{x}+{y}")
        
        # Header
        header_frame = tk.Frame(popup, bg=COLORS['primary_dark'], height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="Administrator",
            font=FONTS['heading_medium'],
            fg=COLORS['text_light'],
            bg=COLORS['primary_dark']
        )
        title_label.pack(pady=LAYOUT['padding_large'])
        
        # Formular-Bereich
        form_frame = tk.Frame(popup, bg=COLORS['background_main'])
        form_frame.pack(fill="both", expand=True, padx=LAYOUT['padding_xlarge'], pady=LAYOUT['padding_large'])
        
        # Benutzername
        tk.Label(
            form_frame,
            text="Benutzername",
            font=FONTS['body_large'],
            fg=COLORS['text_primary'],
            bg=COLORS['background_main']
        ).pack(anchor="w", pady=(0, LAYOUT['padding_small']))
        
        username_var = tk.StringVar()
        username_entry = tk.Entry(
            form_frame,
            textvariable=username_var,
            font=FONTS['body_large'],
            relief='flat',
            bd=1,
            highlightthickness=1,
            highlightcolor=COLORS['text_accent'],
            highlightbackground=COLORS['border_light']
        )
        username_entry.pack(fill="x", pady=(0, LAYOUT['padding_medium']), ipady=LAYOUT['padding_small'])
        
        # Passwort
        tk.Label(
            form_frame,
            text="Passwort",
            font=FONTS['body_large'],
            fg=COLORS['text_primary'],
            bg=COLORS['background_main']
        ).pack(anchor="w", pady=(0, LAYOUT['padding_small']))
        
        password_var = tk.StringVar()
        password_entry = tk.Entry(
            form_frame,
            textvariable=password_var,
            show="*",
            font=FONTS['body_large'],
            relief='flat',
            bd=1,
            highlightthickness=1,
            highlightcolor=COLORS['text_accent'],
            highlightbackground=COLORS['border_light']
        )
        password_entry.pack(fill="x", pady=(0, LAYOUT['padding_medium']), ipady=LAYOUT['padding_small'])
        
        # Status-Label für Fehlermeldungen
        status_label = tk.Label(
            form_frame,
            text="",
            font=FONTS['body_medium'],
            fg=COLORS['button_danger'],
            bg=COLORS['background_main']
        )
        status_label.pack(pady=(0, LAYOUT['padding_medium']))
        
        def try_login():
            """Überprüft die Anmeldedaten"""
            username = username_var.get().strip()
            password = password_var.get().strip()
            
            if username == "admin" and password == "admin":
                popup.destroy()
                self.controller.show_frame("AdminPage")
                messagebox.showinfo(
                    "Login erfolgreich",
                    "Sie wurden erfolgreich als Administrator angemeldet."
                )
            else:
                status_label.config(text="Ungültige Anmeldedaten. Bitte versuchen Sie es erneut.")
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                username_entry.focus()
        
        # Button-Bereich
        button_frame = tk.Frame(form_frame, bg=COLORS['background_main'])
        button_frame.pack(fill="x", pady=LAYOUT['padding_large'])
        
        # Anmelden Button
        login_btn = create_modern_button(
            button_frame,
            "Anmelden",
            style='primary',
            command=try_login
        )
        login_btn.pack(side="left", padx=(0, LAYOUT['padding_small']))
        
        # Abbrechen Button
        cancel_btn = create_modern_button(
            button_frame,
            "Abbrechen",
            style='secondary',
            command=popup.destroy
        )
        cancel_btn.pack(side="left")
        
        # Enter-Taste für Login
        popup.bind('<Return>', lambda event: try_login())
        username_entry.focus()

    def update_page(self, **kwargs):
        """Aktualisiert die Seite"""
        self.load_products()

