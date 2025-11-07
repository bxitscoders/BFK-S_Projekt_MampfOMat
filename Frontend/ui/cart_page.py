import tkinter as tk

class CartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f5f5f5")
        self.controller = controller

        tk.Label(self, text="🛒 Ihr Warenkorb", font=("Segoe UI", 20, "bold"), bg="#f5f5f5").pack(pady=25)
        self.cart_list = tk.Label(self, font=("Segoe UI", 13), bg="#f5f5f5", justify="left")
        self.cart_list.pack(pady=10)

        btn_frame = tk.Frame(self, bg="#f5f5f5")
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Zurück", bg="#ddd", relief="flat", command=lambda: controller.show_frame("HomePage")).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Bestellen", bg="#ffd966", relief="flat", command=lambda: controller.show_frame("ThankYouPage")).grid(row=0, column=1, padx=10)

    def update_page(self):
        text = ""
        total = 0
        for name, qty in self.controller.cart.items():
            price = 1.5 * qty
            total += price
            text += f"{name} × {qty} = {price:.2f}€\n"
        text += f"\nGesamt: {total:.2f}€"
        self.cart_list.config(text=text)
