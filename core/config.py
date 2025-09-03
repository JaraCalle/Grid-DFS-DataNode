from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_PREFIX: str = "/api/v1"
    DATANODE_ID: str = "dn1"
    DATANODE_HOST: str = "127.0.0.1"
    DATANODE_PORT: int = 9001
    GRPC_PORT: int = 1350
    STORAGE_PATH: str = "./data"
    NAMENODE_URL: str = "http://127.0.0.1:8000/api/v1/namenode"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
