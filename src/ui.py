# ui.py - Handles UI components using Tkinter

import tkinter as tk
from tkinter import messagebox
from menu import menu
from order_manger import place_order, get_total_revenue, get_unique_customers
from utils import show_bill, show_message

def start_app():
    """Launches the Tkinter UI."""
    root = tk.Tk()
    root.title("Online Food Delivery System")
    root.geometry("500x500")

    # Heading
    tk.Label(root, text="Welcome to Food Order System", font=("Arial", 16, "bold")).pack(pady=10)

    # Customer Name Entry
    tk.Label(root, text="Enter Customer Name:").pack()
    customer_entry = tk.Entry(root)
    customer_entry.pack()

    # Item Selection
    tk.Label(root, text="Select Items:").pack()
    selected_items = {item: tk.IntVar() for item in menu.keys()}
    for item in menu.keys():
        tk.Checkbutton(root, text=f"{item} - ${menu[item][0]:.2f}", variable=selected_items[item]).pack(anchor="w")

    # Order Button Function
    def order_food():
        customer_name = customer_entry.get().strip()
        chosen_items = [item for item, var in selected_items.items() if var.get() == 1]

        order_details, error = place_order(customer_name, chosen_items)
        if error:
            messagebox.showerror("Error", error)
        else:
            show_bill(order_details, menu)

    # Buttons
    tk.Button(root, text="Place Order", command=order_food, bg="green", fg="white").pack(pady=10)
    tk.Button(root, text="Show Total Revenue", command=lambda: show_message("Total Revenue", f"Total Revenue: ${get_total_revenue():.2f}"), bg="blue", fg="white").pack(pady=5)
    tk.Button(root, text="Show Unique Customers", command=lambda: show_message("Unique Customers", "\n".join(get_unique_customers()) or "No customers yet!"), bg="orange", fg="white").pack(pady=5)

    root.mainloop()
