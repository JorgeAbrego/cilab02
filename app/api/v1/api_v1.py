from fastapi import APIRouter
from app.api.v1.endpoints import random
from app.api.v1.endpoints import users

api_router = APIRouter()

api_router.include_router(random.router, prefix="/random")
api_router.include_router(users.router, prefix="/users")
