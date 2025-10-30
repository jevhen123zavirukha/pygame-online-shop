import tkinter as tk


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


# -----------------------------
# GUI SETUP
# -----------------------------
root = tk.Tk()
root.title("Online Shop")
root.geometry("650x600")

# Title labelgit
title = tk.Label(root, text="Welcome to our Online Shop!", font=("Arial", 18, "bold"), pady=10, fg="white", bg="blue")
title.pack(fill=tk.X)

# Start the GUI event loop
root.mainloop()
