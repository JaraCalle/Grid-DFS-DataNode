import os
from core.config import settings

os.makedirs(settings.STORAGE_PATH, exist_ok=True)

def save_block(block_id: str, data: bytes):
    file_path = os.path.join(settings.STORAGE_PATH, block_id)
    with open(file_path, "wb") as f:
        f.write(data)
    return {"msg": f"Block {block_id} saved at {file_path}"}

def get_block(block_id: str) -> bytes | None:
    file_path = os.path.join(settings.STORAGE_PATH, block_id)
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        return f.read()
