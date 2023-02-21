from lib.response_parser import Response_parser
import bcrypt

class Users:
    def __init__(self, conn):
        self.conn = conn


    def create_user(self, data):

        name = data['name']
        surname = data['surname']
        password = data['password']

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        sql_statement = f"INSERT INTO users (name, surname, password) VALUES ('{name}','{surname}','{hashed_password.decode('utf-8')}')"

        response = self.conn.execute(sql_statement)
        return Response_parser.post_item(response)


    def get_all_users(self):
        
        sql_statement = f"SELECT * FROM users"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def get_one_user(self, user_id):
        
        sql_statement = f"SELECT * FROM users WHERE id = '{user_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def update_one_user(self, user_id, data):
        
        name = data['name']
        surname = data['surname']
        password = data['password']
        
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        sql_statement = f"UPDATE users SET name = '{name}', surname = '{surname}', password = '{hashed_password}' WHERE id = '{user_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.update_item(response)


    def delete_one_user(self, user_id):
        
        sql_statement = f"DELETE FROM users WHERE id = '{user_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.delete_item(response)
