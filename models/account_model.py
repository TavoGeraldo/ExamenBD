from db.db_conector import DBConnector
from mysql.connector import Error

class AccountModel:
    def create_account(self, user_id, initial_balance):
        conn = DBConnector.get_connection()
        if not conn:
            return False, "Error de conexión a la base de datos.", None

        try:
            cursor = conn.cursor()
            args = [user_id, initial_balance, '']
            result_args = cursor.callproc('sp_crear_cuenta', args)
            conn.commit()
            new_account_number = result_args[2]
            return True, "¡Cuenta creada exitosamente!", new_account_number
        except Error as e:
            return False, f"Error desde la base de datos: {e.msg}", None
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    def get_user_accounts(self, user_id):
        conn = DBConnector.get_connection()
        if not conn:
            return None, "Error de conexión."
        try:
            cursor = conn.cursor()
            query = "SELECT id, numero_cuenta, saldo FROM Cuentas WHERE usuario_id = %s AND estado = 'activa'"
            cursor.execute(query, (user_id,))
            accounts = cursor.fetchall()
            return accounts, None
        except Error as e:
            return None, f"Error al obtener cuentas: {e}"
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    def transfer_money(self, source_account_id, dest_account_number, amount, note):
        conn = DBConnector.get_connection()
        if not conn:
            return False, "Error de conexión."
        try:
            cursor = conn.cursor()
            args = (source_account_id, dest_account_number, amount, note)
            cursor.callproc('sp_transferir_dinero', args)
            conn.commit()
            return True, "¡Transferencia realizada con éxito!"
        except Error as e:
            return False, f"Error desde la base de datos: {e.msg}"
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

