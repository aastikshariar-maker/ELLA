"""Financial API Endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.agents.financial_agent import FinancialAgent

router = APIRouter()
financial_agent = FinancialAgent()


@router.post("/analyze", response_model=dict)
async def analyze_financials(company_id: str, db: AsyncSession = Depends(get_db)):
    """Analyze company financials"""
    try:
        financial_data = {
            "company_id": company_id,
            "monthly_revenue": 5000,
            "monthly_burn": 25000,
            "total_funding": 250000,
            "team_size": 5,
            "stage": "seed",
        }
        
        result = await financial_agent.analyze(financial_data)
        
        return {
            "success": True,
            "company_id": company_id,
            "analysis": result,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/forecast/{company_id}", response_model=dict)
async def get_forecast(company_id: str, months: int = 24, db: AsyncSession = Depends(get_db)):
    """Get financial forecast for a company"""
    try:
        return {
            "company_id": company_id,
            "months": months,
            "forecast": {
                "24_month_revenue": 500000,
                "24_month_burn": 600000,
                "breakeven_month": 18,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/runway/{company_id}", response_model=dict)
async def get_runway(company_id: str, db: AsyncSession = Depends(get_db)):
    """Get runway calculation for a company"""
    try:
        return {
            "company_id": company_id,
            "runway_months": 10,
            "health_status": "Caution",
            "recommendation": "Begin fundraising process",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
