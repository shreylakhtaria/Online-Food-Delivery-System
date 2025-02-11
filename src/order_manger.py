# order_manager.py - Handles order management

from menu import menu
import openpyxl
from datetime import datetime

# List to store orders
orders = []

# Set to store unique customers
unique_customers = set()

# Variable to track total revenue
total_revenue = 0

# Discount codes
discount_codes = {
    "WELCOME10": 0.10,
    "WELCOME20": 0.20,
    "PYTHON30": 0.30
}

def place_order(customer_name, selected_items, discount_code=None):
    """Places an order and returns order details."""
    global total_revenue

    if not customer_name:
        return None, "Customer name cannot be empty!"

    if not selected_items:
        return None, "Please select at least one item!"

    total_bill = sum(menu[item][0] * quantity for item, quantity in selected_items)
    
    # Apply discount if valid code is provided
    discount = 0
    if discount_code and discount_code in discount_codes:
        discount = total_bill * discount_codes[discount_code]
        total_bill -= discount

    order_id = len(orders) + 1
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    order_details = (order_id, customer_name, selected_items, total_bill, discount, order_time)
    orders.append(order_details)
    unique_customers.add(customer_name)
    total_revenue += total_bill

    save_to_excel(order_details)

    return order_details, None

def save_to_excel(order_details):
    """Saves order details to an Excel file."""
    order_id, customer_name, items, total_bill, discount, order_time = order_details
    order_date, order_time = order_time.split(" ")

    try:
        workbook = openpyxl.load_workbook("orders.xlsx")
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Orders"
        sheet.append(["Order ID", "Customer Name", "Items", "Total Bill", "Discount", "Order Date", "Order Time"])
    else:
        sheet = workbook.active

    items_str = ", ".join([f"{item} (x{quantity})" for item, quantity in items])
    sheet.append([order_id, customer_name, items_str, total_bill, discount, order_date, order_time])

    workbook.save("orders.xlsx")

def get_total_revenue():
    """Returns total revenue generated from orders."""
    return total_revenue

def get_unique_customers():
    """Returns a list of unique customers who placed orders."""
    return list(unique_customers)