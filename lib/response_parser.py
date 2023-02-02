from fastapi import Response, HTTPException

class Response_parser:

    def post_item(sql_response):
        if sql_response == None:
            raise HTTPException(status_code=500, detail="Not created")
        return {"status_code": 201, "message": "Created"}
    

    async def get_items(sql_response):
        if sql_response == None:
            return  HTTPException(status_code=404, detail="The data does not exists")

        sql_response = [
            {column:value for column, value in row._mapping.items()}
            for row in sql_response]
        return {'status_code': 200, 'data': sql_response}


    async def update_item(sql_response):
        return {"Message": "Updated"}, 200


    async def delete_item(sql_response):
        if sql_response == None:
            raise HTTPException(status_code=500, detail="No response")
        return {"status_code": 200, "message": "Deleted"}
        
