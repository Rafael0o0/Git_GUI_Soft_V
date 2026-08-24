import tkinter as tk
 
ventana = tk.Tk()
ventana.title("Trabajo Grupal - Git GUI")
ventana.geometry("420x320")
ventana.configure(bg="#1e3a5f")
 
ventana.mainloop()


from tkinter import messagebox
 
def mostrar_mensaje():
    messagebox.showinfo(
        "Mensaje",
        "Hola, este es un proyecto de ejemplo para Git GUI."
    )
 
boton_mensaje = tk.Button(
    ventana,
    text="Mostrar mensaje",
    command=mostrar_mensaje,
)
boton_mensaje.pack(pady=10)

def saludar():
    nombre = entrada_nombre.get().strip()
    if nombre == "":
        etiqueta_resultado.configure(
            text="Por favor escribe tu nombre."
        )
    else:
        etiqueta_resultado.configure(
            text=f"Hola, {nombre}! Bienvenido(a)."
        )
 
etiqueta_nombre = tk.Label(ventana, text="Escribe tu nombre:")
etiqueta_nombre.pack(pady=(15, 2))
 
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)
 
boton_saludo = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludo.pack(pady=8)
 
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=(5, 15))
