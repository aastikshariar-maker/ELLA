"""Strategic Agent - Handles high-level business strategy and planning"""

import logging
from typing import Dict, Any, List
from datetime import datetime

from app.agents.base_agent import BaseAgent
from app.services.llm_service import LLMService

logger = logging.getLogger(__name__)


class StrategicAgent(BaseAgent):
    """Strategic decision-making and planning agent"""
    
    def __init__(self):
        super().__init__(
            name="Strategic Agent",
            description="Handles high-level business strategy, vision, and planning"
        )
        self.llm_service = LLMService()
    
    async def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze company strategy and provide insights"""
        logger.info(f"{self.name} analyzing company strategy")
        
        try:
            company_name = data.get("company_name", "Company")
            industry = data.get("industry", "Unknown")
            current_stage = data.get("stage", "seed")
            team_size = data.get("team_size", 1)
            market_size = data.get("target_market", "Unknown")
            
            strategic_analysis = await self._generate_strategic_analysis(
                company_name, industry, current_stage, team_size, market_size
            )
            
            okrs = await self._generate_okrs(company_name, strategic_analysis)
            
            competitive_position = await self._analyze_competitive_position(
                company_name, industry, data.get("competitors", [])
            )
            
            self.store_memory("last_analysis", strategic_analysis)
            self.store_memory("last_okrs", okrs)
            
            return {
                "agent": self.name,
                "timestamp": datetime.now().isoformat(),
                "strategic_analysis": strategic_analysis,
                "okrs": okrs,
                "competitive_position": competitive_position,
                "recommendations": self._extract_recommendations(strategic_analysis),
            }
        
        except Exception as e:
            logger.error(f"Error in strategic analysis: {e}")
            return {"error": str(e), "agent": self.name}
    
    async def recommend(self, context: Dict[str, Any]) -> List[str]:
        """Generate strategic recommendations"""
        return [
            "Define clear 5-year vision aligned with market opportunities",
            "Establish quarterly OKRs with measurable outcomes",
            "Develop competitive differentiation strategy",
            "Create roadmap with clear milestones and priorities",
            "Establish key performance indicators (KPIs)",
        ]
    
    async def _generate_strategic_analysis(self, company: str, industry: str, stage: str, team_size: int, market: str) -> Dict[str, Any]:
        """Generate comprehensive strategic analysis"""
        prompt = f"Analyze strategy for {company} in {industry} at {stage} stage"
        response = await self.llm_service.get_completion(prompt)
        
        return {
            "vision": "Market leadership through innovation",
            "market_opportunity": "Large and growing market",
            "competitive_advantages": ["Strong team", "Innovative product"],
            "challenges": ["Resource constraints", "Market competition"],
            "growth_levers": ["Product innovation", "Market expansion"],
            "full_analysis": response,
        }
    
    async def _generate_okrs(self, company: str, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate OKRs based on analysis"""
        return {
            "quarterly_okrs": [
                {"objective": "Achieve product-market fit", "key_results": ["100 active users", "40%+ retention"]}
            ],
            "annual_objectives": ["Market leadership", "$1M ARR"],
        }
    
    async def _analyze_competitive_position(self, company: str, industry: str, competitors: List[str]) -> Dict[str, Any]:
        """Analyze competitive positioning"""
        return {
            "positioning": f"{company} is well-positioned in the {industry} market",
            "differentiation": ["Unique value proposition", "Innovation focus"],
            "threats": ["Established competitors", "Market saturation"],
        }
    
    def _extract_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Extract recommendations from analysis"""
        return ["Execute quarterly OKRs", "Validate market assumptions", "Build competitive moat"]
