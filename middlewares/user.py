import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from typing import Callable
from routers.user import SECRET_KEY, ALGORITHM

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get('X-API-Key')
        if api_key is None:
            # If API key is not present in the request header, return 401
            print("API key required")
        response = await call_next(request)
        return response