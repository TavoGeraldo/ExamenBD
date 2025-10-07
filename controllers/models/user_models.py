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


