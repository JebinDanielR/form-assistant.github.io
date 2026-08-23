from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://postgres:password@localhost:5432/govform"

    # Qdrant
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_collection: str = "scheme_docs"

    # Ollama
    ollama_base_url: str = "http://localhost:11434"
    vision_model: str = "qwen3-vl:8b"
    chat_model: str = "qwen3:8b"
    embed_model: str = "nomic-embed-text"

    # App
    cors_origins: str = "http://localhost:5173"
    secret_key: str = "change-this-in-production"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()