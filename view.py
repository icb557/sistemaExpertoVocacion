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
    
    def reset_seleccion():
        for boton in botones:
            boton.config(bg="white", fg="black")  # Volver al color original
        seleccionados.clear()

    # Crear ventana principal
    root = tk.Tk()
    root.title("Selecciona tus intereses")
    root.geometry("600x550")

    # Etiqueta y entrada para el nombre
    tk.Label(root, text="Ingrese su nombre:", font=("Arial", 12)).pack(pady=5)
    nombre_entry = tk.Entry(root, font=("Arial", 12))
    nombre_entry.pack(pady=5)

    # Crear los botones de intereses como "cajas"
    tk.Label(root, text="Intereses:", font=("Arial", 12)).pack(pady=5)
    botones = []
    frame = tk.Frame(root)
    frame.pack(pady=10)

    for index, interes in enumerate(intereses):
        btn = tk.Button(frame, text=interes, font=("Arial", 10), width=15, height=2,
                        bg="white", fg="black", relief="raised")
        btn.config(command=lambda b=btn, i=interes: toggle_interes(b, i))
        btn.grid(row=index % 5, column=index // 5, padx=5, pady=5)
        botones.append(btn)

    # Botón para confirmar selección
    def registrar():
        print(seleccionados)
        if validar_datos(nombre_entry, seleccionados):
            results = run_inputs(sistemaExperto, seleccionados, nombre_entry.get().strip())
            if results:
                formatted_results = [f"{index + 1}. {vocacion[0]}" for index, (vocacion) in enumerate(results)]
                messagebox.showinfo("Resultados", f"Estas son las carreras ordenadas en base a tus interes a las que te recomendamos aspirar: \n\n{'\n'.join(formatted_results)}")
                reset_seleccion()
            else:
                messagebox.showinfo("Resultados", "No se encontraron recomendaciones basadas en tus intereses.")

    tk.Button(root, text="Limpiar", font=("Arial", 12), command=reset_seleccion).pack(pady=10)
    tk.Button(root, text="Registrar", font=("Arial", 12), command=registrar).pack(pady=10)
    tk.Button(root, text="Cerrar", font=("Arial", 12), command=root.quit).pack(pady=10)

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
