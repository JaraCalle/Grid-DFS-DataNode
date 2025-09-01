from fastapi import APIRouter
from core.config import settings
from modules.blocks.routes import router as block_routes

api_router = APIRouter(prefix=settings.API_V1_PREFIX)
api_router.include_router(block_routes, prefix="/block", tags=["blocks"])