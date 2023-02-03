from lib.response_parser import Response_parser
import json

class Chapters:
    def __init__(self, conn):
        self.conn = conn


    def create_chapter(self, data):

        title = json.dumps(data['title'])
        desc = json.dumps(data['desc'])
        release_date = json.dumps(data['release_date'])

        sql_statement = f"INSERT INTO chapters (title, \"desc\", release_date) VALUES ('{title}','{desc}','{release_date}')"

        response = self.conn.execute(sql_statement)
        return Response_parser.post_item(response)


    def get_all_chapters(self):
        
        sql_statement = f"SELECT * FROM chapters"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def get_one_chapter(self, chapter_id):
        
        sql_statement = f"SELECT * FROM chapters WHERE chapter_id = '{chapter_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.get_items(response)


    def update_one_chapter(self, chapter_id, data):
        
        title = json.dumps(data['title'])
        desc = json.dumps(data['desc'])
        release_date = json.dumps(data['release_date'])

        sql_statement = f"UPDATE chapters SET title = '{title}', \"desc\" = '{desc}', release_date = '{release_date}' WHERE chapter_id = '{chapter_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.update_item(response)


    def delete_one_chapter(self, chapter_id):
        
        sql_statement = f"DELETE FROM chapters WHERE chapter_id = '{chapter_id}'"

        response = self.conn.execute(sql_statement)
        return Response_parser.delete_item(response)
