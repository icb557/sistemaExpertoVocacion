import tkinter as tk
from tkinter import messagebox
from vocationService import run_inputs, get_results

intereses = [
    "Matemáticas", "Tecnología", "Programación", "Lógica",
    "Creatividad", "Diseño", "Ayudar", "Biología",
    "Liderazgo", "Estrategia"
]

def show_menu(sistemaExperto):
    # Almacenar intereses seleccionados
    seleccionados = []

    # Función para manejar selección/deselección
    def toggle_interes(boton, interes):
        if interes in seleccionados:
            seleccionados.remove(interes)
            boton.config(bg="white", fg="black")  # Volver al color original
        else:
            seleccionados.append(interes)
            boton.config(bg="green", fg="white")  # Marcar seleccionado

    # Crear ventana principal
    root = tk.Tk()
    root.title("Selecciona tus intereses")
    root.geometry("600x700")

    # Etiqueta y entrada para el nombre
    tk.Label(root, text="Ingrese su nombre:", font=("Arial", 12)).pack(pady=5)
    nombre_entry = tk.Entry(root, font=("Arial", 12))
    nombre_entry.pack(pady=5)

    # Crear los botones de intereses como "cajas"
    botones = []
    frame = tk.Frame(root)
    frame.pack(pady=10)

    for interes in intereses:
        btn = tk.Button(frame, text=interes, font=("Arial", 10), width=15, height=2,
                        bg="white", fg="black", relief="raised")
        btn.config(command=lambda b=btn, i=interes: toggle_interes(b, i))
        btn.pack(pady=5)
        botones.append(btn)

    # Botón para confirmar selección
    def registrar():
        if validar_datos(nombre_entry, seleccionados):
            run_inputs(sistemaExperto, seleccionados, nombre_entry.get().strip())
            results = get_results(sistemaExperto)
            if results:
                messagebox.showinfo("Resultados", f"De acuerdo a tus intereses, estas son las carreras que te recomendamos aspirar: \n\n{', '.join(results)}")
            else:
                messagebox.showinfo("Resultados", "No se encontraron recomendaciones basadas en tus intereses.")

    tk.Button(root, text="Registrar", font=("Arial", 12), command=registrar).pack(pady=10)

    # Ejecutar aplicación
    root.mainloop()

def validar_datos(nombre_entry, seleccionados):
    nombre = nombre_entry.get().strip()
    if not nombre:
        messagebox.showwarning("Error", "Debe ingresar un nombre.")
        return False
    
    if not seleccionados:
        messagebox.showwarning("Error", "No seleccionó intereses.")
        return False
    
    return True
