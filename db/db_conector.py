import mysql.connector
from mysql.connector import Error, IntegrityError
from config.db import DB_config
from tkinter import messagebox

class DBConnector:
    @staticmethod
    def get_connection():
        try:
            conn = mysql.connector.connect(**DB_config)
            if conn.is_connected():
                return conn
        except Error as e:
            messagebox.showerror("Error de conexion", e)
            return None