from fastapi import FastAPI
from src.utils.db import Base, engine
from src.user.models import UserModel  # needed so Base knows the table
from src.user.router import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_routes)