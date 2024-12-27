from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import os
from fastapi.responses import JSONResponse

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get('X-API-Key')
        if api_key is None:
            return JSONResponse(status_code=401, content='Unauthorized')
        elif api_key != os.environ.get("API_KEY"):
            return JSONResponse(status_code=401, content='Unauthorized')
        response = await call_next(request)
        return response 