import contextvars
from fastapi import FastAPI, Request

global_request = contextvars.ContextVar('global_request')

def add_global_request_middleware(app: FastAPI):
    @app.middleware('http')
    async def global_request_middleware(request: Request, call_next):
        global_request.set(request)
        response = await call_next(request)
        return response
    
    return global_request_middleware