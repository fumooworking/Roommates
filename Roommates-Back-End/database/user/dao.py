from pymysql.cursors import DictCursor

from database.dao import BaseDao
from database.user import queries


class UserDao(BaseDao):

    #                             USER BASIC

    def get_all_users(self):
        with self.connection.cursor(DictCursor) as cur:
            cur.execute(queries.GET_USER)
            self.connection.commit()
            return cur.fetchall()

    def delete_user_by_id(self, user_id):
        with self.connection.cursor(DictCursor) as cur:
            cur.execute(queries.DELETE_USER_BY_ID, (user_id,))
            self.connection.commit()

    def patch_user_by_id(self, data):
        id_user = data.get('id', None)
        username = data.get('username', None)
        mail = data.get('mail', None)
        password = data.get('password', None)

        with self.connection.cursor(DictCursor) as cur:
            cur.execute(queries.PATCH_USER_BY_ID, (username, mail, password, id_user))
            self.connection.commit()

    def get_user_by_id(self, user_id):
        with self.connection.cursor(DictCursor) as cur:
            cur.execute(queries.GET_USER_BY_ID, (user_id,))
            return cur.fetchall()

    def get_user_by_username(self, username):
        with self.connection.cursor(DictCursor) as cur:
            cur.execute(queries.GET_USER_BY_USERNAME, (username,))
            return cur.fetchall()

