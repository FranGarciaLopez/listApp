from fastapi import FastAPI
from main import app, engine
from typing import Dict, Any
from controllers.chapters import Chapters

@app.post("/chapters", description="This endpoint creates a new chapter in the database", tags=["Chapters"]) 
async def add_chapter_route(data: Dict[str, Any]  = {
                                'title':        [{"en": "The last of us"}],
                                'desc':         [{"en": "The last of us  chapter 1"}],
                                'release_date': '2023-01-15',
                            }):
    return Chapters(engine).create_chapter(data)


@app.get("/chapters", description="This endpoint gets all the chapters in the database", tags=["Chapters"])
async def get_all_chapters_route():
    return await Chapters(engine).get_all_chapters()


@app.get("/chapters/{chapter_id}", description="This endpoint get one chapter in the database", tags=["Chapters"])
async def get_one_chapter_route(chapter_id: str):
    return await Chapters(engine).get_one_chapter(chapter_id)


@app.put("/chapters/{chapter_id}", description="This endpoint updates one chapter in the database", tags=["Chapters"])
async def get_one_chapter_route(chapter_id: str, data: Dict[str, Any]  = {
                                                    'title':        [{"en": "The last of us"}],
                                                    'desc':         [{"en": "The last of us  chapter 1"}],
                                                    'release_date': '2023-01-15',
                                                }):
    return await Chapters(engine).update_one_chapter(chapter_id, data)


@app.delete("/chapters/{chapter_id}", description="This endpoint deletes one chapter in the database", tags=["Chapters"])
async def get_one_chapter_route(chapter_id: str):
    return await Chapters(engine).delete_one_chapter(chapter_id)