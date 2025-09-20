# Sistema Comercial - Interfaz de Gestión

Descripción --------------------

Interfaz gráfica para un sistema comercial completo que incluye formularios para administrar todas las tablas de una
base de datos de comercio electrónico. Esta versión incluye el diseño completo de la interfaz pero aún no tiene implementada
la lógica de negocio ni la conexión a base de datos.

Características ------------------

- 15 tablas diferentes**: Alertas, Categorías, Clientes, Clientes_Direcciones, Detalles_Devolucion, Detalles_pedido,
 Devoluciones, Empleados, Historial_Pedidos, Logs_Clientes, Pedidos, Prefe_Clientes, Prod_proveedor, Productos y Proveedores
- Interfaz intuitiva organizada por pestañas
- Diseño uniforme con botones de acción para cada formulario
- Campos de entrada para todos los atributos de cada tabla
- Mensajes de confirmación para las operaciones CRUD
- Diseño responsive y organizado

Nota importante -----------------------

- Esta versión solo incluye la interfaz gráfica, la funcionalidad de los botones está simulada con mensajes emergentes
- Los datos ingresados en los formularios no se GUARDARAN en la base de datos real
- La aplicación muestra la estructura completa pero requiere implementación de la base de datos paraser gestionada

Requisitos Previos -----------------------

- Python 3.6 o superior
- pip (gestor de paquetes de Python)
- Módulos estándar de Python (tkinter, ttk, messagebox)

Instalación -------------------

1. Clona o descarga el proyecto en tu equipo
2. Abre una terminal en la carpeta del proyecto
3. Ejecuta el archivo principal:
   ```
   python sistema_comercial.py
   ```

Estructura de la Aplicación -------------------------

La interfaz está organizada en 15 pestañas, cada una correspondiente a una tabla de la base de datos:

1. **Alertas**: Gestión de alertas del sistema de inventario
2. **Categorías**: Administración de categorías de productos
3. **Clientes**: Gestión de información de clientes
4. **Clientes_Direcciones**: Direcciones asociadas a clientes
5. **Detalles_Devolucion**: Detalles de productos devueltos
6. **Detalles_pedido**: Elementos individuales de cada pedido
7. **Devoluciones**: Registro de devoluciones completas
8. **Empleados**: Información del personal
9. **Historial_Pedidos**: Seguimiento histórico de pedidos
10. **Logs_Clientes**: Registro de actividades de clientes
11. **Pedidos**: Encabezados de pedidos
12. **Prefe_Clientes**: Preferencias de clientes
13. **Prod_proveedor**: Relación productos-proveedores
14. **Productos**: Catálogo completo de productos
15. **Proveedores**: Información de proveedores

Funcionalidades por Tabla ---------------------------

Cada pestaña incluye:
- Formulario con todos los campos de la tabla correspondiente
- Botones de acción (Guardar, Actualizar, Eliminar, Limpiar)
- Validaciones básicas mediante mensajes emergentes
- Diseño consistente y fácil de usar

Próximos Pasos para Implementación Completa ------------------

- Conexión a base de datos MySQL/PostgreSQL/SQLite
- Implementación de operaciones CRUD reales
- Validación de datos en campos de entrada
- Implementación de autenticación de usuarios
- Mecanismos de backup y recuperación de datos
- Reportes y estadísticas

