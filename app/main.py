from fastapi import FastAPI
from app.middlewares import APIKeyMiddleware

app = FastAPI()

app.add_middleware(APIKeyMiddleware)