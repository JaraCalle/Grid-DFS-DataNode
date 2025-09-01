from fastapi import FastAPI
from modules.blocks.routes import router as block_routes
from core.config import settings
from api.routes import api_router


app = FastAPI(title=f"DataNode {settings.DATANODE_ID}")
app.include_router(api_router)

@app.get("/")
def root():
    return {"msg": f"DataNode {settings.DATANODE_ID} is running"}
