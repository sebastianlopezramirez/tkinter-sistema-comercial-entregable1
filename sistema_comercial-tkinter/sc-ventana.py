import tkinter as tk # importo la interfaz de tkinter
from tkinter import ttk, messagebox# interfaz mas moderna

# creo la ventana principal sc-ventana

ventana = tk.Tk() # defino que la ventana ppal se lalamra ventana
ventana.geometry("1400x900") #tamaño de la ventana ppal
ventana.title("Sistema_Comercial") #titulo de la ventana principal
ventana.configure(bg='blue')

#configuracion de estilo para lsa pestañas
style=ttk.Style()
style.configure('TNotebook', tabmargins=[1,1,2,0]) # margenes [izq, arriba, der, abajo]
style.configure('TNotebook.Tab', padding=[2,1], front=('Helvetica', '10', 'bold'))

# crear los widgest de las pestañas para cada tabla de la base de datos sistema_comercial

notebook=ttk.Notebook(ventana) # as pestañas seran los notebook e iran dentro de la ventana ppal

# se crean los frames(contenedores de las pestañas) para cada tabla
tab1 = ttk.Frame(notebook) #contenedor para la pestaña 1
tab2 = ttk.Frame(notebook) #contenedor para la pestaña 2
tab3 = ttk.Frame(notebook) #contenedor para la pestaña 3
tab4 = ttk.Frame(notebook) #contenedor para la pestaña 4
tab5 = ttk.Frame(notebook) #contenedor para la pestaña 5
tab6 = ttk.Frame(notebook) #contenedor para la pestaña 6
tab7 = ttk.Frame(notebook) #contenedor para la pestaña 7
tab8 = ttk.Frame(notebook) #contenedor para la pestaña 8
tab9 = ttk.Frame(notebook) #contenedor para la pestaña 9
tab10 = ttk.Frame(notebook) #contenedor para la pestaña 10
tab11 = ttk.Frame(notebook) #contenedor para la pestaña 11
tab12 = ttk.Frame(notebook) #contenedor para la pestaña 12
tab13 = ttk.Frame(notebook) #contenedor para la pestaña 13
tab14 = ttk.Frame(notebook) #contenedor para la pestaña 14
tab15 = ttk.Frame(notebook) #contenedor para la pestaña 15

# ingreso los labs de cada notebook
notebook.add(tab1, text="Alertas") # pestaña 1
notebook.add(tab2, text="Categorias")  # pestaña 2
notebook.add(tab3, text="Clientes")  # pestaña 3
notebook.add(tab4, text="Clientes_Direcciones")  # pestaña 4
notebook.add(tab5, text="Detalles_Devolucion")  # pestaña 5
notebook.add(tab6, text="Detalles_pedido")  # pestaña 6
notebook.add(tab7, text="Devoluciones")  # pestaña 7
notebook.add(tab8, text="Empleados")  # pestaña 8
notebook.add(tab9, text="Historial_Pedidos")  # pestaña 9
notebook.add(tab10, text="Logs_Clientes")  # pestaña 10
notebook.add(tab11, text="Pedidos")  # pestaña 11
notebook.add(tab12, text="Prefe_Clientes")  # pestaña 12
notebook.add(tab13, text="Prod_proveedor")  # pestaña 13
notebook.add(tab14, text="Productos")  # pestaña 14
notebook.add(tab15, text="Proveedores")  # pestaña 15

notebook.pack(expand=True, fill="both") # empaquetado de las pestañas para que se puedan ver a la hora de correr el codigo

# contenido 1 primera pestaña productos ----------------------------------------------------------------------------------
titulo1 = tk.Label(tab1,text="GESTION - ALERTAS",font=("Arial", 16, "bold"),fg="white",bg="darkblue",pady=10,padx=10)
titulo1.pack(pady=10, fill="x")

#frame para contener el formulario
form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

