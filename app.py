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
