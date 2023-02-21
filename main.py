from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://oqwtqlla:mpMVxj0eFbGdlNobU9tZvtGItafo9fho@dumbo.db.elephantsql.com/oqwtqlla"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

app = FastAPI()

from routes.routes import *

if __name__ == "__main__":
    app.run()