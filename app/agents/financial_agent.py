"""Financial Agent - Handles financial modeling and analysis"""

import logging
from typing import Dict, Any, List
from datetime import datetime

from app.agents.base_agent import BaseAgent
from app.services.llm_service import LLMService

logger = logging.getLogger(__name__)


class FinancialAgent(BaseAgent):
    """Financial modeling and forecasting agent"""
    
    def __init__(self):
        super().__init__(
            name="Financial Agent",
            description="Handles financial modeling, projections, and fundraising strategy"
        )
        self.llm_service = LLMService()
    
    async def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze financial situation and provide forecasts"""
        logger.info(f"{self.name} analyzing financials")
        
        try:
            monthly_revenue = data.get("monthly_revenue", 0)
            monthly_burn = data.get("monthly_burn", 5000)
            runway_months = data.get("runway_months")
            team_size = data.get("team_size", 1)
            funding_stage = data.get("stage", "seed")
            
            if runway_months is None:
                total_funds = data.get("total_funding", 50000)
                runway_months = self._calculate_runway(total_funds, monthly_burn, monthly_revenue)
            
            forecasts = self._generate_forecasts(
                monthly_revenue, monthly_burn, runway_months, team_size
            )
            
            burn_analysis = self._analyze_burn_rate(monthly_revenue, monthly_burn, runway_months)
            
            fundraising_strategy = self._generate_fundraising_strategy(
                funding_stage, monthly_burn, runway_months, team_size
            )
            
            self.store_memory("last_forecasts", forecasts)
            self.store_memory("burn_analysis", burn_analysis)
            
            return {
                "agent": self.name,
                "timestamp": datetime.now().isoformat(),
                "current_metrics": {
                    "monthly_revenue": monthly_revenue,
                    "monthly_burn": monthly_burn,
                    "runway_months": runway_months,
                },
                "forecasts": forecasts,
                "burn_analysis": burn_analysis,
                "fundraising_strategy": fundraising_strategy,
                "recommendations": self._extract_financial_recommendations(burn_analysis, runway_months),
            }
        
        except Exception as e:
            logger.error(f"Error in financial analysis: {e}")
            return {"error": str(e), "agent": self.name}
    
    async def recommend(self, context: Dict[str, Any]) -> List[str]:
        """Generate financial recommendations"""
        return [
            "Implement strict budget discipline",
            "Focus on revenue generation",
            "Track unit economics closely",
            "Build financial forecasting processes",
        ]
    
    def _calculate_runway(self, total_funds: float, monthly_burn: float, monthly_revenue: float = 0) -> float:
        """Calculate runway in months"""
        net_burn = monthly_burn - monthly_revenue
        if net_burn <= 0:
            return float('inf')
        return total_funds / net_burn
    
    def _generate_forecasts(self, revenue: float, burn: float, runway: float, team_size: int) -> Dict[str, Any]:
        """Generate 24-month financial forecasts"""
        return {
            "24_month_revenue": revenue * 12 * 2.5,
            "24_month_burn": burn * 12 * 2,
            "breakeven_month": 18 if revenue > 0 else 24,
        }
    
    def _analyze_burn_rate(self, revenue: float, burn: float, runway: float) -> Dict[str, Any]:
        """Analyze burn rate and cash efficiency"""
        net_burn = burn - revenue
        
        if runway > 24:
            health = "Healthy"
        elif runway > 12:
            health = "Caution"
        elif runway > 6:
            health = "Critical"
        else:
            health = "Urgent"
        
        return {
            "monthly_burn": burn,
            "monthly_revenue": revenue,
            "net_monthly_burn": net_burn,
            "runway_months": runway,
            "health_status": health,
        }
    
    def _generate_fundraising_strategy(self, stage: str, monthly_burn: float, runway: float, team_size: int) -> Dict[str, Any]:
        """Generate fundraising strategy"""
        return {
            "recommended_round": "Series A" if stage == "seed" else "Series B",
            "target_raise": monthly_burn * 12,
            "timeline": "Next 3-6 months",
            "investor_types": ["VCs", "Angel investors"],
        }
    
    def _extract_financial_recommendations(self, burn_analysis: Dict[str, Any], runway: float) -> List[str]:
        """Extract financial recommendations"""
        recommendations = []
        
        if runway < 6:
            recommendations.append("URGENT: Secure funding immediately")
        elif runway < 12:
            recommendations.append("Begin fundraising process")
        
        recommendations.extend([
            "Build detailed financial forecasts",
            "Establish monthly financial reviews",
        ])
        
        return recommendations
