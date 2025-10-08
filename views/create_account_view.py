import tkinter as tk
from tkinter import ttk, messagebox


class CreateAccountView(tk.Toplevel):
    def __init__(self, parent, controller, user_id):
        super().__init__(parent)
        self.controller = controller
        self.user_id = user_id

        self.title("Crear Nueva Cuenta")
        self.geometry("350x150")
        self.resizable(False, False)
        self.grab_set()

        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Saldo Inicial:").grid(row=0, column=0, padx=5, pady=10)
        self.balance_entry = ttk.Entry(main_frame, width=20)
        self.balance_entry.grid(row=0, column=1, padx=5, pady=10)
        self.balance_entry.insert(0, "0.00")

        create_button = ttk.Button(main_frame, text="Crear Cuenta", command=self.create_account_clicked)
        create_button.grid(row=1, column=0, columnspan=2, pady=20)

    def _limpiar_y_convertir_monto(self, texto_monto):
        if not isinstance(texto_monto, str):
            return None

        texto_limpio = texto_monto.replace(",", "").replace("$", "")

        try:
            return float(texto_limpio)
        except (ValueError, TypeError):
            return None

    def create_account_clicked(self):
        balance_str = self.balance_entry.get().strip()

        if not balance_str:
            messagebox.showerror("Error de validación", "El campo de saldo no puede estar vacío.", parent=self)
            return

        initial_balance = self._limpiar_y_convertir_monto(balance_str)

        if initial_balance is None:
            messagebox.showerror("Error de validación", "Por favor, ingrese un monto válido (solo números).",
                                 parent=self)
            return

        if initial_balance < 0:
            messagebox.showerror("Error de validación", "El saldo inicial no puede ser negativo.", parent=self)
            return

        self.controller.handle_create_account(self.user_id, initial_balance, self)