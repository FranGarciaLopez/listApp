from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from fastapi.staticfiles import StaticFiles
import os

DB_USER = os.getenv("oqwtqlla")
DB_PASSWORD = os.getenv("mpMVxj0eFbGdlNobU9tZvtGItafo9fho")
DB_HOST = os.getenv("dumbo.db.elephantsql.com")
DB_NAME = os.getenv("oqwtqlla")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
cwd = os.getcwd()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

app = FastAPI()
BASE_PATH = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=os.path.join(cwd, "static")), name="static")
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

from routes.routes import *


@app.get("/", status_code=200)
async def read_root(request: Request):
    """
    Root GET
    """
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request},
    )

if __name__ == "__main__":
    app.run()