#fila 1 ID - e usa .GRID para alinear organiza los widget en filas o columnas perfecto para formularios
tk.Label(form_frame, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Producto_ID
tk.Label(form_frame, text="Producto_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Producto_ID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Producto_ID.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Mensaje
tk.Label(form_frame, text="Mensaje:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Mensaje = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Mensaje.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Fecha
tk.Label(form_frame, text="Fecha:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Nivel
tk.Label(form_frame, text="Nivel:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Nivel = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Nivel.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Vista
tk.Label(form_frame, text="Vista:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Vista = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Vista.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Fecha_Vista
tk.Label(form_frame, text="Fecha_Vista:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_Vista = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_Vista.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: Usuario_Vista
tk.Label(form_frame, text="Usuario_Vista:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Usuario_Vista = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Usuario_Vista.grid(row=8, column=1, sticky="w", pady=10)

# CONFIGURACION DE MENSAJES DE LOS BOTONES
def save_products():
    messagebox.showinfo(title="Guardar", message="Alerta guardada correctamente")  # Corregido

def update_product():  # Corregido el nombre (update_prodcut → update_product)
    messagebox.showinfo(title="Actualizar", message="Alerta actualizada correctamente")  # Corregido

def delete_product():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar esta alerta?"):  # Corregido
        messagebox.showinfo(title="Eliminar", message="Alerta eliminada correctamente")

def clear_product_form():
    ID.delete(0, tk.END)
    Producto_ID.delete(0, tk.END)
    Mensaje.delete(0, tk.END)
    Fecha.delete(0, tk.END)
    Nivel.delete(0, tk.END)
    Vista.delete(0, tk.END)
    Fecha_Vista.delete(0, tk.END)
    Usuario_Vista.delete(0, tk.END)


#frame para botones_products
button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_products)
btn_save.pack(side=tk.LEFT, padx=5) # boton oara guardar

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_product)
btn_update.pack(side=tk.LEFT, padx=5) # boton para actualizar

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_product)
btn_delete.pack(side=tk.LEFT, padx=5) #boton para eliminar

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_product_form)
btn_clear.pack(side=tk.LEFT, padx=5) # boton para limpiar


# contenido 2 segunda pestaña categorías ----------------------------------------------------------------------------------
titulo2 = tk.Label(tab2, text="GESTIÓN - CATEGORÍAS", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo2.pack(pady=10, fill="x") #

# frame para contener el formulario
form_frame2 = tk.Frame(tab2)
form_frame2.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame2, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_cat = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_cat.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Nombre
tk.Label(form_frame2, text="Nombre:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Nombre_cat = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
Nombre_cat.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Descripción
tk.Label(form_frame2, text="Descripción:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Descripcion_cat = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
Descripcion_cat.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Imagen
tk.Label(form_frame2, text="Imagen:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Imagen_cat = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
Imagen_cat.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Activa
tk.Label(form_frame2, text="Activa:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Activa_cat = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
Activa_cat.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Creado
tk.Label(form_frame2, text="Creado:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Creado_cat = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
Creado_cat.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Actualizado
tk.Label(form_frame2, text="Actualizado:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Actualizado_cat = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
Actualizado_cat.grid(row=7, column=1, sticky="w", pady=10)

# Configuración de mensajes de los botones para categorías
def save_categories():
    messagebox.showinfo(title="Guardar", message="Categoría guardada correctamente")

def update_category():
    messagebox.showinfo(title="Actualizar", message="Categoría actualizada correctamente")

def delete_category():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar esta categoría?"):
        messagebox.showinfo(title="Eliminar", message="Categoría eliminada correctamente")

def clear_category_form():
    ID_cat.delete(0, tk.END)
    Nombre_cat.delete(0, tk.END)
    Descripcion_cat.delete(0, tk.END)
    Imagen_cat.delete(0, tk.END)
    Activa_cat.delete(0, tk.END)
    Creado_cat.delete(0, tk.END)
    Actualizado_cat.delete(0, tk.END)

# frame para botones_categories
button_frame2 = tk.Frame(tab2)
button_frame2.pack(pady=20)

btn_save_cat = tk.Button(button_frame2, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_categories)
btn_save_cat.pack(side=tk.LEFT, padx=5)

btn_update_cat = tk.Button(button_frame2, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_category)
btn_update_cat.pack(side=tk.LEFT, padx=5)

btn_delete_cat = tk.Button(button_frame2, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_category)
btn_delete_cat.pack(side=tk.LEFT, padx=5)

btn_clear_cat = tk.Button(button_frame2, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_category_form)
btn_clear_cat.pack(side=tk.LEFT, padx=5)



# contenido 3 tercera pestaña clientes ----------------------------------------------------------------------------------
titulo3 = tk.Label(tab3, text="GESTIÓN - CLIENTES", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo3.pack(pady=10, fill="x")


# frame para contener el formulario
form_frame3 = tk.Frame(tab3)
form_frame3.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame3, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_cli.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Nombre
tk.Label(form_frame3, text="Nombre:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Nombre_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Nombre_cli.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Apellido
tk.Label(form_frame3, text="Apellido:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Apellido_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Apellido_cli.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Email
tk.Label(form_frame3, text="Email:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Email_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Email_cli.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Teléfono
tk.Label(form_frame3, text="Teléfono:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Telefono_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Telefono_cli.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Dirección
tk.Label(form_frame3, text="Dirección:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Direccion_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Direccion_cli.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Ciudad
tk.Label(form_frame3, text="Ciudad:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Ciudad_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Ciudad_cli.grid(row=7, column=1, sticky="w", pady=10)

# fila 8: Código Postal
tk.Label(form_frame3, text="Código Postal:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
CodigoPostal_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
CodigoPostal_cli.grid(row=8, column=1, sticky="w", pady=10)

# fila 9: País
tk.Label(form_frame3, text="País:", font=("Arial", 12, "bold")).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
Pais_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Pais_cli.grid(row=9, column=1, sticky="w", pady=10)

# fila 10: Fecha Registro
tk.Label(form_frame3, text="Fecha Registro:", font=("Arial", 12, "bold")).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
FechaRegistro_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaRegistro_cli.grid(row=10, column=1, sticky="w", pady=10)

# fila 11: Actualizado
tk.Label(form_frame3, text="Actualizado:", font=("Arial", 12, "bold")).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
Actualizado_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Actualizado_cli.grid(row=11, column=1, sticky="w", pady=10)

# fila 12: Estado
tk.Label(form_frame3, text="Estado:", font=("Arial", 12, "bold")).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=10)
Estado_cli = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
Estado_cli.grid(row=12, column=1, sticky="w", pady=10)

# Configuración de mensajes de los botones para clientes
def save_clients():
    messagebox.showinfo(title="Guardar", message="Cliente guardado correctamente")

def update_client():
    messagebox.showinfo(title="Actualizar", message="Cliente actualizado correctamente")

def delete_client():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este cliente?"):
        messagebox.showinfo(title="Eliminar", message="Cliente eliminado correctamente")

def clear_client_form():
    ID_cli.delete(0, tk.END)
    Nombre_cli.delete(0, tk.END)
    Apellido_cli.delete(0, tk.END)
    Email_cli.delete(0, tk.END)
    Telefono_cli.delete(0, tk.END)
    Direccion_cli.delete(0, tk.END)
    Ciudad_cli.delete(0, tk.END)
    CodigoPostal_cli.delete(0, tk.END)
    Pais_cli.delete(0, tk.END)
    FechaRegistro_cli.delete(0, tk.END)
    Actualizado_cli.delete(0, tk.END)
    Estado_cli.delete(0, tk.END)

# frame para botones_clients
button_frame3 = tk.Frame(tab3)
button_frame3.pack(pady=20)

btn_save_cli = tk.Button(button_frame3, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_clients)
btn_save_cli.pack(side=tk.LEFT, padx=5)

btn_update_cli = tk.Button(button_frame3, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_client)
btn_update_cli.pack(side=tk.LEFT, padx=5)

btn_delete_cli = tk.Button(button_frame3, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_client)
btn_delete_cli.pack(side=tk.LEFT, padx=5)

btn_clear_cli = tk.Button(button_frame3, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_client_form)
btn_clear_cli.pack(side=tk.LEFT, padx=5)


# contenido 4 cuarta pestaña clientes_direcciones ----------------------------------------------------------------------------------
titulo4 = tk.Label(tab4, text="GESTIÓN - CLIENTES_DIRECCIONES", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo4.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame4 = tk.Frame(tab4)
form_frame4.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame4, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_dir.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Cliente_ID
tk.Label(form_frame4, text="Cliente_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Cliente_ID_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
Cliente_ID_dir.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Tipo
tk.Label(form_frame4, text="Tipo:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Tipo_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
Tipo_dir.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Dirección
tk.Label(form_frame4, text="Dirección:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Direccion_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
Direccion_dir.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Ciudad
tk.Label(form_frame4, text="Ciudad:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Ciudad_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
Ciudad_dir.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Código Postal
tk.Label(form_frame4, text="Código Postal:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
CodigoPostal_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
CodigoPostal_dir.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Provincia
tk.Label(form_frame4, text="Provincia:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Provincia_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
Provincia_dir.grid(row=7, column=1, sticky="w", pady=10)

# fila 8: País
tk.Label(form_frame4, text="País:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Pais_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
Pais_dir.grid(row=8, column=1, sticky="w", pady=10)

# fila 9: Es Principal
tk.Label(form_frame4, text="Es Principal:", font=("Arial", 12, "bold")).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
EsPrincipal_dir = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
EsPrincipal_dir.grid(row=9, column=1, sticky="w", pady=10)

# Configuración de mensajes de los botones para clientes_direcciones
def save_direcciones():
    messagebox.showinfo(title="Guardar", message="Dirección guardada correctamente")

def update_direccion():
    messagebox.showinfo(title="Actualizar", message="Dirección actualizada correctamente")

def delete_direccion():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar esta dirección?"):
        messagebox.showinfo(title="Eliminar", message="Dirección eliminada correctamente")

def clear_direccion_form():
    ID_dir.delete(0, tk.END)
    Cliente_ID_dir.delete(0, tk.END)
    Tipo_dir.delete(0, tk.END)
    Direccion_dir.delete(0, tk.END)
    Ciudad_dir.delete(0, tk.END)
    CodigoPostal_dir.delete(0, tk.END)
    Provincia_dir.delete(0, tk.END)
    Pais_dir.delete(0, tk.END)
    EsPrincipal_dir.delete(0, tk.END)

# frame para botones_direcciones
button_frame4 = tk.Frame(tab4)
button_frame4.pack(pady=20)

btn_save_dir = tk.Button(button_frame4, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_direcciones)
btn_save_dir.pack(side=tk.LEFT, padx=5)

btn_update_dir = tk.Button(button_frame4, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_direccion)
btn_update_dir.pack(side=tk.LEFT, padx=5)

btn_delete_dir = tk.Button(button_frame4, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_direccion)
btn_delete_dir.pack(side=tk.LEFT, padx=5)

btn_clear_dir = tk.Button(button_frame4, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_direccion_form)
btn_clear_dir.pack(side=tk.LEFT, padx=5)


# contenido 5 quinta pestaña detalles_devolucion ----------------------------------------------------------------------------------
titulo5 = tk.Label(tab5, text="GESTIÓN - DETALLES_DEVOLUCION", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo5.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame5 = tk.Frame(tab5)
form_frame5.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame5, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_detdev = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_detdev.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Devolucion_ID
tk.Label(form_frame5, text="Devolucion_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Devolucion_ID_detdev = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
Devolucion_ID_detdev.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Producto_ID
tk.Label(form_frame5, text="Producto_ID:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Producto_ID_detdev = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
Producto_ID_detdev.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Cantidad
tk.Label(form_frame5, text="Cantidad:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Cantidad_detdev = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
Cantidad_detdev.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Precio Unitario
tk.Label(form_frame5, text="Precio Unitario:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
PrecioUnitario_detdev = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
PrecioUnitario_detdev.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Subtotal
tk.Label(form_frame5, text="Subtotal:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Subtotal_detdev = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
Subtotal_detdev.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Estado Producto
tk.Label(form_frame5, text="Estado Producto:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
EstadoProducto_detdev = tk.Entry(form_frame5, width=25, font=("Arial", 12), relief="solid", bd=1)
EstadoProducto_detdev.grid(row=7, column=1, sticky="w", pady=10)

# Configuración de mensajes de los botones para detalles_devolucion
def save_detalles_devolucion():
    messagebox.showinfo(title="Guardar", message="Detalle de devolución guardado correctamente")

def update_detalle_devolucion():
    messagebox.showinfo(title="Actualizar", message="Detalle de devolución actualizado correctamente")

def delete_detalle_devolucion():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este detalle de devolución?"):
        messagebox.showinfo(title="Eliminar", message="Detalle de devolución eliminado correctamente")

def clear_detalle_devolucion_form():
    ID_detdev.delete(0, tk.END)
    Devolucion_ID_detdev.delete(0, tk.END)
    Producto_ID_detdev.delete(0, tk.END)
    Cantidad_detdev.delete(0, tk.END)
    PrecioUnitario_detdev.delete(0, tk.END)
    Subtotal_detdev.delete(0, tk.END)
    EstadoProducto_detdev.delete(0, tk.END)

# frame para botones_detalles_devolucion
button_frame5 = tk.Frame(tab5)
button_frame5.pack(pady=20)

btn_save_detdev = tk.Button(button_frame5, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_detalles_devolucion)
btn_save_detdev.pack(side=tk.LEFT, padx=5)

btn_update_detdev = tk.Button(button_frame5, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_detalle_devolucion)
btn_update_detdev.pack(side=tk.LEFT, padx=5)

btn_delete_detdev = tk.Button(button_frame5, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_detalle_devolucion)
btn_delete_detdev.pack(side=tk.LEFT, padx=5)

btn_clear_detdev = tk.Button(button_frame5, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_detalle_devolucion_form)
btn_clear_detdev.pack(side=tk.LEFT, padx=5)


# contenido 6 sexta pestaña detalles_pedido ----------------------------------------------------------------------------------
titulo6 = tk.Label(tab6, text="GESTIÓN - DETALLES_PEDIDO", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo6.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame6 = tk.Frame(tab6)
form_frame6.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame6, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_detped = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_detped.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Pedido_ID
tk.Label(form_frame6, text="Pedido_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Pedido_ID_detped = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
Pedido_ID_detped.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Producto_ID
tk.Label(form_frame6, text="Producto_ID:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Producto_ID_detped = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
Producto_ID_detped.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Cantidad
tk.Label(form_frame6, text="Cantidad:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Cantidad_detped = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
Cantidad_detped.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Precio Unitario
tk.Label(form_frame6, text="Precio Unitario:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
PrecioUnitario_detped = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
PrecioUnitario_detped.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Descuento
tk.Label(form_frame6, text="Descuento:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Descuento_detped = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
Descuento_detped.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Subtotal
tk.Label(form_frame6, text="Subtotal:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Subtotal_detped = tk.Entry(form_frame6, width=25, font=("Arial", 12), relief="solid", bd=1)
Subtotal_detped.grid(row=7, column=1, sticky="w", pady=10)

# Configuración de mensajes de los botones para detalles_pedido
def save_detalles_pedido():
    messagebox.showinfo(title="Guardar", message="Detalle de pedido guardado correctamente")

def update_detalle_pedido():
    messagebox.showinfo(title="Actualizar", message="Detalle de pedido actualizado correctamente")

def delete_detalle_pedido():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este detalle de pedido?"):
        messagebox.showinfo(title="Eliminar", message="Detalle de pedido eliminado correctamente")

def clear_detalle_pedido_form():
    ID_detped.delete(0, tk.END)
    Pedido_ID_detped.delete(0, tk.END)
    Producto_ID_detped.delete(0, tk.END)
    Cantidad_detped.delete(0, tk.END)
    PrecioUnitario_detped.delete(0, tk.END)
    Descuento_detped.delete(0, tk.END)
    Subtotal_detped.delete(0, tk.END)

# frame para botones_detalles_pedido
button_frame6 = tk.Frame(tab6)
button_frame6.pack(pady=20)

btn_save_detped = tk.Button(button_frame6, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_detalles_pedido)
btn_save_detped.pack(side=tk.LEFT, padx=5)

btn_update_detped = tk.Button(button_frame6, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_detalle_pedido)
btn_update_detped.pack(side=tk.LEFT, padx=5)

btn_delete_detped = tk.Button(button_frame6, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_detalle_pedido)
btn_delete_detped.pack(side=tk.LEFT, padx=5)

btn_clear_detped = tk.Button(button_frame6, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_detalle_pedido_form)
btn_clear_detped.pack(side=tk.LEFT, padx=5)


# contenido 7 séptima pestaña devoluciones ----------------------------------------------------------------------------------
titulo7 = tk.Label(tab7, text="GESTIÓN - DEVOLUCIONES", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo7.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame7 = tk.Frame(tab7)
form_frame7.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame7, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_dev.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Pedido_ID
tk.Label(form_frame7, text="Pedido_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Pedido_ID_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
Pedido_ID_dev.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Cliente_ID
tk.Label(form_frame7, text="Cliente_ID:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Cliente_ID_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
Cliente_ID_dev.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Fecha Solicitud
tk.Label(form_frame7, text="Fecha Solicitud:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
FechaSolicitud_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaSolicitud_dev.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Fecha Procesado
tk.Label(form_frame7, text="Fecha Procesado:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
FechaProcesado_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
FechaProcesado_dev.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Motivo
tk.Label(form_frame7, text="Motivo:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Motivo_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
Motivo_dev.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Descripción
tk.Label(form_frame7, text="Descripción:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Descripcion_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
Descripcion_dev.grid(row=7, column=1, sticky="w", pady=10)

# fila 8: Estado
tk.Label(form_frame7, text="Estado:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Estado_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
Estado_dev.grid(row=8, column=1, sticky="w", pady=10)

# fila 9: Monto Devolución
tk.Label(form_frame7, text="Monto Devolución:", font=("Arial", 12, "bold")).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
MontoDevolucion_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
MontoDevolucion_dev.grid(row=9, column=1, sticky="w", pady=10)

# fila 10: Empleado_ID
tk.Label(form_frame7, text="Empleado_ID:", font=("Arial", 12, "bold")).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
Empleado_ID_dev = tk.Entry(form_frame7, width=25, font=("Arial", 12), relief="solid", bd=1)
Empleado_ID_dev.grid(row=10, column=1, sticky="w", pady=10)

# Configuración de mensajes de los botones para devoluciones
def save_devoluciones():
    messagebox.showinfo(title="Guardar", message="Devolución guardada correctamente")

def update_devolucion():
    messagebox.showinfo(title="Actualizar", message="Devolución actualizada correctamente")

def delete_devolucion():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar esta devolución?"):
        messagebox.showinfo(title="Eliminar", message="Devolución eliminada correctamente")

def clear_devolucion_form():
    ID_dev.delete(0, tk.END)
    Pedido_ID_dev.delete(0, tk.END)
    Cliente_ID_dev.delete(0, tk.END)
    FechaSolicitud_dev.delete(0, tk.END)
    FechaProcesado_dev.delete(0, tk.END)
    Motivo_dev.delete(0, tk.END)
    Descripcion_dev.delete(0, tk.END)
    Estado_dev.delete(0, tk.END)
    MontoDevolucion_dev.delete(0, tk.END)
    Empleado_ID_dev.delete(0, tk.END)

# frame para botones_devoluciones
button_frame7 = tk.Frame(tab7)
button_frame7.pack(pady=20)

btn_save_dev = tk.Button(button_frame7, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_devoluciones)
btn_save_dev.pack(side=tk.LEFT, padx=5)

btn_update_dev = tk.Button(button_frame7, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_devolucion)
btn_update_dev.pack(side=tk.LEFT, padx=5)

btn_delete_dev = tk.Button(button_frame7, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_devolucion)
btn_delete_dev.pack(side=tk.LEFT, padx=5)

btn_clear_dev = tk.Button(button_frame7, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_devolucion_form)
btn_clear_dev.pack(side=tk.LEFT, padx=5)


# contenido 8 - pestaña empleados ----------------------------------------------------------------------------------
titulo8 = tk.Label(tab8, text="GESTION - EMPLEADOS", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo8.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame_empleados = tk.Frame(tab8)
form_frame_empleados.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame_empleados, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_empleado.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Nombre
tk.Label(form_frame_empleados, text="Nombre:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Nombre_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Nombre_empleado.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Apellido
tk.Label(form_frame_empleados, text="Apellido:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Apellido_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Apellido_empleado.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Email
tk.Label(form_frame_empleados, text="Email:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Email_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Email_empleado.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Teléfono
tk.Label(form_frame_empleados, text="Teléfono:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Telefono_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Telefono_empleado.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Cargo
tk.Label(form_frame_empleados, text="Cargo:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Cargo_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Cargo_empleado.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Departamento
tk.Label(form_frame_empleados, text="Departamento:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Departamento_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Departamento_empleado.grid(row=7, column=1, sticky="w", pady=10)

# fila 8: Fecha de Contratación
tk.Label(form_frame_empleados, text="Fecha Contratación:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_contratacion = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_contratacion.grid(row=8, column=1, sticky="w", pady=10)

# fila 9: Salario
tk.Label(form_frame_empleados, text="Salario:", font=("Arial", 12, "bold")).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
Salario_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Salario_empleado.grid(row=9, column=1, sticky="w", pady=10)

# fila 10: Supervisor ID
tk.Label(form_frame_empleados, text="Supervisor ID:", font=("Arial", 12, "bold")).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
Supervisor_id = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Supervisor_id.grid(row=10, column=1, sticky="w", pady=10)

# fila 11: Estado
tk.Label(form_frame_empleados, text="Estado:", font=("Arial", 12, "bold")).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
Estado_empleado = tk.Entry(form_frame_empleados, width=25, font=("Arial", 12), relief="solid", bd=1)
Estado_empleado.grid(row=11, column=1, sticky="w", pady=10)

# funciones para los botones de empleados
def save_empleado():
    messagebox.showinfo(title="Guardar", message="Empleado guardado correctamente")

def update_empleado():
    messagebox.showinfo(title="Actualizar", message="Empleado actualizado correctamente")

def delete_empleado():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este empleado?"):
        messagebox.showinfo(title="Eliminar", message="Empleado eliminado correctamente")

def clear_empleado_form():
    ID_empleado.delete(0, tk.END)
    Nombre_empleado.delete(0, tk.END)
    Apellido_empleado.delete(0, tk.END)
    Email_empleado.delete(0, tk.END)
    Telefono_empleado.delete(0, tk.END)
    Cargo_empleado.delete(0, tk.END)
    Departamento_empleado.delete(0, tk.END)
    Fecha_contratacion.delete(0, tk.END)
    Salario_empleado.delete(0, tk.END)
    Supervisor_id.delete(0, tk.END)
    Estado_empleado.delete(0, tk.END)

# frame para botones de empleados
button_frame_empleados = tk.Frame(tab8)
button_frame_empleados.pack(pady=20)

btn_save_empleado = tk.Button(button_frame_empleados, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_empleado)
btn_save_empleado.pack(side=tk.LEFT, padx=5)

btn_update_empleado = tk.Button(button_frame_empleados, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_empleado)
btn_update_empleado.pack(side=tk.LEFT, padx=5)

btn_delete_empleado = tk.Button(button_frame_empleados, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_empleado)
btn_delete_empleado.pack(side=tk.LEFT, padx=5)

btn_clear_empleado = tk.Button(button_frame_empleados, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_empleado_form)
btn_clear_empleado.pack(side=tk.LEFT, padx=5)


# contenido 9 - pestaña historial precios ----------------------------------------------------------------------------------
titulo9 = tk.Label(tab9, text="GESTION - HISTORIAL DE PRECIOS", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo9.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame_historial = tk.Frame(tab9)
form_frame_historial.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame_historial, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_historial = tk.Entry(form_frame_historial, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_historial.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Producto_ID
tk.Label(form_frame_historial, text="Producto_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Producto_ID_historial = tk.Entry(form_frame_historial, width=25, font=("Arial", 12), relief="solid", bd=1)
Producto_ID_historial.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Precio Anterior
tk.Label(form_frame_historial, text="Precio Anterior:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Precio_anterior = tk.Entry(form_frame_historial, width=25, font=("Arial", 12), relief="solid", bd=1)
Precio_anterior.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Precio Nuevo
tk.Label(form_frame_historial, text="Precio Nuevo:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Precio_nuevo = tk.Entry(form_frame_historial, width=25, font=("Arial", 12), relief="solid", bd=1)
Precio_nuevo.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Fecha
tk.Label(form_frame_historial, text="Fecha:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_historial = tk.Entry(form_frame_historial, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_historial.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Usuario
tk.Label(form_frame_historial, text="Usuario:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Usuario_historial = tk.Entry(form_frame_historial, width=25, font=("Arial", 12), relief="solid", bd=1)
Usuario_historial.grid(row=6, column=1, sticky="w", pady=10)

# funciones para los botones de historial de precios
def save_historial():
    messagebox.showinfo(title="Guardar", message="Registro de historial de precios guardado correctamente")

def update_historial():
    messagebox.showinfo(title="Actualizar", message="Registro de historial de precios actualizado correctamente")

def delete_historial():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este registro de historial de precios?"):
        messagebox.showinfo(title="Eliminar", message="Registro de historial de precios eliminado correctamente")

def clear_historial_form():
    ID_historial.delete(0, tk.END)
    Producto_ID_historial.delete(0, tk.END)
    Precio_anterior.delete(0, tk.END)
    Precio_nuevo.delete(0, tk.END)
    Fecha_historial.delete(0, tk.END)
    Usuario_historial.delete(0, tk.END)

# frame para botones de historial de precios
button_frame_historial = tk.Frame(tab9)
button_frame_historial.pack(pady=20)

btn_save_historial = tk.Button(button_frame_historial, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_historial)
btn_save_historial.pack(side=tk.LEFT, padx=5)

btn_update_historial = tk.Button(button_frame_historial, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_historial)
btn_update_historial.pack(side=tk.LEFT, padx=5)

btn_delete_historial = tk.Button(button_frame_historial, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_historial)
btn_delete_historial.pack(side=tk.LEFT, padx=5)

btn_clear_historial = tk.Button(button_frame_historial, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_historial_form)
btn_clear_historial.pack(side=tk.LEFT, padx=5)



# contenido 10 - pestaña logs clientes ----------------------------------------------------------------------------------
titulo10 = tk.Label(tab10, text="GESTION - LOGS DE CLIENTES", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo10.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame_logs = tk.Frame(tab10)
form_frame_logs.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame_logs, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_logs = tk.Entry(form_frame_logs, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_logs.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Cliente_ID
tk.Label(form_frame_logs, text="Cliente_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Cliente_ID = tk.Entry(form_frame_logs, width=25, font=("Arial", 12), relief="solid", bd=1)
Cliente_ID.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Acción
tk.Label(form_frame_logs, text="Acción:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Accion = tk.Entry(form_frame_logs, width=25, font=("Arial", 12), relief="solid", bd=1)
Accion.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Fecha
tk.Label(form_frame_logs, text="Fecha:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_logs = tk.Entry(form_frame_logs, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_logs.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Detalles
tk.Label(form_frame_logs, text="Detalles:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Detalles = tk.Entry(form_frame_logs, width=25, font=("Arial", 12), relief="solid", bd=1)
Detalles.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: IP
tk.Label(form_frame_logs, text="IP:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
IP = tk.Entry(form_frame_logs, width=25, font=("Arial", 12), relief="solid", bd=1)
IP.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Usuario
tk.Label(form_frame_logs, text="Usuario:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Usuario_logs = tk.Entry(form_frame_logs, width=25, font=("Arial", 12), relief="solid", bd=1)
Usuario_logs.grid(row=7, column=1, sticky="w", pady=10)

# funciones para los botones de logs de clientes
def save_logs():
    messagebox.showinfo(title="Guardar", message="Registro de log guardado correctamente")

def update_logs():
    messagebox.showinfo(title="Actualizar", message="Registro de log actualizado correctamente")

def delete_logs():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este registro de log?"):
        messagebox.showinfo(title="Eliminar", message="Registro de log eliminado correctamente")

def clear_logs_form():
    ID_logs.delete(0, tk.END)
    Cliente_ID.delete(0, tk.END)
    Accion.delete(0, tk.END)
    Fecha_logs.delete(0, tk.END)
    Detalles.delete(0, tk.END)
    IP.delete(0, tk.END)
    Usuario_logs.delete(0, tk.END)

# frame para botones de logs de clientes
button_frame_logs = tk.Frame(tab10)
button_frame_logs.pack(pady=20)

btn_save_logs = tk.Button(button_frame_logs, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_logs)
btn_save_logs.pack(side=tk.LEFT, padx=5)

btn_update_logs = tk.Button(button_frame_logs, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_logs)
btn_update_logs.pack(side=tk.LEFT, padx=5)

btn_delete_logs = tk.Button(button_frame_logs, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_logs)
btn_delete_logs.pack(side=tk.LEFT, padx=5)

btn_clear_logs = tk.Button(button_frame_logs, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_logs_form)
btn_clear_logs.pack(side=tk.LEFT, padx=5)


# contenido 11 - pestaña pedidos ----------------------------------------------------------------------------------
titulo11 = tk.Label(tab11, text="GESTION - PEDIDOS", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo11.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame_pedidos = tk.Frame(tab11)
form_frame_pedidos.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame_pedidos, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_pedido = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_pedido.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Cliente_ID
tk.Label(form_frame_pedidos, text="Cliente_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Cliente_ID_pedido = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Cliente_ID_pedido.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Empleado_ID
tk.Label(form_frame_pedidos, text="Empleado_ID:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Empleado_ID = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Empleado_ID.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Fecha Pedido
tk.Label(form_frame_pedidos, text="Fecha Pedido:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_pedido = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_pedido.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Fecha Envío
tk.Label(form_frame_pedidos, text="Fecha Envío:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_envio = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_envio.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Fecha Entrega
tk.Label(form_frame_pedidos, text="Fecha Entrega:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_entrega = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_entrega.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Dirección Envío ID
tk.Label(form_frame_pedidos, text="Dirección Envío ID:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Direccion_envio_id = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Direccion_envio_id.grid(row=7, column=1, sticky="w", pady=10)

# fila 8: Dirección Facturación ID
tk.Label(form_frame_pedidos, text="Dirección Facturación ID:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Direccion_facturacion_id = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Direccion_facturacion_id.grid(row=8, column=1, sticky="w", pady=10)

# fila 9: Estado
tk.Label(form_frame_pedidos, text="Estado:", font=("Arial", 12, "bold")).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
Estado_pedido = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Estado_pedido.grid(row=9, column=1, sticky="w", pady=10)

# fila 10: Método Pago
tk.Label(form_frame_pedidos, text="Método Pago:", font=("Arial", 12, "bold")).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
Metodo_pago = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Metodo_pago.grid(row=10, column=1, sticky="w", pady=10)

# fila 11: Referencia Pago
tk.Label(form_frame_pedidos, text="Referencia Pago:", font=("Arial", 12, "bold")).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
Referencia_pago = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Referencia_pago.grid(row=11, column=1, sticky="w", pady=10)

# fila 12: Subtotal
tk.Label(form_frame_pedidos, text="Subtotal:", font=("Arial", 12, "bold")).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=10)
Subtotal = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Subtotal.grid(row=12, column=1, sticky="w", pady=10)

# fila 13: Impuestos
tk.Label(form_frame_pedidos, text="Impuestos:", font=("Arial", 12, "bold")).grid(row=13, column=0, sticky="w", padx=(0, 10), pady=10)
Impuestos = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Impuestos.grid(row=13, column=1, sticky="w", pady=10)

# fila 14: Gastos Envío
tk.Label(form_frame_pedidos, text="Gastos Envío:", font=("Arial", 12, "bold")).grid(row=14, column=0, sticky="w", padx=(0, 10), pady=10)
Gastos_envio = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Gastos_envio.grid(row=14, column=1, sticky="w", pady=10)

# fila 15: Descuento
tk.Label(form_frame_pedidos, text="Descuento:", font=("Arial", 12, "bold")).grid(row=15, column=0, sticky="w", padx=(0, 10), pady=10)
Descuento_pedido = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Descuento_pedido.grid(row=15, column=1, sticky="w", pady=10)

# fila 16: Total
tk.Label(form_frame_pedidos, text="Total:", font=("Arial", 12, "bold")).grid(row=16, column=0, sticky="w", padx=(0, 10), pady=10)
Total = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Total.grid(row=16, column=1, sticky="w", pady=10)

# fila 17: Notas
tk.Label(form_frame_pedidos, text="Notas:", font=("Arial", 12, "bold")).grid(row=17, column=0, sticky="w", padx=(0, 10), pady=10)
Notas = tk.Entry(form_frame_pedidos, width=25, font=("Arial", 12), relief="solid", bd=1)
Notas.grid(row=17, column=1, sticky="w", pady=10)

# funciones para los botones de pedidos
def save_pedido():
    messagebox.showinfo(title="Guardar", message="Pedido guardado correctamente")

def update_pedido():
    messagebox.showinfo(title="Actualizar", message="Pedido actualizado correctamente")

def delete_pedido():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este pedido?"):
        messagebox.showinfo(title="Eliminar", message="Pedido eliminado correctamente")

def clear_pedido_form():
    ID_pedido.delete(0, tk.END)
    Cliente_ID_pedido.delete(0, tk.END)
    Empleado_ID.delete(0, tk.END)
    Fecha_pedido.delete(0, tk.END)
    Fecha_envio.delete(0, tk.END)
    Fecha_entrega.delete(0, tk.END)
    Direccion_envio_id.delete(0, tk.END)
    Direccion_facturacion_id.delete(0, tk.END)
    Estado_pedido.delete(0, tk.END)
    Metodo_pago.delete(0, tk.END)
    Referencia_pago.delete(0, tk.END)
    Subtotal.delete(0, tk.END)
    Impuestos.delete(0, tk.END)
    Gastos_envio.delete(0, tk.END)
    Descuento_pedido.delete(0, tk.END)
    Total.delete(0, tk.END)
    Notas.delete(0, tk.END)

# frame para botones de pedidos
button_frame_pedidos = tk.Frame(tab11)
button_frame_pedidos.pack(pady=20)

btn_save_pedido = tk.Button(button_frame_pedidos, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_pedido)
btn_save_pedido.pack(side=tk.LEFT, padx=5)

btn_update_pedido = tk.Button(button_frame_pedidos, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_pedido)
btn_update_pedido.pack(side=tk.LEFT, padx=5)

btn_delete_pedido = tk.Button(button_frame_pedidos, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_pedido)
btn_delete_pedido.pack(side=tk.LEFT, padx=5)

btn_clear_pedido = tk.Button(button_frame_pedidos, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_pedido_form)
btn_clear_pedido.pack(side=tk.LEFT, padx=5)

# contenido 12 - pestaña preferencias clientes ----------------------------------------------------------------------------------
titulo12 = tk.Label(tab12, text="GESTION - PREFERENCIAS DE CLIENTES", font=("Arial", 16, "bold"), fg="white", bg="darkblue", pady=10, padx=10)
titulo12.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame_preferencias = tk.Frame(tab12)
form_frame_preferencias.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame_preferencias, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_preferencia = tk.Entry(form_frame_preferencias, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_preferencia.grid(row=1, column=1, sticky="w", pady=10)

# fila 2: Cliente_ID
tk.Label(form_frame_preferencias, text="Cliente_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Cliente_ID_preferencia = tk.Entry(form_frame_preferencias, width=25, font=("Arial", 12), relief="solid", bd=1)
Cliente_ID_preferencia.grid(row=2, column=1, sticky="w", pady=10)

# fila 3: Categoria_ID
tk.Label(form_frame_preferencias, text="Categoria_ID:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Categoria_ID = tk.Entry(form_frame_preferencias, width=25, font=("Arial", 12), relief="solid", bd=1)
Categoria_ID.grid(row=3, column=1, sticky="w", pady=10)

# fila 4: Preferencia Marketing
tk.Label(form_frame_preferencias, text="Preferencia Marketing:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Preferencia_marketing = tk.Entry(form_frame_preferencias, width=25, font=("Arial", 12), relief="solid", bd=1)
Preferencia_marketing.grid(row=4, column=1, sticky="w", pady=10)

# fila 5: Notificaciones Email
tk.Label(form_frame_preferencias, text="Notificaciones Email:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Notificaciones_email = tk.Entry(form_frame_preferencias, width=25, font=("Arial", 12), relief="solid", bd=1)
Notificaciones_email.grid(row=5, column=1, sticky="w", pady=10)

# fila 6: Notificaciones SMS
tk.Label(form_frame_preferencias, text="Notificaciones SMS:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Notificaciones_sms = tk.Entry(form_frame_preferencias, width=25, font=("Arial", 12), relief="solid", bd=1)
Notificaciones_sms.grid(row=6, column=1, sticky="w", pady=10)

# fila 7: Fecha Actualización
tk.Label(form_frame_preferencias, text="Fecha Actualización:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Fecha_actualizacion = tk.Entry(form_frame_preferencias, width=25, font=("Arial", 12), relief="solid", bd=1)
Fecha_actualizacion.grid(row=7, column=1, sticky="w", pady=10)

# funciones para los botones de preferencias de clientes
def save_preferencia():
    messagebox.showinfo(title="Guardar", message="Preferencia de cliente guardada correctamente")

def update_preferencia():
    messagebox.showinfo(title="Actualizar", message="Preferencia de cliente actualizada correctamente")

def delete_preferencia():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar esta preferencia de cliente?"):
        messagebox.showinfo(title="Eliminar", message="Preferencia de cliente eliminada correctamente")

def clear_preferencia_form():
    ID_preferencia.delete(0, tk.END)
    Cliente_ID_preferencia.delete(0, tk.END)
    Categoria_ID.delete(0, tk.END)
    Preferencia_marketing.delete(0, tk.END)
    Notificaciones_email.delete(0, tk.END)
    Notificaciones_sms.delete(0, tk.END)
    Fecha_actualizacion.delete(0, tk.END)

# frame para botones de preferencias de clientes
button_frame_preferencias = tk.Frame(tab12)
button_frame_preferencias.pack(pady=20)

btn_save_preferencia = tk.Button(button_frame_preferencias, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_preferencia)
btn_save_preferencia.pack(side=tk.LEFT, padx=5)

btn_update_preferencia = tk.Button(button_frame_preferencias, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_preferencia)
btn_update_preferencia.pack(side=tk.LEFT, padx=5)

btn_delete_preferencia = tk.Button(button_frame_preferencias, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_preferencia)
btn_delete_preferencia.pack(side=tk.LEFT, padx=5)

btn_clear_preferencia = tk.Button(button_frame_preferencias, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_preferencia_form)
btn_clear_preferencia.pack(side=tk.LEFT, padx=5)

# Contenido tabla 13 -
# contenido 13 pestaña producto_proveedor ----------------------------------------------------------------------------------
titulo13 = tk.Label(tab13,text="GESTION - PRODUCTO_PROVEEDOR",font=("Arial", 16, "bold"),fg="white",bg="darkblue",pady=10,padx=10)
titulo13.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame13 = tk.Frame(tab13)
form_frame13.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame13, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_pp.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Producto_ID
tk.Label(form_frame13, text="Producto_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Producto_ID_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
Producto_ID_pp.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Proveedor_ID
tk.Label(form_frame13, text="Proveedor_ID:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Proveedor_ID_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
Proveedor_ID_pp.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Precio_Compra
tk.Label(form_frame13, text="Precio_Compra:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Precio_Compra_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
Precio_Compra_pp.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Tiempo_Entrega
tk.Label(form_frame13, text="Tiempo_Entrega:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Tiempo_Entrega_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
Tiempo_Entrega_pp.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Cantidad_Minima
tk.Label(form_frame13, text="Cantidad_Minima:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Cantidad_Minima_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
Cantidad_Minima_pp.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Es_Proveedor_Principal
tk.Label(form_frame13, text="Es_Proveedor_Principal:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Es_Proveedor_Principal_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
Es_Proveedor_Principal_pp.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: Ultima_Compra
tk.Label(form_frame13, text="Ultima_Compra:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Ultima_Compra_pp = tk.Entry(form_frame13, width=25, font=("Arial", 12), relief="solid", bd=1)
Ultima_Compra_pp.grid(row=8, column=1, sticky="w", pady=10)

# CONFIGURACION DE MENSAJES DE LOS BOTONES
def save_producto_proveedor():
    messagebox.showinfo(title="Guardar", message="Relación Producto-Proveedor guardada correctamente")

def update_producto_proveedor():
    messagebox.showinfo(title="Actualizar", message="Relación Producto-Proveedor actualizada correctamente")

def delete_producto_proveedor():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar esta relación Producto-Proveedor?"):
        messagebox.showinfo(title="Eliminar", message="Relación Producto-Proveedor eliminada correctamente")

def clear_producto_proveedor_form():
    ID_pp.delete(0, tk.END)
    Producto_ID_pp.delete(0, tk.END)
    Proveedor_ID_pp.delete(0, tk.END)
    Precio_Compra_pp.delete(0, tk.END)
    Tiempo_Entrega_pp.delete(0, tk.END)
    Cantidad_Minima_pp.delete(0, tk.END)
    Es_Proveedor_Principal_pp.delete(0, tk.END)
    Ultima_Compra_pp.delete(0, tk.END)

# frame para botones_producto_proveedor
button_frame13 = tk.Frame(tab13)
button_frame13.pack(pady=20)

btn_save_pp = tk.Button(button_frame13, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_producto_proveedor)
btn_save_pp.pack(side=tk.LEFT, padx=5)

btn_update_pp = tk.Button(button_frame13, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_producto_proveedor)
btn_update_pp.pack(side=tk.LEFT, padx=5)

btn_delete_pp = tk.Button(button_frame13, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_producto_proveedor)
btn_delete_pp.pack(side=tk.LEFT, padx=5)

btn_clear_pp = tk.Button(button_frame13, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_producto_proveedor_form)
btn_clear_pp.pack(side=tk.LEFT, padx=5)


# contenido 14 pestaña productos ----------------------------------------------------------------------------------
titulo14 = tk.Label(tab14,text="GESTION - PRODUCTOS",font=("Arial", 16, "bold"),fg="white",bg="darkblue",pady=10,padx=10)
titulo14.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame14 = tk.Frame(tab14)
form_frame14.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame14, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_p.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Categoria_ID
tk.Label(form_frame14, text="Categoria_ID:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Categoria_ID_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Categoria_ID_p.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Nombre
tk.Label(form_frame14, text="Nombre:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Nombre_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Nombre_p.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Descripcion
tk.Label(form_frame14, text="Descripcion:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Descripcion_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Descripcion_p.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Precio
tk.Label(form_frame14, text="Precio:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Precio_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Precio_p.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Precio_Oferta
tk.Label(form_frame14, text="Precio_Oferta:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Precio_Oferta_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Precio_Oferta_p.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Stock
tk.Label(form_frame14, text="Stock:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Stock_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Stock_p.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: Codigo_SKU
tk.Label(form_frame14, text="Codigo_SKU:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Codigo_SKU_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Codigo_SKU_p.grid(row=8, column=1, sticky="w", pady=10)

# Fila 9: Imagen
tk.Label(form_frame14, text="Imagen:", font=("Arial", 12, "bold")).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
Imagen_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Imagen_p.grid(row=9, column=1, sticky="w", pady=10)

# Fila 10: Peso
tk.Label(form_frame14, text="Peso:", font=("Arial", 12, "bold")).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
Peso_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Peso_p.grid(row=10, column=1, sticky="w", pady=10)

# Fila 11: Dimensiones
tk.Label(form_frame14, text="Dimensiones:", font=("Arial", 12, "bold")).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
Dimensiones_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Dimensiones_p.grid(row=11, column=1, sticky="w", pady=10)

# Fila 12: Destacado
tk.Label(form_frame14, text="Destacado:", font=("Arial", 12, "bold")).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=10)
Destacado_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Destacado_p.grid(row=12, column=1, sticky="w", pady=10)

# Fila 13: Creado
tk.Label(form_frame14, text="Creado:", font=("Arial", 12, "bold")).grid(row=13, column=0, sticky="w", padx=(0, 10), pady=10)
Creado_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Creado_p.grid(row=13, column=1, sticky="w", pady=10)

# Fila 14: Actualizado
tk.Label(form_frame14, text="Actualizado:", font=("Arial", 12, "bold")).grid(row=14, column=0, sticky="w", padx=(0, 10), pady=10)
Actualizado_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Actualizado_p.grid(row=14, column=1, sticky="w", pady=10)

# Fila 15: Estado
tk.Label(form_frame14, text="Estado:", font=("Arial", 12, "bold")).grid(row=15, column=0, sticky="w", padx=(0, 10), pady=10)
Estado_p = tk.Entry(form_frame14, width=25, font=("Arial", 12), relief="solid", bd=1)
Estado_p.grid(row=15, column=1, sticky="w", pady=10)

# CONFIGURACION DE MENSAJES DE LOS BOTONES
def save_productos():
    messagebox.showinfo(title="Guardar", message="Producto guardado correctamente")

def update_productos():
    messagebox.showinfo(title="Actualizar", message="Producto actualizado correctamente")

def delete_productos():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este producto?"):
        messagebox.showinfo(title="Eliminar", message="Producto eliminado correctamente")

def clear_productos_form():
    ID_p.delete(0, tk.END)
    Categoria_ID_p.delete(0, tk.END)
    Nombre_p.delete(0, tk.END)
    Descripcion_p.delete(0, tk.END)
    Precio_p.delete(0, tk.END)
    Precio_Oferta_p.delete(0, tk.END)
    Stock_p.delete(0, tk.END)
    Codigo_SKU_p.delete(0, tk.END)
    Imagen_p.delete(0, tk.END)
    Peso_p.delete(0, tk.END)
    Dimensiones_p.delete(0, tk.END)
    Destacado_p.delete(0, tk.END)
    Creado_p.delete(0, tk.END)
    Actualizado_p.delete(0, tk.END)
    Estado_p.delete(0, tk.END)

# frame para botones_productos
button_frame14 = tk.Frame(tab14)
button_frame14.pack(pady=20)

btn_save_p = tk.Button(button_frame14, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_productos)
btn_save_p.pack(side=tk.LEFT, padx=5)

btn_update_p = tk.Button(button_frame14, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_productos)
btn_update_p.pack(side=tk.LEFT, padx=5)

btn_delete_p = tk.Button(button_frame14, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_productos)
btn_delete_p.pack(side=tk.LEFT, padx=5)

btn_clear_p = tk.Button(button_frame14, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_productos_form)
btn_clear_p.pack(side=tk.LEFT, padx=5)

# contenido 15 pestaña proveedores ----------------------------------------------------------------------------------
titulo15 = tk.Label(tab15,text="GESTION - PROVEEDORES",font=("Arial", 16, "bold"),fg="white",bg="darkblue",pady=10,padx=10)
titulo15.pack(pady=10, fill="x")

# frame para contener el formulario
form_frame15 = tk.Frame(tab15)
form_frame15.pack(pady=20, anchor="w", padx=50)

# fila 1: ID
tk.Label(form_frame15, text="ID:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ID_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
ID_pr.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Nombre
tk.Label(form_frame15, text="Nombre:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
Nombre_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Nombre_pr.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Contacto_Nombre
tk.Label(form_frame15, text="Contacto_Nombre:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
Contacto_Nombre_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Contacto_Nombre_pr.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Contacto_Telefono
tk.Label(form_frame15, text="Contacto_Telefono:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
Contacto_Telefono_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Contacto_Telefono_pr.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Email
tk.Label(form_frame15, text="Email:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
Email_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Email_pr.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Telefono
tk.Label(form_frame15, text="Telefono:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Telefono_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Telefono_pr.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Direccion
tk.Label(form_frame15, text="Direccion:", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
Direccion_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Direccion_pr.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: Ciudad
tk.Label(form_frame15, text="Ciudad:", font=("Arial", 12, "bold")).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
Ciudad_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Ciudad_pr.grid(row=8, column=1, sticky="w", pady=10)

# Fila 9: Codigo_Postal
tk.Label(form_frame15, text="Codigo_Postal:", font=("Arial", 12, "bold")).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
Codigo_Postal_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Codigo_Postal_pr.grid(row=9, column=1, sticky="w", pady=10)

# Fila 10: Pais
tk.Label(form_frame15, text="Pais:", font=("Arial", 12, "bold")).grid(row=10, column=0, sticky="w", padx=(0, 10), pady=10)
Pais_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Pais_pr.grid(row=10, column=1, sticky="w", pady=10)

# Fila 11: Notas
tk.Label(form_frame15, text="Notas:", font=("Arial", 12, "bold")).grid(row=11, column=0, sticky="w", padx=(0, 10), pady=10)
Notas_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Notas_pr.grid(row=11, column=1, sticky="w", pady=10)

# Fila 12: Creado
tk.Label(form_frame15, text="Creado:", font=("Arial", 12, "bold")).grid(row=12, column=0, sticky="w", padx=(0, 10), pady=10)
Creado_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Creado_pr.grid(row=12, column=1, sticky="w", pady=10)

# Fila 13: Actualizado
tk.Label(form_frame15, text="Actualizado:", font=("Arial", 12, "bold")).grid(row=13, column=0, sticky="w", padx=(0, 10), pady=10)
Actualizado_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Actualizado_pr.grid(row=13, column=1, sticky="w", pady=10)

# Fila 14: Estado
tk.Label(form_frame15, text="Estado:", font=("Arial", 12, "bold")).grid(row=14, column=0, sticky="w", padx=(0, 10), pady=10)
Estado_pr = tk.Entry(form_frame15, width=25, font=("Arial", 12), relief="solid", bd=1)
Estado_pr.grid(row=14, column=1, sticky="w", pady=10)

# CONFIGURACION DE MENSAJES DE LOS BOTONES
def save_proveedores():
    messagebox.showinfo(title="Guardar", message="Proveedor guardado correctamente")

def update_proveedores():
    messagebox.showinfo(title="Actualizar", message="Proveedor actualizado correctamente")

def delete_proveedores():
    if messagebox.askyesno(title="Eliminar", message="¿Está seguro de eliminar este proveedor?"):
        messagebox.showinfo(title="Eliminar", message="Proveedor eliminado correctamente")

def clear_proveedores_form():
    ID_pr.delete(0, tk.END)
    Nombre_pr.delete(0, tk.END)
    Contacto_Nombre_pr.delete(0, tk.END)
    Contacto_Telefono_pr.delete(0, tk.END)
    Email_pr.delete(0, tk.END)
    Telefono_pr.delete(0, tk.END)
    Direccion_pr.delete(0, tk.END)
    Ciudad_pr.delete(0, tk.END)
    Codigo_Postal_pr.delete(0, tk.END)
    Pais_pr.delete(0, tk.END)
    Notas_pr.delete(0, tk.END)
    Creado_pr.delete(0, tk.END)
    Actualizado_pr.delete(0, tk.END)
    Estado_pr.delete(0, tk.END)

# frame para botones_proveedores
button_frame15 = tk.Frame(tab15)
button_frame15.pack(pady=20)

btn_save_pr = tk.Button(button_frame15, text="Guardar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=save_proveedores)
btn_save_pr.pack(side=tk.LEFT, padx=5)

btn_update_pr = tk.Button(button_frame15, text="Actualizar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=update_proveedores)
btn_update_pr.pack(side=tk.LEFT, padx=5)

btn_delete_pr = tk.Button(button_frame15, text="Eliminar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=delete_proveedores)
btn_delete_pr.pack(side=tk.LEFT, padx=5)

btn_clear_pr = tk.Button(button_frame15, text="Limpiar", font=("Arial", 12, "bold"), bg="black", fg="white", width=10, command=clear_proveedores_form)
btn_clear_pr.pack(side=tk.LEFT, padx=5)


ventana.mainloop()
