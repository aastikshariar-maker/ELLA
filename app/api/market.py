"""Market Analysis API Endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.agents.market_agent import MarketAgent

router = APIRouter()
market_agent = MarketAgent()


@router.post("/analyze", response_model=dict)
async def analyze_market(company_id: str, db: AsyncSession = Depends(get_db)):
    """Analyze market for a company"""
    try:
        market_data = {
            "company_id": company_id,
            "company_name": "Sample Company",
            "industry": "SaaS",
            "target_market": "Enterprise",
            "competitors": ["Competitor1", "Competitor2"],
        }
        
        result = await market_agent.analyze(market_data)
        
        return {
            "success": True,
            "company_id": company_id,
            "analysis": result,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tam-sam-som/{company_id}", response_model=dict)
async def get_market_sizing(company_id: str, db: AsyncSession = Depends(get_db)):
    """Get TAM/SAM/SOM for a company"""
    try:
        return {
            "company_id": company_id,
            "tam": "$500B",
            "sam": "$250B",
            "som": "$2.5B",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/competitors/{company_id}", response_model=dict)
async def analyze_competitors(company_id: str, db: AsyncSession = Depends(get_db)):
    """Get competitive analysis for a company"""
    try:
        return {
            "company_id": company_id,
            "competitors": [
                {"name": "Competitor1", "market_position": "Leader"},
                {"name": "Competitor2", "market_position": "Challenger"},
            ],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
