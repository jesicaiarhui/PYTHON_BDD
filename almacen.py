import tkinter as tk
from tkinter import ttk
import mysql.connector

conexion = mysql.connector.connect(user="root", host="localhost", port = "3306", database="ALMACEN")

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children()) # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT PRODUCTOS.NOMBRE, CATEGORIA.NOMBRE FROM PRODUCTOS JOIN CATEGORIA ON = Carreras.IDCARRERA")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Crear ventana
root = tk.Tk()
root.title("Consulta de Productos")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("Nombre", "categoria", "marca", "Precio", "Stock"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Categoria")
tree.heading("#3", text="Marca")
tree.heading("#4", text= "Precio")
tree.heading("#5", text= "Stock")
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.pack(padx=10, pady=10)

# Botón para cargar datos
cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()