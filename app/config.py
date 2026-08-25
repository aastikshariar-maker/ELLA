"""Application Configuration"""

from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Application
    APP_NAME: str = "AI Co-Founder Platform"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:8501",  # Streamlit
    ]
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/aicofounder"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_CACHE_TTL: int = 3600
    
    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4"
    OPENAI_TEMPERATURE: float = 0.7
    OPENAI_MAX_TOKENS: int = 2000
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    CELERY_TASK_TIME_LIMIT: int = 3600
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Feature Flags
    ENABLE_MARKET_ANALYSIS: bool = True
    ENABLE_FINANCIAL_MODELING: bool = True
    ENABLE_STRATEGIC_PLANNING: bool = True
    ENABLE_OPERATIONS_OPTIMIZATION: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
