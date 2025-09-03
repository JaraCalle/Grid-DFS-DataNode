from fastapi import APIRouter
from core.config import settings

api_router = APIRouter(prefix=settings.API_V1_PREFIX)