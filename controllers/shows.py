from lib.response_parser import Response_parser
import json

class Shows:
    def __init__(self, conn):
        self.conn = conn


    def create_show(self, data):

        name = json.dumps(data['name'])
        desc = json.dumps(data['desc'])
        tipo = json.dumps(data['tipo'])
        release_date = json.dumps(data['release_date'])

        sql_statement = f"INSERT INTO shows (name, \"desc\", tipo, release_date) VALUES ('{name}','{desc}','{tipo}','{release_date}')"

        response = self.conn.execute(sql_statement)
        return Response_parser.post_item(response)


    def get_all_shows(self):
        
        sql_statement = f"SELECT * FROM shows"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def get_one_show(self, show_id):
        
        sql_statement = f"SELECT * FROM shows WHERE show_id = '{show_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def update_one_show(self, show_id, data):
        
        name = json.dumps(data['name'])
        desc = json.dumps(data['desc'])
        tipo = json.dumps(data['tipo'])
        release_date = json.dumps(data['release_date'])

        sql_statement = f"UPDATE shows SET name = '{name}', \"desc\" = '{desc}', tipo = '{tipo}', release_date = '{release_date}' WHERE show_id = '{show_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.update_item(response)


    def delete_one_show(self, show_id):
        
        sql_statement = f"DELETE FROM shows WHERE show_id = '{show_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.delete_item(response)
