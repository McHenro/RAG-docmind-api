"""
Application settings loaded from the .env file.
pydantic-settings validates every value at startup.
If a required variable is missing, the app fails immediately with a clear error.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    database_url: str       # async URL: postgresql+asyncpg://...
    database_url_sync: str  # sync URL:  postgresql+psycopg2://... (for Alembic)

    # OpenAI
    openai_api_key: str
    embedding_model: str 
    embedding_dimensions: int 

    # LLM — used for answer generation in the query pipeline
    llm_model: str = "gpt-4o-mini"

    # Chunking defaults (can be overridden per request)
    chunk_size: int
    chunk_overlap: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Single shared instance — imported everywhere
settings = Settings()