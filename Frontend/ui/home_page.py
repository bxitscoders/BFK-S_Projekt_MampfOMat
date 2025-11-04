import tkinter as tk
from tkinter import PhotoImage

PRODUCTS = [
    {"name": "Brezel", "image": "assets/Brezel.png"},
    {"name": "Croissant", "image": "assets/Croissant.png"},
    {"name": "Brötchen", "image": "assets/Broetchen.png"},
    {"name": "Käsebrötchen", "image": "assets/Kaesebroetchen.png"},
    {"name": "Muffin", "image": "assets/Muffin.png"},
    {"name": "Berliner", "image": "assets/Berliner.png"},
]

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="🍞 Willkommen beim Bäckerautomaten 🍩", font=("Arial", 18)).pack(pady=20)
        self.products_frame = tk.Frame(self)
        self.products_frame.pack()

        self.images = []
        for i, product in enumerate(PRODUCTS):
            img = PhotoImage(file=product["image"]).subsample(4, 4)
            self.images.append(img)  # sonst wird Bild gelöscht
            btn = tk.Button(
                self.products_frame,
                image=img,
                text=product["name"],
                compound="top",
                command=lambda p=product: controller.show_frame("ProductPage", product=p),
                width=180, height=160
            )
            btn.grid(row=i//3, column=i%3, padx=20, pady=20)
