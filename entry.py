import tkinter as tk

root = tk.Tk()
root.title("Entry")
root.geometry("350x375")
root.resizable(100,100)


# Stringvars
nombre = tk.StringVar()
apellido = tk.StringVar()
email = tk.StringVar()
saludo = tk.StringVar()

# Seteo valor por defecto
nombre.set("Nombre")
apellido.set("Apellido")
email.set("Email")

# Funcion saludar
def saludar():
    print(f"Hola {nombre.get()} {apellido.get()}")
    print(f"Tu email es: {email.get()}")
    tk.Label(root, text=f"Hola \"{nombre.get()} {apellido.get()}\"").place(x=30, y=180)
    tk.Label(root, text=f"Tu email es: '{email.get()}'").place(x=30, y=210)


# Entiqueta nombre
etiqueta_nombre = tk.Label(root,text="Escribe aqui tu nombre: ", bd=5, fg="blue", font=("Arial 10"))
etiqueta_nombre.place(x=10,y=10)
# Entrada nombre
entrada_nombre = tk.Entry(root, textvariable=nombre, bd=5, bg="green")
entrada_nombre.place(x=170, y=10)

# Etiqueta apellido
etiqueta_apellido = tk.Label(root,text="Escribe aqui tu apellido: ", bd=5, fg="blue", font=("Arial 10"))
etiqueta_apellido.place(x=10,y=40)
# Entrada apellido
entrada_epellido = tk.Entry(root, textvariable=apellido, bd=5, bg="green")
entrada_epellido.place(x=170, y=40)

# Etiqueta email
etiqueta_email = tk.Label(root,text="Escribe aqui tu email: ", bd=5, fg="blue", font=("Arial 10"))
etiqueta_email.place(x=10,y=70)
# Entrada email
entrada_email = tk.Entry(root, textvariable=email, bd=5, bg="green")
entrada_email.place(x=170, y=70)

# Boton saludar
btn_saludo = tk.Button(root, text="Saludar", command=saludar, bd=5, bg="green")
btn_saludo.place(x=30,y=130)

entrar = tk.Entry(root, bd=10, font=("Arial 10"), textvariable=saludo, state="disabled")
entrar.place(x=70, y=250)

root.mainloop()
