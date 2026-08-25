"""Company Data Model"""

from sqlalchemy import Column, String, Integer, Float, DateTime, Text, Enum
from sqlalchemy.sql import func
from datetime import datetime
import enum

from app.database import Base


class CompanyStage(str, enum.Enum):
    """Company development stages"""
    IDEA = "idea"
    PRE_SEED = "pre-seed"
    SEED = "seed"
    SERIES_A = "series-a"
    SERIES_B = "series-b"
    SERIES_C = "series-c"
    GROWTH = "growth"
    PROFITABILITY = "profitability"


class Company(Base):
    """Company Profile Model"""
    
    __tablename__ = "companies"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    industry = Column(String(100), nullable=False)
    stage = Column(Enum(CompanyStage), default=CompanyStage.SEED, nullable=False)
    
    # Team
    team_size = Column(Integer, default=1, nullable=False)
    founders = Column(String(500), nullable=True)  # JSON string
    
    # Financials
    monthly_revenue = Column(Float, default=0.0, nullable=False)
    monthly_burn = Column(Float, default=0.0, nullable=False)
    runway_months = Column(Float, nullable=True)
    total_funding = Column(Float, default=0.0, nullable=False)
    
    # Product
    product_description = Column(Text, nullable=True)
    target_market = Column(String(500), nullable=True)
    key_features = Column(String(1000), nullable=True)  # JSON string
    
    # Metadata
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    def __repr__(self):
        return f"<Company(id={self.id}, name={self.name}, stage={self.stage})>"
