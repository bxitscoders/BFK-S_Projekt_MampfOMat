import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

PRODUCTS = [
    {"id": 1, "name": "Croissant", "price": 2.20, "description": "Zartblättriges Buttercroissant."},
    {"id": 2, "name": "Brezel", "price": 1.50, "description": "Frisch gebackene Brezel."},
    {"id": 3, "name": "Muffin", "price": 2.50, "description": "Saftiger Muffin."},
]

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f5f5f5")
        self.controller = controller

        tk.Label(self, text="🛠️ Adminbereich", font=("Segoe UI", 20, "bold"), bg="#f5f5f5").pack(pady=20)
        self.products_frame = tk.Frame(self, bg="#f5f5f5")
        self.products_frame.pack()

        self.images = []
        self.load_products()

        tk.Button(self, text="➕ Neues Produkt", bg="#ffd966", relief="flat",
                  command=self.add_product_window).pack(pady=10)
        tk.Button(self, text="⬅️ Zurück", bg="#ddd", relief="flat",
                  command=lambda: controller.show_frame("HomePage")).pack(pady=5)

    def load_products(self):
        for widget in self.products_frame.winfo_children():
            widget.destroy()
        self.images.clear()

        for i, product in enumerate(PRODUCTS):
            frame = tk.Frame(self.products_frame, bg="white", relief="solid", bd=1)
            frame.grid(row=i // 3, column=i % 3, padx=20, pady=20, ipadx=10, ipady=10)
            img = Image.open(f"assets/{product['name']}.png").resize((120, 120))
            tk_img = ImageTk.PhotoImage(img)
            self.images.append(tk_img)

            tk.Label(frame, image=tk_img, bg="white").pack()
            tk.Label(frame, text=f"{product['name']} ({product['price']}€)", font=("Segoe UI", 11, "bold"), bg="white").pack()
            tk.Button(frame, text="Bearbeiten", bg="#ddd", relief="flat",
                      command=lambda p=product: self.edit_product(p)).pack(pady=5)

    def edit_product(self, product):
        win = tk.Toplevel(self)
        win.title("Produkt bearbeiten")
        win.geometry("300x300")
        tk.Label(win, text="Produkt bearbeiten", font=("Segoe UI", 14, "bold")).pack(pady=10)

        name_var = tk.StringVar(value=product["name"])
        price_var = tk.DoubleVar(value=product["price"])
        desc_var = tk.StringVar(value=product["description"])

        for lbl, var in [("Name", name_var), ("Preis", price_var), ("Beschreibung", desc_var)]:
            tk.Label(win, text=lbl).pack()
            tk.Entry(win, textvariable=var).pack(pady=2)

        def save():
            product["name"] = name_var.get()
            product["price"] = price_var.get()
            product["description"] = desc_var.get()
            self.load_products()
            win.destroy()
            messagebox.showinfo("Gespeichert", "Produkt aktualisiert!")

        tk.Button(win, text="Speichern", bg="#ffd966", relief="flat", command=save).pack(pady=10)

    def add_product_window(self):
        win = tk.Toplevel(self)
        win.title("Produkt hinzufügen")
        win.geometry("300x300")
        tk.Label(win, text="Neues Produkt", font=("Segoe UI", 14, "bold")).pack(pady=10)

        name_var, price_var, desc_var = tk.StringVar(), tk.DoubleVar(), tk.StringVar()
        for lbl, var in [("Name", name_var), ("Preis", price_var), ("Beschreibung", desc_var)]:
            tk.Label(win, text=lbl).pack()
            tk.Entry(win, textvariable=var).pack(pady=2)

        def add():
            new = {"id": len(PRODUCTS)+1, "name": name_var.get(), "price": price_var.get(), "description": desc_var.get()}
            PRODUCTS.append(new)
            self.load_products()
            win.destroy()
            messagebox.showinfo("Hinzugefügt", "Neues Produkt angelegt!")

        tk.Button(win, text="Hinzufügen", bg="#ffd966", relief="flat", command=add).pack(pady=10)
