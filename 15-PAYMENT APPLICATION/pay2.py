import tkinter as tk
from tkinter import messagebox

class PaymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment Application")
        
        # Variables to store user input
        self.amount_var = tk.StringVar()
        self.card_number_var = tk.StringVar()
        self.pin_var = tk.StringVar()
        
        # Entry fields for user input
        tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(root, text="Card Number:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.card_number_var).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(root, text="PIN:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.pin_var, show="*").grid(row=2, column=1, padx=5, pady=5)
        
        # Button to process payment
        tk.Button(root, text="Process Payment", command=self.process_payment).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    def process_payment(self):
        amount = self.amount_var.get()
        card_number = self.card_number_var.get()
        pin = self.pin_var.get()
        
        messagebox.showinfo("Payment", f"Payment of Rs.{amount} processed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
