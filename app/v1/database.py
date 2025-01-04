from pymongo import MongoClient
from fastapi import Request

MONGO_URL = "mongodb://root:example@localhost:27017"

async def create_database(app):
    app.state.mongodb_client = MongoClient(MONGO_URL)
    app.state.database = app.state.mongodb_client["advertisement"]

async def close_database(app):
    app.state.mongodb_client.close()

async def get_database(request: Request):
    return request.app.state.database