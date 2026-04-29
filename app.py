import tkinter as tk

root = tk.Tk()
root.title("Invoice Management System")
root.geometry("400x400")

title_label = tk.Label(root, text="Invoice Management System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

root.mainloop()
