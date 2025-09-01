from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from .service import save_block, get_block
import io

router = APIRouter()

@router.put("/{block_id}")
async def upload_block(block_id: str, file: UploadFile = File(...)):
    data = await file.read()
    result = save_block(block_id, data)
    return result

@router.get("/{block_id}")
def download_block(block_id: str):
    data = get_block(block_id)
    if not data:
        raise HTTPException(status_code=404, detail="Block not found")
    return StreamingResponse(io.BytesIO(data), media_type="application/octet-stream")
