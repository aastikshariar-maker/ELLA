"""Company Management API Endpoints"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
import uuid

from app.database import get_db
from app.models.company import Company, CompanyStage

router = APIRouter()


class CompanyCreate:
    """Company creation schema"""
    def __init__(self, name: str, industry: str, stage: str = "seed", team_size: int = 1):
        self.name = name
        self.industry = industry
        self.stage = stage
        self.team_size = team_size


class CompanyResponse:
    """Company response schema"""
    def __init__(self, id: str, name: str, industry: str, stage: str, team_size: int):
        self.id = id
        self.name = name
        self.industry = industry
        self.stage = stage
        self.team_size = team_size


@router.post("/", response_model=dict)
async def create_company(
    name: str,
    industry: str,
    stage: str = "seed",
    team_size: int = 1,
    monthly_revenue: float = 0.0,
    monthly_burn: float = 5000.0,
    db: AsyncSession = Depends(get_db)
):
    """Create a new company profile"""
    try:
        company_id = str(uuid.uuid4())
        company = Company(
            id=company_id,
            name=name,
            industry=industry,
            stage=stage,
            team_size=team_size,
            monthly_revenue=monthly_revenue,
            monthly_burn=monthly_burn,
        )
        db.add(company)
        await db.commit()
        await db.refresh(company)
        
        return {
            "success": True,
            "company_id": company_id,
            "name": name,
            "industry": industry,
            "stage": stage,
        }
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{company_id}", response_model=dict)
async def get_company(company_id: str, db: AsyncSession = Depends(get_db)):
    """Get company details"""
    try:
        company = await db.query(Company).filter(Company.id == company_id).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        
        return {
            "id": company.id,
            "name": company.name,
            "industry": company.industry,
            "stage": company.stage,
            "team_size": company.team_size,
            "monthly_revenue": company.monthly_revenue,
            "monthly_burn": company.monthly_burn,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{company_id}", response_model=dict)
async def update_company(
    company_id: str,
    team_size: Optional[int] = None,
    monthly_revenue: Optional[float] = None,
    monthly_burn: Optional[float] = None,
    db: AsyncSession = Depends(get_db) = None,
):
    """Update company profile"""
    try:
        company = await db.query(Company).filter(Company.id == company_id).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        
        if team_size is not None:
            company.team_size = team_size
        if monthly_revenue is not None:
            company.monthly_revenue = monthly_revenue
        if monthly_burn is not None:
            company.monthly_burn = monthly_burn
        
        await db.commit()
        await db.refresh(company)
        
        return {"success": True, "company_id": company.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
