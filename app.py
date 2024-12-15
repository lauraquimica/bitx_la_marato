import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import pandas as pd

def cargar_excel():
    """Función para cargar un archivo Excel seleccionado por el usuario."""
    archivo = filedialog.askopenfilename(
        title="Seleccionar un archivo Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )

    if archivo:
        try:
            # Carga el archivo Excel usando pandas
            datos = pd.read_excel(archivo)
            messagebox.showinfo("Éxito", f"Archivo cargado con éxito. Contiene {len(datos)} filas y {len(datos.columns)} columnas.")
            print(datos.head())  # Muestra una vista previa en la terminal
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
    else:
        messagebox.showwarning("Atención", "No seleccionaste ningún archivo.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Datos Médicos")
ventana.geometry("600x400")
ventana.configure(bg="#e0f7fa")

# Agregar un icono (asegúrate de tener una imagen llamada "icono.png" en el mismo directorio)
try:
    ventana.iconphoto(False, PhotoImage(file="icono.png"))
except:
    pass

# Encabezado
encabezado = tk.Label(
    ventana, 
    text="Bienvenido a la Calculadora de Datos Médicos",
    font=("Arial", 16, "bold"), 
    bg="#e0f7fa", 
    fg="#00796b"
)
encabezado.pack(pady=20)

# Subtítulo
subtitulo = tk.Label(
    ventana, 
    text="Esta herramienta está diseñada para ayudar con problemas respiratorios",
    font=("Arial", 12), 
    bg="#e0f7fa", 
    fg="#004d40"
)
subtitulo.pack(pady=10)

# Imagen decorativa (asegúrate de tener una imagen llamada "pulmones.png" en el mismo directorio)
try:
    imagen = PhotoImage(file="pulmones.png")
    etiqueta_imagen = tk.Label(ventana, image=imagen, bg="#e0f7fa")
    etiqueta_imagen.pack(pady=10)
except:
    pass

# Botón para cargar el archivo
boton_cargar = tk.Button(
    ventana, 
    text="Cargar Archivo Excel", 
    command=cargar_excel, 
    bg="#004d40", 
    fg="white", 
    font=("Arial", 12, "bold"), 
    padx=20, 
    pady=10
)
boton_cargar.pack(pady=20)

# Etiqueta de pie de página
pie_pagina = tk.Label(
    ventana, 
    text="Asegúrate de cargar datos correctos para un análisis preciso",
    font=("Arial", 10), 
    bg="#e0f7fa", 
    fg="#004d40"
)
pie_pagina.pack(side="bottom", pady=10)

# Ejecutar la aplicación
ventana.mainloop()
