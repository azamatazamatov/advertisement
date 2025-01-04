from fastapi import FastAPI
from app.v1.middlewares.api_key_validation import APIKeyMiddleware
from app.v1.routers.advertisements import router as advertisements_router
from app.v1.routers.users import router as users_router
from app.v1.database import create_database, close_database

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