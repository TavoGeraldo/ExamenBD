import tkinter as tk
from tkinter import ttk, messagebox


class MainView(tk.Toplevel):
    def __init__(self, user_data, controller):
        super().__init__()
        self.title("Panel Principal")
        self.geometry("500x480")
        self.resizable(False, False)

        self.controller = controller
        self.user_id = user_data[0]
        self.user_name = user_data[1]
        self.user_lastname = user_data[2]

        welcome_frame = ttk.Frame(self, padding="10")
        welcome_frame.pack(fill=tk.X)
        ttk.Label(
            welcome_frame,
            text=f"¡Bienvenido, {self.user_name} {self.user_lastname}!",
            font=("Arial", 14, "bold")
        ).pack()

        accounts_frame = ttk.Frame(self, padding="10")
        accounts_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(accounts_frame, text="Mis Cuentas", font=("Arial", 12)).pack(anchor="w")

        columns = ("numero_cuenta", "saldo")
        self.tree = ttk.Treeview(accounts_frame, columns=columns, show="headings", height=5)

        self.tree.heading("numero_cuenta", text="Número de Cuenta")
        self.tree.heading("saldo", text="Saldo Actual")
        self.tree.column("numero_cuenta", width=250, anchor=tk.W)
        self.tree.column("saldo", width=150, anchor=tk.E)

        style = ttk.Style()
        style.map('Treeview', background=[('selected', '#0078D7')])
        self.tree.tag_configure('oddrow', background='#F0F0F0')
        self.tree.tag_configure('evenrow', background='white')

        self.tree.pack(fill=tk.X, expand=False, pady=5)

        buttons_frame = ttk.Frame(self, padding="10")
        buttons_frame.pack(fill=tk.X, side=tk.BOTTOM)

        ttk.Button(buttons_frame, text="Crear Nueva Cuenta", command=self.create_account).pack(fill=tk.X, pady=3)
        ttk.Button(buttons_frame, text="Transferir Dinero", command=self.transfer_money).pack(fill=tk.X, pady=3)
        ttk.Button(buttons_frame, text="Consultar Historial", command=self.show_movements).pack(fill=tk.X, pady=3)
        ttk.Button(buttons_frame, text="Cerrar Sesión", command=self.close_session).pack(fill=tk.X, pady=10)

        self.load_accounts()

    def load_accounts(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        accounts, error = self.controller.get_accounts_for_view(self.user_id)

        if error:
            messagebox.showerror("Error", f"No se pudieron cargar las cuentas: {error}")
            return

        if accounts:
            for i, (acc_id, acc_num, acc_bal) in enumerate(accounts):
                saldo_formateado = f"${acc_bal:,.2f}"
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                self.tree.insert("", tk.END, values=(acc_num, saldo_formateado), tags=(tag,))

    def create_account(self):
        create_window = self.controller.show_create_account_view(self.user_id)
        self.wait_window(create_window)
        self.load_accounts()

    def transfer_money(self):
        transfer_window = self.controller.show_transfer_money_view(self.user_id)
        self.wait_window(transfer_window)
        self.load_accounts()

    def show_movements(self):
        messagebox.showinfo("Historial", "Historial.")


    def close_session(self):
        self.controller.logout()
