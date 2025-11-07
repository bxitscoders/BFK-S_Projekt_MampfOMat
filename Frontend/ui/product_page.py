import tkinter as tk
from PIL import Image, ImageTk

class ProductPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f5f5f5")
        self.controller = controller
        self.product = None

        self.image_label = tk.Label(self, bg="#f5f5f5")
        self.image_label.pack(pady=20)

        self.name_label = tk.Label(self, font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#333")
        self.name_label.pack()
        self.desc_label = tk.Label(self, wraplength=500, bg="#f5f5f5", font=("Segoe UI", 12))
        self.desc_label.pack(pady=10)

        qty_frame = tk.Frame(self, bg="#f5f5f5")
        qty_frame.pack(pady=10)
        tk.Label(qty_frame, text="Menge:", bg="#f5f5f5", font=("Segoe UI", 12)).pack(side="left", padx=5)
        self.qty_var = tk.IntVar(value=1)
        tk.Entry(qty_frame, textvariable=self.qty_var, width=5, justify="center").pack(side="left")

        self.price_label = tk.Label(self, text="Preis: -- €", font=("Segoe UI", 14, "bold"), bg="#f5f5f5")
        self.price_label.pack(pady=5)

        btn_frame = tk.Frame(self, bg="#f5f5f5")
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Zurück", bg="#ddd", relief="flat", command=lambda: controller.show_frame("HomePage")).grid(row=0, column=0, padx=15)
        tk.Button(btn_frame, text="In den Warenkorb", bg="#ffd966", relief="flat",
                  command=self.add_to_cart).grid(row=0, column=1, padx=15)

    def update_page(self, product):
        self.product = product
        img = Image.open(product["image"]).resize((200, 200))
        tk_img = ImageTk.PhotoImage(img)
        self.image_label.config(image=tk_img)
        self.image_label.image = tk_img
        self.name_label.config(text=product["name"])
        self.desc_label.config(text=f"Leckere {product['name']} – frisch gebacken und ofenwarm!")
        self.price_label.config(text="Preis: 1.50 €")

    def add_to_cart(self):
        name = self.product["name"]
        qty = self.qty_var.get()
        self.controller.cart[name] = self.controller.cart.get(name, 0) + qty
        self.controller.show_frame("CartPage")
