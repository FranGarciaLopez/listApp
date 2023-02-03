from fastapi import FastAPI
from main import app, engine
from typing import Dict, Any
from controllers.categories import Categories

@app.post("/categories", description="This endpoint creates a new categorie in the database", tags=["Categories"]) 
async def add_categorie_route(data: Dict[str, Any]  = {
                                'name':        [{"en": "Thriller"}],
                                'desc':         [{"en": "Here are thriller series"}],
                            }):
    return Categories(engine).create_categorie(data)


@app.get("/categories", description="This endpoint gets all the categories in the database", tags=["Categories"])
async def get_all_categories_route():
    return await Categories(engine).get_all_categories()


@app.get("/categories/{categorie_id}", description="This endpoint get one categorie in the database", tags=["Categories"])
async def get_one_categorie_route(categorie_id: str):
    return await Categories(engine).get_one_categorie(categorie_id)


@app.put("/categories/{categorie_id}", description="This endpoint updates one categorie in the database", tags=["Categories"])
async def get_one_categorie_route(categorie_id: str, data: Dict[str, Any]  = {
                                                    'name':        [{"en": "Thriller"}],
                                                    'desc':         [{"en": "Here are thriller series"}],
                                                }):
    return await Categories(engine).update_one_categorie(categorie_id, data)


@app.delete("/categories/{categorie_id}", description="This endpoint deletes one categorie in the database", tags=["Categories"])
async def get_one_categorie_route(categorie_id: str):
    return await Categories(engine).delete_one_categorie(categorie_id)