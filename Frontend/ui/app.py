import tkinter as tk
from ui.home_page import HomePage
from ui.product_page import ProductPage
from ui.cart_page import CartPage
from ui.thankyou_page import ThankYouPage
from ui.admin_page import AdminPage

# Einheitliches helles Design
PRIMARY_COLOR = "#f5f5f5"
ACCENT_COLOR = "#f0c14b"
TEXT_COLOR = "#333"
FONT = ("Segoe UI", 12)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bäckerautomat – DNAKE")
        self.geometry("900x700")
        self.minsize(800, 600)
        self.config(bg=PRIMARY_COLOR)
        self.cart = {}

        # Container für Seiten
        self.container = tk.Frame(self, bg=PRIMARY_COLOR)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (HomePage, ProductPage, CartPage, ThankYouPage, AdminPage):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name, **kwargs):
        frame = self.frames[page_name]
        if hasattr(frame, "update_page"):
            frame.update_page(**kwargs)
        frame.tkraise()
