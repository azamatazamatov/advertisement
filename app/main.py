from fastapi import FastAPI
from app.middlewares import APIKeyMiddleware
from app.routers import advertisements_router, users_router
from app.database import create_database, close_database

app = FastAPI()

app.include_router(advertisements_router)
app.include_router(users_router)

# app.add_middleware(APIKeyMiddleware)

@app.on_event("startup")
async def startup():
    await create_database(app)

@app.on_event("shutdown")
async def shutdown():
    await close_database(app)