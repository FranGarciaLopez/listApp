from lib.response_parser import Response_parser

class Users:
    def __init__(self, conn):
        self.conn = conn


    def create_user(self, data):

        name = data['name']
        surname = data['surname']
        password = data['password']

        sql_statement = f"INSERT INTO users (name, surname, password) VALUES ('{name}','{surname}','{password}')"

        response = self.conn.execute(sql_statement)
        return Response_parser.post_item(response)


    def get_all_users(self):
        
        sql_statement = f"SELECT * FROM users"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)
