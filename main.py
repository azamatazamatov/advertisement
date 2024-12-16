from fastapi import FastAPI
from database import database
from routers import advertisement_router, user_router
from middlewares.user import APIKeyMiddleware

app = FastAPI()

app.include_router(advertisement_router)
app.include_router(user_router)

app.add_middleware(APIKeyMiddleware)
