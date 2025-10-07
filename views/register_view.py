import tkinter as tk


class RegisterView(tk.Toplevel):
    def __init__(self, user_controller):
        super().__init__()
        self.user_controller = user_controller
        self.title("Registro de usuario")
        self.geometry("400x230")
        self.resizable(width=False, height=False)

        self.user_label = tk.Label(self, text="Usuario:")
        self.user_entry = tk.Entry(self)

        self.password_label = tk.Label(self, text="Contraseña:")
        self.password_entry = tk.Entry(self, show="*")

        self.name_label = tk.Label(self, text="Nombre:")
        self.name_entry = tk.Entry(self)

        self.lastname_label = tk.Label(self, text="Apellido:")
        self.lastname_entry = tk.Entry(self)

        self.register_button = tk.Button(self, text="Registrar", command=self.register_button_clicked)

        # --- Layout ---
        self.user_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.user_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.name_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.lastname_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.lastname_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.register_button.grid(row=4, column=0, columnspan=2, pady=15)

    def register_button_clicked(self):
        username = self.user_entry.get()
        password = self.password_entry.get()
        name = self.name_entry.get()
        lastname = self.lastname_entry.get()
        self.user_controller.handle_register_window(username, password, name, lastname,self)