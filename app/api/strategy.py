"""Strategy API Endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.database import get_db
from app.agents.strategic_agent import StrategicAgent

router = APIRouter()
strategic_agent = StrategicAgent()


@router.post("/generate", response_model=dict)
async def generate_strategy(company_id: str, db: AsyncSession = Depends(get_db)):
    """Generate strategic plan for a company"""
    try:
        # Get company data from DB
        company_data = {
            "company_id": company_id,
            "company_name": "Sample Company",
            "industry": "SaaS",
            "stage": "seed",
            "team_size": 5,
            "target_market": "Enterprise",
            "competitors": ["Competitor1", "Competitor2"],
        }
        
        # Run strategic analysis
        result = await strategic_agent.analyze(company_data)
        
        return {
            "success": True,
            "company_id": company_id,
            "strategy": result,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{company_id}", response_model=dict)
async def get_strategy(company_id: str, db: AsyncSession = Depends(get_db)):
    """Get current strategy for a company"""
    try:
        return {
            "company_id": company_id,
            "strategy": "Strategy data would be retrieved from database",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{company_id}/okrs", response_model=dict)
async def generate_okrs(company_id: str, db: AsyncSession = Depends(get_db)):
    """Generate OKRs for a company"""
    try:
        company_data = {
            "company_id": company_id,
            "company_name": "Sample Company",
        }
        
        result = await strategic_agent.analyze(company_data)
        
        return {
            "success": True,
            "company_id": company_id,
            "okrs": result.get("okrs", {}),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
