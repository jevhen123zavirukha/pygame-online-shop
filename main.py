import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os


# -----------------------------
# PRODUCT DATA
# -----------------------------
# List of products available in the shop with name and price
products = [
    {"name": "Drinks (5 L)", "price": 5},
    {"name": "Bread (720 g)", "price": 2},
    {"name": "Meat (1.2 kg)", "price": 4},
    {"name": "Toys (Lego)", "price": 50},
    {"name": "Milk and cheese (2 L + 650 g)", "price": 6},
]

# Dictionary to hold cart items: {product_name: {"price": x, "quantity": y}}
cart = {}


# -----------------------------
# CART MANAGEMENT FUNCTIONS
# -----------------------------
def add_to_cart(product):
    """
    Add a product to the cart. If the product is already in the cart, increment quantity by 1.
    Then update the cart view.

    :param product: dict, product information with 'name' and 'price'
    """
    if product["name"] in cart:
        cart[product["name"]]["quantity"] += 1
    else:
        cart[product["name"]] = {"price": product["price"], "quantity": 1}
        # func


# -----------------------------
# GUI SETUP
# -----------------------------
root = tk.Tk()

# Frame for products
product_frame = tk.Frame(root, pady=10)
product_frame.pack()

product_label = tk.Label(product_frame, text="Available Products:", font=("Arial", 14))
product_label.grid(row=0, column=0, columnspan=3, pady=5)

# Add product labels, prices, and "Add" buttons
for idx, product in enumerate(products):
    name_label = tk.Label(product_frame, text=product["name"], font=("Arial", 12))
    name_label.grid(row=idx + 1, column=0, padx=10, pady=5, sticky="w")

    price_label = tk.Label(product_frame, text=f"{product['price']} USD", font=("Arial", 12))
    price_label.grid(row=idx + 1, column=1, padx=10)

    add_button = tk.Button(product_frame, text="Add", command=lambda p=product: add_to_cart(p), bg="green", fg="white")
    add_button.grid(row=idx + 1, column=2, padx=10)


# Title label
title = tk.Label(root, text="Welcome to our Online Shop!", font=("Arial", 18, "bold"), pady=10, fg="white", bg="blue")
title.pack(fill=tk.X)

root.title("Online Shop")
root.geometry("650x600")

# Start the GUI event loop
root.mainloop()
