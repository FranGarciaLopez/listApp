from fastapi import FastAPI
from main import app, engine
from typing import Dict, Any
from controllers.shows import Shows


@app.post("/shows", description="This endpoint creates a new show in the database", tags=["Shows"]) 
async def add_show_route(data: Dict[str, Any]  = {
                            'name':          [{"en": "The walking dead"}],
                            'desc':          [{"en": "The walking dead series"}],
                            'tipo':          "Zombies",
                            'release_date':  "2010-10-31",
                        }):
    return Shows(engine).create_show(data)


@app.get("/shows", description="This endpoint gets all the shows in the database", tags=["Shows"])
async def get_all_shows_route():
    return await Shows(engine).get_all_shows()


@app.get("/shows/{show_id}", description="This endpoint get one show in the database", tags=["Shows"])
async def get_one_show_route(show_id: str):
    return await Shows(engine).get_one_show(show_id)


@app.put("/shows/{show_id}", description="This endpoint updates one show in the database", tags=["Shows"])
async def get_one_show_route(show_id: str, data: Dict[str, Any]  = {
                            'name':          [{"en": "The last of us"}],
                            'desc':          [{"en": "The last of us series"}],
                            'tipo':          "Zombies",
                            'release_date':  "2023-01-15",
                        }):
    return await Shows(engine).update_one_show(show_id, data)


@app.delete("/shows/{show_id}", description="This endpoint updates one show in the database", tags=["Shows"])
async def get_one_show_route(show_id: str):
    return await Shows(engine).delete_one_show(show_id)