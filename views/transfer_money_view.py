
import tkinter as tk
from tkinter import ttk, messagebox


class TransferMoneyView(tk.Toplevel):
    def __init__(self, parent, controller, user_id):
        super().__init__(parent)
        self.controller = controller
        self.user_id = user_id
        self.user_accounts = {}

        self.title("Transferir Dinero")
        self.geometry("450x300")
        self.resizable(False, False)
        self.grab_set()

        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(1, weight=1)

        ttk.Label(main_frame, text="Cuenta de Origen:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        self.source_account_combo = ttk.Combobox(main_frame, state="readonly")
        self.source_account_combo.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        ttk.Label(main_frame, text="Cuenta de Destino:").grid(row=1, column=0, padx=5, pady=10, sticky="w")
        self.dest_account_entry = ttk.Entry(main_frame)
        self.dest_account_entry.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

        ttk.Label(main_frame, text="Monto:").grid(row=2, column=0, padx=5, pady=10, sticky="w")
        self.amount_entry = ttk.Entry(main_frame)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        ttk.Label(main_frame, text="Nota (opcional):").grid(row=3, column=0, padx=5, pady=10, sticky="w")
        self.note_entry = ttk.Entry(main_frame)
        self.note_entry.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

        transfer_button = ttk.Button(main_frame, text="Realizar Transferencia", command=self.transfer_button_clicked)
        transfer_button.grid(row=4, column=0, columnspan=2, pady=20)

        self.load_user_accounts()

    def load_user_accounts(self):
        accounts, error = self.controller.get_accounts_for_view(self.user_id)
        if error:
            messagebox.showerror("Error", error, parent=self)
            self.destroy()
            return

        if not accounts:
            messagebox.showwarning("Sin Cuentas", "No tienes cuentas activas para transferir.", parent=self)
            self.destroy()
            return

        account_list = []
        for acc_id, acc_num, acc_bal in accounts:
            display_text = f"{acc_num} (Saldo: ${acc_bal:,.2f})"
            account_list.append(display_text)
            self.user_accounts[display_text] = acc_id

        self.source_account_combo['values'] = account_list
        self.source_account_combo.current(0)

    def transfer_button_clicked(self):
        selected_account_text = self.source_account_combo.get()
        dest_account_number = self.dest_account_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        note = self.note_entry.get().strip()

        if not all([selected_account_text, dest_account_number, amount_str]):
            messagebox.showerror("Error", "Todos los campos (excepto la nota) son obligatorios.", parent=self)
            return

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido.", parent=self)
            return

        source_account_id = self.user_accounts[selected_account_text]
        self.controller.handle_transfer(source_account_id, dest_account_number, amount, note, self)