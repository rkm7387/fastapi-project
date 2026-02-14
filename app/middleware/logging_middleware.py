import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request, call_next):
        logging.info(f'Request: {request.method} {request.url}')
        response = await call_next(request)
        logging.info(f'Response: {response.status_code}')
        return response
    