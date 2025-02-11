# utils.py - Utility functions for bill display and statistics

import tkinter as tk
from tkinter import messagebox

def show_bill(order_details, menu):
    """Displays the bill in a new pop-up window."""
    order_id, customer_name, items, total, discount, order_time = order_details
    order_date, order_time = order_time.split(" ")

    bill_window = tk.Toplevel()
    bill_window.title("Bill Receipt")
    bill_window.geometry("300x300")

    tk.Label(bill_window, text="Bill Receipt", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(bill_window, text=f"Order ID: {order_id}", font=("Arial", 12)).pack()
    tk.Label(bill_window, text=f"Customer: {customer_name}", font=("Arial", 12)).pack()
    tk.Label(bill_window, text=f"Order Date: {order_date}", font=("Arial", 12)).pack()
    tk.Label(bill_window, text=f"Order Time: {order_time}", font=("Arial", 12)).pack()

    tk.Label(bill_window, text="Items Ordered:", font=("Arial", 12, "underline")).pack()
    for item, quantity in items:
        tk.Label(bill_window, text=f"- {item} (x{quantity}) - ${menu[item][0] * quantity:.2f}").pack()

    tk.Label(bill_window, text=f"Discount: ${discount:.2f}", font=("Arial", 12)).pack()
    tk.Label(bill_window, text=f"\nTotal: ${total:.2f}", font=("Arial", 14, "bold")).pack(pady=10)

def show_message(title, message):
    """Displays an information message box."""
    messagebox.showinfo(title, message)