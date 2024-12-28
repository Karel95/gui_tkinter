import tkinter as tk

root = tk.Tk()
root.title("Entry")
root.geometry("350x250")


# Stringvars
nombre = tk.IntVar()
apellido = tk.StringVar()
email = tk.StringVar()

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
etiqueta_nombre = tk.Label(root,text="Escribe aqui tu nombre: ")
etiqueta_nombre.place(x=10,y=10)
# Entrada nombre
entrada_nombre = tk.Entry(root, textvariable=nombre)
entrada_nombre.place(x=170, y=10)
# Etiqueta apellido
etiqueta_apellido = tk.Label(root,text="Escribe aqui tu apellido: ")
etiqueta_apellido.place(x=10,y=40)
# Entrada apellido
entrada_epellido = tk.Entry(root, textvariable=apellido)
entrada_epellido.place(x=170, y=40)
# Etiqueta email
etiqueta_email = tk.Label(root,text="Escribe aqui tu email: ")
etiqueta_email.place(x=10,y=70)
# Entrada email
entrada_email = tk.Entry(root, textvariable=email)
entrada_email.place(x=170, y=70)

# Boton saludar
btn_saludo = tk.Button(root, text="Saludar", command=saludar)
btn_saludo.place(x=30,y=130)

root.mainloop()