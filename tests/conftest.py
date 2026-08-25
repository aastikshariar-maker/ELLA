"""Pytest configuration and fixtures"""

import pytest
import asyncio
from typing import Generator


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def sample_company_data():
    """Sample company data for testing"""
    return {
        "company_name": "TestStartup",
        "industry": "SaaS",
        "stage": "seed",
        "team_size": 5,
        "monthly_revenue": 5000,
        "monthly_burn": 25000,
        "total_funding": 250000,
        "target_market": "Enterprise",
        "competitors": ["Competitor1", "Competitor2"],
    }


@pytest.fixture
def sample_financial_data():
    """Sample financial data for testing"""
    return {
        "monthly_revenue": 5000,
        "monthly_burn": 25000,
        "total_funding": 250000,
        "runway_months": 10,
        "team_size": 5,
        "stage": "seed",
    }
