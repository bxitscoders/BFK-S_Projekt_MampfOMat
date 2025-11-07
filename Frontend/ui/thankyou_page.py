import tkinter as tk

class ThankYouPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f5f5f5")

        tk.Label(self, text="🙏 Vielen Dank für Ihre Bestellung!", font=("Segoe UI", 20, "bold"), bg="#f5f5f5").pack(pady=40)
        tk.Label(self, text="Gleich kommt Ihr Produkt heraus 😋", font=("Segoe UI", 14), bg="#f5f5f5").pack(pady=10)
        tk.Button(self, text="Zurück zur Startseite", bg="#ffd966", relief="flat",
                  command=lambda: controller.show_frame("HomePage")).pack(pady=30)
