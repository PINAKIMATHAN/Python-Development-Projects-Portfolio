import tkinter as tk
from tkinter import messagebox

class PaymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment Application")

        # Payment details
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0, sticky="w")
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)

        self.recipient_label = tk.Label(root, text="Recipient:")
        self.recipient_label.grid(row=1, column=0, sticky="w")
        self.recipient_entry = tk.Entry(root)
        self.recipient_entry.grid(row=1, column=1)

        self.purpose_label = tk.Label(root, text="Purpose:")
        self.purpose_label.grid(row=2, column=0, sticky="w")
        self.purpose_entry = tk.Entry(root)
        self.purpose_entry.grid(row=2, column=1)

        # Payment button
        self.pay_button = tk.Button(root, text="Make Payment", command=self.make_payment)
        self.pay_button.grid(row=3, column=0, columnspan=2)

    def make_payment(self):
        amount = self.amount_entry.get()
        recipient = self.recipient_entry.get()
        purpose = self.purpose_entry.get()

        messagebox.showinfo("Payment Details", f"Amount: {amount}\nRecipient: {recipient}\nPurpose: {purpose}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
