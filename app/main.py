"""FastAPI Application Entry Point"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.database import init_db

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management"""
    # Startup
    logger.info("Starting AI Co-Founder Platform...")
    await init_db()
    
    yield
    
    # Shutdown
    logger.info("Shutting down AI Co-Founder Platform...")


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    app = FastAPI(
        title=settings.APP_NAME,
        description="AI-powered Co-Founder Platform for Strategic Business Management",
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Health check endpoint
    @app.get("/health")
    async def health_check():
        """Health check endpoint"""
        return {
            "status": "healthy",
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
        }
    
    # API Routes
    @app.get("/")
    async def root():
        """Root endpoint"""
        return {
            "message": "Welcome to AI Co-Founder Platform",
            "docs": "/docs",
            "health": "/health",
        }
    
    # TODO: Import and include routers
    # from app.api import companies, strategy, financial, market, operations
    # app.include_router(companies.router, prefix="/api/companies", tags=["companies"])
    # app.include_router(strategy.router, prefix="/api/strategy", tags=["strategy"])
    # app.include_router(financial.router, prefix="/api/financial", tags=["financial"])
    # app.include_router(market.router, prefix="/api/market", tags=["market"])
    # app.include_router(operations.router, prefix="/api/operations", tags=["operations"])
    
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
    )
