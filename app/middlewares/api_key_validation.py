from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import os


class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get('X-API-Key')
        if api_key is None:
            raise HTTPException(status_code=401, detail='Unauthorized')
        elif api_key != os.environ.get("API_KEY"):
            raise HTTPException(status_code=401, detail='Unauthorized')
        response = await call_next(request)
        return response