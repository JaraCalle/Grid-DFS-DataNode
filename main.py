import threading
import uvicorn
from fastapi import FastAPI
from core.config import settings
from api.routes import api_router
from modules.grpc.server import serve_grpc

app = FastAPI(title=f"DataNode {settings.DATANODE_ID}")
app.include_router(api_router)

@app.get("/")
def root():
    return {"msg": f"DataNode {settings.DATANODE_ID} REST API is running"}

def start_rest():
    uvicorn.run("main:app", host=settings.DATANODE_HOST, port=settings.REST_PORT, reload=False)

def start_grpc():
    serve_grpc()

if __name__ == "__main__":
    t1 = threading.Thread(target=start_rest, daemon=True)
    t2 = threading.Thread(target=start_grpc, daemon=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()