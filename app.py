import tkinter as tk
from tkinter import messagebox


# =========================
# Ventana principal
# =========================
ventana = tk.Tk()
ventana.title("Trabajo Grupal - Git GUI")
ventana.geometry("420x320")
ventana.configure(bg="#1e3a5f")
ventana.resizable(False, False)


# =========================
# Funciones
# =========================
def mostrar_mensaje():
    messagebox.showinfo(
        "Mensaje",
        "Holaa, este es un proyecto de ejemplo para Git GUI."
    )


def saludar():
    nombre = entrada_nombre.get().strip()

    if nombre == "":
        etiqueta_resultado.configure(
            text="Por favor escribe tu nombre."
        )
    else:
        etiqueta_resultado.configure(
            text=f"Holaa, {nombre}! Bienvenido."
        )

//djsadkjaj

# =========================
# Título
# =========================
etiqueta_titulo = tk.Label(
    ventana,
    text="Demo - Control de versiones con Git GUI",
    bg="#1e3a5f",
    fg="white",
    font=("Segoe UI", 13, "bold"),
    wraplength=380,
    justify="center"
)
etiqueta_titulo.pack(pady=(20, 10))


# =========================
# Botón principal
# =========================
boton_mensaje = tk.Button(
    ventana,
    text="Mostrar mensaje",
    command=mostrar_mensaje,
    bg="#f2a900",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=20,
    height=1
)
boton_mensaje.pack(pady=10)


# =========================
# Nombre
# =========================
etiqueta_nombre = tk.Label(
    ventana,
    text="Escribe tu nombre:",
    bg="#1e3a5f",
    fg="white",
    font=("Segoe UI", 10)
)
etiqueta_nombre.pack(pady=(15, 2))


entrada_nombre = tk.Entry(
    ventana,
    width=30,
    font=("Segoe UI", 10)
)
entrada_nombre.pack(pady=5)


# =========================
# Botón Saludar
# =========================
boton_saludo = tk.Button(
    ventana,
    text="Saludar",
    command=saludar,
    bg="#4caf50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=14
)
boton_saludo.pack(pady=8)


# =========================
# Resultado
# =========================
etiqueta_resultado = tk.Label(
    ventana,
    text="",
    bg="#1e3a5f",
    fg="#f2a900",
    font=("Segoe UI", 10, "italic")
)
etiqueta_resultado.pack(pady=(5, 15))


# =========================
# Ejecutar programa
# =========================
ventana.mainloop()