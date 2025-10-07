import tkinter as tk
from tkinter import messagebox


class MainView(tk.Toplevel):
    def __init__(self, user_data, controller):
        super().__init__()
        self.title("Panel Principal")
        self.geometry("400x300")
        self.resizable(False, False)

        self.controller = controller

        self.user_data = user_data


        self.user_id = user_data[0]
        self.user_name = user_data[1]
        self.user_lastname = user_data[2]


        tk.Label(
            self,
            text=f"Bienvenido, {self.user_name} {self.user_lastname}!",
            font=("Arial", 14, "bold")
        ).pack(pady=20)

        # --- Botones de opciones ---
        tk.Button(self, text="Crear nueva cuenta bancaria", width=30,
                  command=self.create_account).pack(pady=10)

        tk.Button(self, text="Transferir dinero", width=30,
                  command=self.transfer_money).pack(pady=10)

        tk.Button(self, text="Consultar historial de movimientos", width=30,
                  command=self.show_movements).pack(pady=10)

        tk.Button(self, text="Cerrar sesión", width=30,
                  command=self.close_session).pack(pady=10)

    def create_account(self):
        self.controller.show_create_account_view(self.user_id)
        messagebox.showinfo("Cuenta", "Función: Crear nueva cuenta bancaria")

    def transfer_money(self):
        messagebox.showinfo("Transferencia", "Función: Transferir dinero")

    def show_movements(self):
        messagebox.showinfo("Movimientos", "Función: Consultar historial de movimientos")

    def close_session(self):
        messagebox.showinfo("Salir", "Sesión cerrada correctamente")
        self.destroy()
