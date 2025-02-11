# ui.py - Handles UI components using Tkinter

import tkinter as tk
from tkinter import simpledialog, messagebox
from menu import menu
from order_manger import place_order, get_total_revenue, get_unique_customers
from utils import show_bill, show_message

ADMIN_PASSWORD = "admin123"  # Set your admin password here

def start_app():
    """Launches the Tkinter UI."""
    root = tk.Tk()
    root.title("Online Food Delivery System")

    # Set a static window size
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")

    # Heading
    tk.Label(root, text="Welcome to Food Order System", font=("Arial", 20, "bold"), bg="#ff6347", fg="#ffffff").pack(pady=10)

    # Customer Name Entry
    customer_frame = tk.Frame(root, bg="#f0f0f0")
    customer_frame.pack(pady=5)
    tk.Label(customer_frame, text="Enter Customer Name:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    customer_entry = tk.Entry(customer_frame, font=("Arial", 12), bg="#e0ffff")
    customer_entry.grid(row=0, column=1, padx=5, pady=5)

    # Discount Code Entry
    tk.Label(customer_frame, text="Enter Discount Code (if any):", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    discount_entry = tk.Entry(customer_frame, font=("Arial", 12), bg="#e0ffff")
    discount_entry.grid(row=1, column=1, padx=5, pady=5)

    # Item Selection
    item_frame = tk.Frame(root, bg="#f0f0f0")
    item_frame.pack(pady=5)
    tk.Label(item_frame, text="Select Items and Quantities:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")

    selected_items = {item: tk.IntVar() for item in menu.keys()}
    quantities = {item: tk.IntVar(value=1) for item in menu.keys()}
    row = 1
    current_category = None
    for item, (price, category) in menu.items():
        if category != current_category:
            current_category = category
            tk.Label(item_frame, text=category, bg="#f0f0f0", font=("Arial", 14, "bold")).grid(row=row, column=0, padx=5, pady=5, sticky="w")
            row += 1
        tk.Checkbutton(item_frame, text=f"{item} - ${price:.2f}", variable=selected_items[item], bg="#f0f0f0", font=("Arial", 12)).grid(row=row, column=0, padx=5, pady=2, sticky="w")
        tk.Entry(item_frame, textvariable=quantities[item], width=5, font=("Arial", 12)).grid(row=row, column=1, padx=5, pady=2)
        row += 1

    # Order Button Function
    def order_food():
        customer_name = customer_entry.get().strip()
        discount_code = discount_entry.get().strip()
        chosen_items = [(item, quantities[item].get()) for item, var in selected_items.items() if var.get() == 1]

        order_details, error = place_order(customer_name, chosen_items, discount_code)
        if error:
            messagebox.showerror("Error", error)
        else:
            show_bill(order_details, menu)

    # Admin Authentication
    def authenticate_admin():
        password = simpledialog.askstring("Admin Authentication", "Enter admin password:", show='*')
        if password == ADMIN_PASSWORD:
            show_admin_panel()
        else:
            messagebox.showerror("Authentication Failed", "Incorrect password!")

    # Admin Panel
    def show_admin_panel():
        admin_window = tk.Toplevel(root)
        admin_window.title("Admin Panel")

        # Calculate the required height based on the number of unique customers
        num_customers = len(get_unique_customers())
        window_height = 200 + (num_customers * 20)
        admin_window.geometry(f"400x{window_height}")
        admin_window.configure(bg="#f0f0f0")

        total_revenue = get_total_revenue()
        unique_customers = get_unique_customers()

        tk.Label(admin_window, text="Admin Panel", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
        tk.Label(admin_window, text=f"Total Revenue: ${total_revenue:.2f}", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        tk.Label(admin_window, text="Unique Customers:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        for customer in unique_customers:
            tk.Label(admin_window, text=customer, font=("Arial", 12), bg="#f0f0f0").pack()

    # Buttons
    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=10)
    tk.Button(button_frame, text="Place Order", command=order_food, bg="#32cd32", fg="white", font=("Arial", 14)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Admin", command=authenticate_admin, bg="#ff4500", fg="white", font=("Arial", 14)).grid(row=0, column=1, padx=5, pady=5)

    root.mainloop()