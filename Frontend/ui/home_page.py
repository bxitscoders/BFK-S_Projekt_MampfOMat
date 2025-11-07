import tkinter as tk
from PIL import Image, ImageTk

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
        super().__init__(parent, bg="#f5f5f5")
        self.controller = controller
        self.images = []

        title = tk.Label(self, text="🥐 Willkommen beim Bäckerautomaten 🧁",
                         font=("Segoe UI", 22, "bold"), bg="#f5f5f5", fg="#333")
        title.pack(pady=30)

        # Produktgrid
        self.grid_frame = tk.Frame(self, bg="#f5f5f5")
        self.grid_frame.pack(expand=True)

        for i, product in enumerate(PRODUCTS):
            img = Image.open(product["image"])
            img = img.resize((140, 140))
            tk_img = ImageTk.PhotoImage(img)
            self.images.append(tk_img)

            card = tk.Frame(self.grid_frame, bg="white", relief="raised", bd=2)
            card.grid(row=i // 3, column=i % 3, padx=25, pady=25, ipadx=10, ipady=10)

            lbl_img = tk.Label(card, image=tk_img, bg="white")
            lbl_img.pack()
            lbl_name = tk.Label(card, text=product["name"], font=("Segoe UI", 13, "bold"), bg="white")
            lbl_name.pack(pady=(5, 0))

            tk.Button(card, text="Ansehen", font=("Segoe UI", 11),
                      bg="#ffd966", relief="flat", cursor="hand2",
                      command=lambda p=product: controller.show_frame("ProductPage", product=p)
                      ).pack(pady=5)

        # Login unten links
        bottom = tk.Frame(self, bg="#f5f5f5")
        bottom.pack(fill="x", pady=15, padx=20)
        tk.Button(bottom, text="🔐 Admin Login", font=("Segoe UI", 11),
                  bg="#ddd", relief="flat", cursor="hand2",
                  command=lambda: controller.show_frame("AdminPage")).pack(side="left")
