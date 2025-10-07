from views.login_view import LoginView
from views.register_view import RegisterView
from tkinter import messagebox

class UserController:
    def __init__(self, user_model):

        self.user_model = user_model
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

