from fastapi import FastAPI
from app.middlewares.v1.api_key_validation import APIKeyMiddleware
from app.routers.v1.advertisements import router as advertisements_router
from app.routers.v1.users import router as users_router
from app.database import create_database, close_database

app = FastAPI()

app.include_router(advertisements_router, prefix="/api/v1/advertisement", tags=["Advertisement"])
app.include_router(users_router)

app.add_middleware(APIKeyMiddleware)

@app.on_event("startup")
async def startup():
    await create_database(app)

@app.on_event("shutdown")
async def shutdown():
    await close_database(app)