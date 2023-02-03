from lib.response_parser import Response_parser
import json

class Categories:
    def __init__(self, conn):
        self.conn = conn


    def create_categorie(self, data):

        name = json.dumps(data['name'])
        desc = json.dumps(data['desc'])

        sql_statement = f"INSERT INTO categories (name, \"desc\") VALUES ('{name}','{desc}')"

        response = self.conn.execute(sql_statement)
        return Response_parser.post_item(response)


    def get_all_categories(self):
        
        sql_statement = f"SELECT * FROM categories"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def get_one_categorie(self, categorie_id):
        
        sql_statement = f"SELECT * FROM categories WHERE categorie_id = '{categorie_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def update_one_categorie(self, categorie_id, data):
        
        name = json.dumps(data['name'])
        desc = json.dumps(data['desc'])

        sql_statement = f"UPDATE categories SET name = '{name}', \"desc\" = '{desc}' WHERE categorie_id = '{categorie_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.update_item(response)


    def delete_one_categorie(self, categorie_id):
        
        sql_statement = f"DELETE FROM categories WHERE categorie_id = '{categorie_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.delete_item(response)
