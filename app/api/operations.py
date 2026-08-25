"""Operations API Endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.agents.operations_agent import OperationsAgent

router = APIRouter()
operations_agent = OperationsAgent()


@router.post("/analyze", response_model=dict)
async def analyze_operations(company_id: str, db: AsyncSession = Depends(get_db)):
    """Analyze operations for a company"""
    try:
        ops_data = {
            "company_id": company_id,
            "team_size": 5,
            "stage": "seed",
            "monthly_burn": 25000,
        }
        
        result = await operations_agent.analyze(ops_data)
        
        return {
            "success": True,
            "company_id": company_id,
            "analysis": result,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/org-structure/{company_id}", response_model=dict)
async def get_org_structure(company_id: str, db: AsyncSession = Depends(get_db)):
    """Get recommended organizational structure"""
    try:
        return {
            "company_id": company_id,
            "structure_type": "Flat/Functional",
            "departments": ["Engineering", "Sales", "Operations"],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/scaling-roadmap/{company_id}", response_model=dict)
async def get_scaling_roadmap(company_id: str, db: AsyncSession = Depends(get_db)):
    """Get scaling roadmap for a company"""
    try:
        return {
            "company_id": company_id,
            "phase_1": {"timeline": "Months 1-3", "focus": "Validate PMF"},
            "phase_2": {"timeline": "Months 4-9", "focus": "Scale revenue and team"},
            "phase_3": {"timeline": "Months 10+", "focus": "Achieve scale"},
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
