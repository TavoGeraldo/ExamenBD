# Proyecto Fintech

Sistema de gestión bancaria para una Fintech, desarrollado en Python con una base de datos MySQL.

## 🛠️ Tecnologías y Herramientas

* **Python:** Lenguaje principal de la aplicación.
* **Tkinter:** Para la construcción de la interfaz gráfica.
* **MySQL:** Como sistema gestor de la base de datos.
* **PyCharm:** IDE de desarrollo.
* **PyInstaller:** Para la generación del archivo ejecutable `.exe`.

## 📦 Instalación y Ejecución

### 1. Preparar la Base de Datos
* Asegúrate de tener un servidor de **MySQL** instalado y en ejecución.
* Ejecutar el archivo `FintechDB.sql` para crear la base de datos, tablas y procedimientos.
* Verificar que las credenciales en el archivo `.env` coincidan con la configuración de MySQL.

### 2. Ejecutar la Aplicación
1.  Descomprime el archivo `entrega_fintech.zip`.
2.  Abre la carpeta `entrega_fintech`.
3.  Haz doble clic en el archivo `app.exe` para iniciar el programa.
4.  **Importante:** Asegúrate de que el archivo `.env` esté en la misma carpeta que `app.exe`.

## 🚀 Uso y Ejemplos de Operaciones

Primero, inicia sesión con uno de los siguientes usuarios de prueba:
* **Usuario 1:** `profe` / **Contraseña:** `pass123`
* **Usuario 2:** `alumno` / **Contraseña:** `pass456`

Una vez dentro, puedes probar las funcionalidades principales:

### Ejemplo 1: Crear una Nueva Cuenta Bancaria
1.  Inicia sesión con cualquiera de los usuarios.
2.  Haz clic en el botón **"Crear Nueva Cuenta"**.
3.  Ingresa un saldo inicial (ej: `500.00`).
4.  Haz clic en **"Crear Cuenta"**.
5.  Una alerta te mostrará el nuevo número de cuenta. Al cerrar la alerta, el panel principal se actualizará.

### Ejemplo 2: Transferir Dinero entre Cuentas
1.  Inicia sesión con un usuario que tenga saldo (ej: `profe`).
2.  Copia el número de cuenta de otro usuario (ej: `alumno`) desde el panel principal.
3.  Haz clic en **"Transferir Dinero"**.
4.  En la nueva ventana, selecciona tu cuenta de origen, pega la cuenta de destino e ingresa un monto.
5.  Haz clic en **"Realizar Transferencia"**. El panel principal se actualizará automáticamente al cerrar la ventana de transferencia.

## 👨‍💻 Autor

* Octavio Geraldo Geraldo
