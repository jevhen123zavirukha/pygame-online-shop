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
        update_cart_view()


def change_quantity(event):
    """
    Prompt the user to change the quantity of a selected cart item.

    :param event: tkinter event object (not used directly here)
    """
    selected_item = cart_tree.selection()
    if not selected_item:
        return

    product_name = cart_tree.item(selected_item, "values")[0]
    # Ask user for new quantity
    new_quantity = simpledialog.askinteger("Change Quantity", f"Enter new quantity for {product_name}:", minvalue=1)

    if new_quantity is not None:
        cart[product_name]["quantity"] = new_quantity
        update_cart_view()


def update_cart_view():
    """
    Update the Treeview that displays the cart.
    Clears existing items and reinserts all items in cart with updated quantities and total prices.
    Also updates the total price label.
    """
    # Clear current view
    for item in cart_tree.get_children():
        cart_tree.delete(item)

    total_price = 0
    # Insert each product in the cart into the Treeview
    for product_name, details in cart.items():
        cart_tree.insert("", "end", values=(product_name, details["quantity"], details["price"] * details["quantity"]))
        total_price += details["price"] * details["quantity"]

    total_price_label.config(text=f"Total price: {total_price} USD")


# -----------------------------
# GUI SETUP
# -----------------------------
root = tk.Tk()

# Title label
title = tk.Label(root, text="Welcome to our Online Shop!", font=("Arial", 18, "bold"), pady=10, fg="white", bg="blue")
title.pack(fill=tk.X)

root.title("Online Shop")
root.geometry("650x600")

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


# Cart label
cart_label = tk.Label(root, text="Your Cart:", font=("Arial", 14), pady=10)
cart_label.pack()

# Treeview for cart
cart_tree = ttk.Treeview(root, columns=("Product", "Quantity", "Price"), show="headings", height=8)
cart_tree.heading("Product", text="Product")
cart_tree.heading("Quantity", text="Quantity")
cart_tree.heading("Price", text="Price")
cart_tree.column("Product", width=200)
cart_tree.column("Quantity", width=100, anchor="center")
cart_tree.column("Price", width=100, anchor="center")
cart_tree.pack(pady=5)


# Total price label
total_price_label = tk.Label(root, text="Total price: 0 USD", font=("Arial", 14), pady=10)
total_price_label.pack()

# Buttons for cart actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Start the GUI event loop
root.mainloop()
