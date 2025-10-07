from mysql.connector import IntegrityError
from mysql.connector.errors import Error, IntegrityError
from tkinter import messagebox

from db.db_conector import DBConnector
class UserModel:
    def __init__(self):
        pass
    def create_user(self, username, password, name, lastname):
        conn = DBConnector.get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (username, password, name, lastname) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, password, name, lastname))
            conn.commit()
            return True
        except IntegrityError as e:
            messagebox.showerror("Error de registro", e)
            return False
        except Error as e:
            messagebox.showerror("Error de registro", e)

            return False

        finally:
            if conn.is_connected():
                conn.close()

    def validate_login(self, username, password):
        conn = DBConnector.get_connection()
        if not conn:
            messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos.")
            return None

        try:
            cursor = conn.cursor()
            query = "SELECT id, name, lastname FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user_data = cursor.fetchone()
            if user_data:
                return user_data
            else:
                return None

        except Error as e:
            print("Error al validar login:", e)
            messagebox.showerror("Error de base de datos", "Ocurrió un error al intentar iniciar sesión.")
            return None

        finally:
            if conn and conn.is_connected():
                conn.close()