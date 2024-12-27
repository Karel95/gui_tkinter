import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My First Window")
root.geometry("500x500")

def print_hello():
    print("Hello World")
    msg = tk.Label(root, text="Hello World", font=("Helvetica", 16))
    msg.pack()

def selection(option):
    print(option)
    msg = tk.Label(root, text=option, font=("Helvetica", 16)).pack()

text = tk.Label(root, text="My First App", font=("Helvetica", 16))
text.pack()

# Styling ttk.Button
style = ttk.Style()
style.configure("Custom.TButton", font=("Helvetica", 16), foreground="black")

# Using the style in ttk.Button
select_button = ttk.Button(root, text="Python", command=lambda: selection('Python'), style="Custom.TButton")
select_button.pack(pady=10)
select_button.config(width=20, cursor='pirate')

ttk.Button(root, text="JavaScript", command=lambda: selection('JavaScript'), width=50, cursor='hand2').pack()

hello_button = tk.Button(root, text="Hello", command=print_hello, font=("Helvetica", 16), bg='blue', fg='white')
hello_button.pack(side=tk.LEFT, padx=5)

min_button = tk.Button(root, text="Minimice", command=root.iconify, font=("Helvetica", 16), bg='red', fg='white')
min_button.pack(side=tk.RIGHT, padx=15)



root.mainloop()
