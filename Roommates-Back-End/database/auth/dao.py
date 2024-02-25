from pymysql.cursors import DictCursor
from database.dao import BaseDao
from database.auth import queries


class AuthDao(BaseDao):
    def login(self, username, password):
        try:
            with self.connection.cursor(DictCursor) as cursor:
                cursor.execute(queries.CHECK_CREDENCIALS, (username, password))
                user = cursor.fetchone()

                if user:
                    return user
                else:
                    return None
        except Exception as e:
            print(f"Error en la consulta de login: {e}")
            return None
        finally:
            self.close_connection()

    def register(self, user_data):
        with self.connection.cursor(DictCursor) as cur:
            values = [user_data['username'], user_data['mail'],
                      user_data['password']]
            try:
                cur.execute(queries.REGISTER, values)
                self.connection.commit()
            except Exception as e:
                # Manejo de errores
                print(e)
                return e