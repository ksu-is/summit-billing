import tkinter as tk

def calculate_total():
    result_label.config(text="Calculation feature will be added next.")

root = tk.Tk()
root.title("Invoice Management System")
root.geometry("400x400")

title_label = tk.Label(root, text="Invoice Management System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

tk.Label(root, text="Customer Name").pack()
customer_entry = tk.Entry(root, width=30)
customer_entry.pack()

tk.Label(root, text="Item Name").pack()
item_entry = tk.Entry(root, width=30)
item_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root, width=30)
quantity_entry.pack()

tk.Label(root, text="Price per Item").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Invoice total will appear here.", justify="left")
result_label.pack(pady=15)

root.mainloop()
