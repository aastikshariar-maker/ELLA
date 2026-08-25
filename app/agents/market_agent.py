"""Market Agent - Handles market research and competitive analysis"""

import logging
from typing import Dict, Any, List
from datetime import datetime

from app.agents.base_agent import BaseAgent
from app.services.llm_service import LLMService

logger = logging.getLogger(__name__)


class MarketAgent(BaseAgent):
    """Market research and competitive analysis agent"""
    
    def __init__(self):
        super().__init__(
            name="Market Agent",
            description="Handles market research, competitor analysis, and market sizing"
        )
        self.llm_service = LLMService()
    
    async def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze market opportunity and competitive landscape"""
        logger.info(f"{self.name} analyzing market")
        
        try:
            industry = data.get("industry", "Unknown")
            target_market = data.get("target_market", "Unknown")
            company_name = data.get("company_name", "Company")
            
            market_sizing = self._calculate_market_sizing(industry, target_market)
            competitors_analysis = self._analyze_competitors(industry, data.get("competitors", []))
            customer_segments = self._identify_customer_segments(target_market)
            market_trends = self._identify_market_trends(industry)
            pricing_strategy = self._develop_pricing_strategy(industry, market_sizing)
            
            self.store_memory("market_sizing", market_sizing)
            self.store_memory("competitor_analysis", competitors_analysis)
            
            return {
                "agent": self.name,
                "timestamp": datetime.now().isoformat(),
                "market_sizing": market_sizing,
                "competitive_analysis": competitors_analysis,
                "customer_segments": customer_segments,
                "market_trends": market_trends,
                "pricing_strategy": pricing_strategy,
                "recommendations": self._extract_market_recommendations(market_sizing),
            }
        
        except Exception as e:
            logger.error(f"Error in market analysis: {e}")
            return {"error": str(e), "agent": self.name}
    
    async def recommend(self, context: Dict[str, Any]) -> List[str]:
        """Generate market recommendations"""
        return [
            "Conduct customer interviews to validate assumptions",
            "Develop detailed buyer personas",
            "Create competitive differentiation strategy",
            "Establish go-to-market strategy",
        ]
    
    def _calculate_market_sizing(self, industry: str, target_market: str) -> Dict[str, Any]:
        """Calculate TAM/SAM/SOM"""
        tam = 500_000_000_000
        sam = tam * 0.5
        som = sam * 0.01
        
        return {
            "tam": f"${tam:,.0f}",
            "sam": f"${sam:,.0f}",
            "som": f"${som:,.0f}",
            "market_growth_rate": "15-25% YoY",
        }
    
    def _analyze_competitors(self, industry: str, competitors: List[str]) -> Dict[str, Any]:
        """Analyze competitive landscape"""
        return {
            "total_competitors": len(competitors),
            "market_concentration": "Fragmented" if len(competitors) > 5 else "Concentrated",
            "competition_intensity": "Moderate to High",
        }
    
    def _identify_customer_segments(self, target_market: str) -> List[Dict[str, Any]]:
        """Identify customer segments"""
        return [
            {"segment": "Enterprise", "size": "10% of TAM", "willingness_to_pay": "High"},
            {"segment": "Mid-Market", "size": "35% of TAM", "willingness_to_pay": "Medium-High"},
            {"segment": "SMB", "size": "55% of TAM", "willingness_to_pay": "Low-Medium"},
        ]
    
    def _identify_market_trends(self, industry: str) -> Dict[str, Any]:
        """Identify market trends"""
        return {
            "macro_trends": [
                "Digital transformation acceleration",
                "Remote work adoption",
                "AI and automation",
            ],
        }
    
    def _develop_pricing_strategy(self, industry: str, market_sizing: Dict[str, Any]) -> Dict[str, Any]:
        """Develop pricing strategy"""
        return {
            "pricing_model": "SaaS/Subscription",
            "tiers": ["Starter ($29-49/mo)", "Professional ($99-199/mo)", "Enterprise (Custom)"],
        }
    
    def _extract_market_recommendations(self, market_sizing: Dict[str, Any]) -> List[str]:
        """Extract market recommendations"""
        return [
            "Focus on highest-value segments first",
            "Develop strong value proposition",
            "Build brand awareness",
        ]
