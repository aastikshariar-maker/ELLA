#!/usr/bin/env python
"""Initialize database and create tables"""

import asyncio
import logging
from app.database import init_db
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Initialize the database"""
    logger.info(f"Initializing database: {settings.DATABASE_URL}")
    
    try:
        await init_db()
        logger.info("✓ Database initialized successfully")
    except Exception as e:
        logger.error(f"✗ Failed to initialize database: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
