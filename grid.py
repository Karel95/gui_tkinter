import tkinter as tk


root = tk.Tk()
root.title("My First Window")
root.geometry("500x500")


# grid layout
label_grid = tk.Label(root, text="First Grid Label", font=("Helvetica", 16))
label_grid.grid(row=0, column=0)

boton_grid = tk.Button(root, text="First Grid Button", font=("Helvetica", 16), bg='green', fg='white')
boton_grid.grid(row=0, column=1, columnspan=2, sticky='ew')

label_grid2 = tk.Label(root, text="Second Grid Label", font=("Helvetica", 16))
label_grid2.grid(row=1, column=0)

boton_grid2 = tk.Button(root, text="Second Grid Button", font=("Helvetica", 16), bg='green', fg='white')
boton_grid2.grid(row=1, column=1, columnspan=2, sticky='ew')



root.mainloop()
