from fastapi import APIRouter


from . import Bridge

routers = APIRouter()

routers.include_router(Bridge.routes)
