from fastapi import FastAPI
from main import app, engine
from typing import Dict, Any
from controllers.users import Users


@app.post("/users", description="This endpoint creates a new user in the database")
async def add_user_route(data: Dict[str, Any]  = {'name': 'John', 'surname': 'Doe', 'password': 'test'}):
    return Users(engine).create_user(data)


@app.get("/users", description="This endpoint gets all the users in the database")
async def get_all_users_route():
    return await Users(engine).get_all_users()
