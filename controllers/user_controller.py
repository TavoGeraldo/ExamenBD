from views.login_view import LoginView
from views.register_view import RegisterView
from views.main_view import MainView
from views.create_account_view import CreateAccountView
from models.account_model import AccountModel
from views.transfer_money_view import TransferMoneyView



from tkinter import messagebox

class UserController:
    def __init__(self, user_model):

        self.user_model = user_model
        self.account_model = AccountModel()
        self.login_view = None
        self.register_view = None

    def run(self):
        self.login_view = LoginView(self)
        self.login_view.mainloop()

    def show_register_window(self):
        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = RegisterView(self)
        self.register_view.lift()

    def handle_register_window(self, username, password, name, lastname, window):
        if not all([username, password, name, lastname]):
            messagebox.showerror(title="Error", message="Username or password is incorrect")
            return

        if self.user_model.create_user(username, password, name, lastname):
            messagebox.showinfo(title="Success", message="User created successfully")
            window.destroy()

    def handle_login(self, username, password):
        if not username or not password:
            messagebox.showerror("Error", "Ingrese usuario y contraseña")
            return


        user_data = self.user_model.validate_login(username, password)

        if user_data:

            user_name = user_data[1]

            messagebox.showinfo("Éxito", f"Bienvenido {user_name}")

            self.login_view.withdraw()


            self.show_main_view(user_data)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def show_main_view(self, user_data):
        self.main_view = MainView(user_data, self)
        self.main_view.protocol("WM_DELETE_WINDOW", self.logout)
        self.main_view.grab_set()

    def logout(self):
        if self.main_view:
            self.main_view.destroy()
            self.main_view = None

        if self.login_view:
            self.login_view.deiconify()

    def show_create_account_view(self, user_id):
        CreateAccountView(self.main_view, self, user_id)

    def handle_create_account(self, user_id, initial_balance, window):

        success, message, new_account_number = self.account_model.create_account(user_id, initial_balance)

        if success:
            full_message = f"{message}\n\nSu nuevo número de cuenta es:\n{new_account_number}"
            messagebox.showinfo("Éxito", full_message, parent=window)
            window.destroy()
        else:
            messagebox.showerror("Error", message, parent=window)

    def get_accounts_for_view(self, user_id):
        return self.account_model.get_user_accounts(user_id)

    def show_transfer_money_view(self, user_id):
        return TransferMoneyView(self.main_view, self, user_id)

    def handle_transfer(self, source_id, dest_num, amount, note, window):
        success, message = self.account_model.transfer_money(source_id, dest_num, amount, note)
        if success:
            messagebox.showinfo("Éxito", message, parent=window)
            window.destroy()
        else:
            messagebox.showerror("Error", message, parent=window)





