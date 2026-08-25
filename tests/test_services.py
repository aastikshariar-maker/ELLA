"""Test suite for services"""

import pytest
from app.services.llm_service import LLMService


@pytest.fixture
def llm_service():
    return LLMService()


@pytest.mark.asyncio
async def test_llm_completion(llm_service):
    """Test LLM completion"""
    prompt = "What is the best strategy for a startup?"
    
    response = await llm_service.get_completion(prompt)
    
    assert isinstance(response, str)
    assert len(response) > 0


@pytest.mark.asyncio
async def test_llm_placeholder_responses(llm_service):
    """Test placeholder responses for different prompts"""
    
    # Test strategic prompt
    response = await llm_service.get_completion("strategic analysis")
    assert "strategic" in response.lower() or len(response) > 0
    
    # Test OKR prompt
    response = await llm_service.get_completion("okr generation")
    assert len(response) > 0
    
    # Test forecast prompt
    response = await llm_service.get_completion("financial forecast")
    assert len(response) > 0
