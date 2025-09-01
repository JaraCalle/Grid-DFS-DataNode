import requests
from core.config import settings

def register_to_namenode():
    url = f"{settings.NAMENODE_URL}/register_datanode"
    payload = {
        "id": settings.DATANODE_ID,
        "ip": settings.DATANODE_HOST,
        "port": settings.DATANODE_PORT,
        "capacity": 1000
    }
    try:
        resp = requests.post(url, json=payload, headers={"Authorization": "Bearer <TOKEN_ADMIN>"})
        print("Register response:", resp.json())
    except Exception as e:
        print("Error registering DataNode:", e)
