import tkinter as tk


root = tk.Tk()
root.title("My First Window")
root.geometry("500x500")


# place layout
label_place = tk.Label(root, text="First Place Label", font=("Helvetica", 16))
label_place.place(x=10, y=30)

boton_place = tk.Button(root, text="First Place Button", font=("Helvetica", 16), bg='green', fg='white')
boton_place.place(x=250, y=30)

label_place2 = tk.Label(root, text="Second Place Label", font=("Helvetica", 16))
label_place2.place(x=10, y=80)

boton_place2 = tk.Button(root, text="Second Place Button", font=("Helvetica", 16), bg='green', fg='white')
boton_place2.place(x=250, y=80)



root.mainloop()
