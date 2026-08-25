#!/usr/bin/env python
"""Seed database with sample data"""

import asyncio
import logging
from datetime import datetime
import uuid

from app.database import AsyncSessionLocal, Base, engine
from app.models.company import Company, CompanyStage
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SAMPLE_COMPANIES = [
    {
        "name": "TechStartup AI",
        "industry": "SaaS",
        "stage": "seed",
        "team_size": 5,
        "monthly_revenue": 5000,
        "monthly_burn": 25000,
        "description": "AI-powered business intelligence platform",
    },
    {
        "name": "CloudSync",
        "industry": "Infrastructure",
        "stage": "series-a",
        "team_size": 15,
        "monthly_revenue": 50000,
        "monthly_burn": 75000,
        "description": "Real-time cloud synchronization service",
    },
    {
        "name": "DataViz Pro",
        "industry": "Analytics",
        "stage": "seed",
        "team_size": 3,
        "monthly_revenue": 2000,
        "monthly_burn": 15000,
        "description": "Beautiful data visualization platform",
    },
]


async def seed_database():
    """Seed database with sample companies"""
    logger.info("Starting database seeding...")
    
    async with AsyncSessionLocal() as session:
        try:
            for company_data in SAMPLE_COMPANIES:
                company = Company(
                    id=str(uuid.uuid4()),
                    **company_data,
                )
                session.add(company)
                logger.info(f"Added company: {company_data['name']}")
            
            await session.commit()
            logger.info("✓ Database seeded successfully")
        
        except Exception as e:
            await session.rollback()
            logger.error(f"✗ Failed to seed database: {e}")
            raise


async def main():
    """Main seeding function"""
    logger.info(f"Database URL: {settings.DATABASE_URL}")
    
    # Create tables first
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Seed data
    await seed_database()


if __name__ == "__main__":
    asyncio.run(main())
