# order_manager.py - Handles order management

from menu import menu

# List to store orders
orders = []

# Set to store unique customers
unique_customers = set()

# Variable to track total revenue
total_revenue = 0

def place_order(customer_name, selected_items):
    """Places an order and returns order details."""
    global total_revenue

    if not customer_name:
        return None, "Customer name cannot be empty!"

    if not selected_items:
        return None, "Please select at least one item!"

    total_bill = sum(menu[item][0] for item in selected_items)
    order_id = len(orders) + 1

    order_details = (order_id, customer_name, selected_items, total_bill)
    orders.append(order_details)
    unique_customers.add(customer_name)
    total_revenue += total_bill

    return order_details, None

def get_total_revenue():
    """Returns total revenue generated from orders."""
    return total_revenue

def get_unique_customers():
    """Returns a list of unique customers who placed orders."""
    return list(unique_customers)
