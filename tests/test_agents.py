"""Test suite for agents"""

import pytest
import asyncio
from app.agents.strategic_agent import StrategicAgent
from app.agents.financial_agent import FinancialAgent
from app.agents.market_agent import MarketAgent
from app.agents.operations_agent import OperationsAgent


@pytest.fixture
def strategic_agent():
    return StrategicAgent()


@pytest.fixture
def financial_agent():
    return FinancialAgent()


@pytest.fixture
def market_agent():
    return MarketAgent()


@pytest.fixture
def operations_agent():
    return OperationsAgent()


@pytest.mark.asyncio
async def test_strategic_agent_analysis(strategic_agent):
    """Test strategic agent analysis"""
    data = {
        "company_name": "TestCo",
        "industry": "SaaS",
        "stage": "seed",
        "team_size": 5,
        "target_market": "Enterprise",
    }
    
    result = await strategic_agent.analyze(data)
    
    assert result["agent"] == "Strategic Agent"
    assert "strategic_analysis" in result
    assert "okrs" in result
    assert "recommendations" in result


@pytest.mark.asyncio
async def test_financial_agent_analysis(financial_agent):
    """Test financial agent analysis"""
    data = {
        "monthly_revenue": 5000,
        "monthly_burn": 25000,
        "total_funding": 250000,
        "team_size": 5,
        "stage": "seed",
    }
    
    result = await financial_agent.analyze(data)
    
    assert result["agent"] == "Financial Agent"
    assert "current_metrics" in result
    assert "forecasts" in result
    assert "burn_analysis" in result
    assert "fundraising_strategy" in result


@pytest.mark.asyncio
async def test_market_agent_analysis(market_agent):
    """Test market agent analysis"""
    data = {
        "company_name": "TestCo",
        "industry": "SaaS",
        "target_market": "Enterprise",
        "competitors": ["Comp1", "Comp2"],
    }
    
    result = await market_agent.analyze(data)
    
    assert result["agent"] == "Market Agent"
    assert "market_sizing" in result
    assert "competitive_analysis" in result
    assert "customer_segments" in result


@pytest.mark.asyncio
async def test_operations_agent_analysis(operations_agent):
    """Test operations agent analysis"""
    data = {
        "team_size": 5,
        "stage": "seed",
        "monthly_burn": 25000,
    }
    
    result = await operations_agent.analyze(data)
    
    assert result["agent"] == "Operations Agent"
    assert "organizational_structure" in result
    assert "scaling_strategy" in result
    assert "kpi_framework" in result


@pytest.mark.asyncio
async def test_agent_memory(strategic_agent):
    """Test agent memory storage and retrieval"""
    strategic_agent.store_memory("test_key", "test_value")
    
    result = strategic_agent.retrieve_memory("test_key")
    assert result == "test_value"


@pytest.mark.asyncio
async def test_agent_recommendations(strategic_agent):
    """Test agent recommendations"""
    context = {}
    recommendations = await strategic_agent.recommend(context)
    
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0
    assert all(isinstance(r, str) for r in recommendations)
