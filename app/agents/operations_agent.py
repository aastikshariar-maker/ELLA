"""Operations Agent - Handles operational optimization and scaling"""

import logging
from typing import Dict, Any, List
from datetime import datetime

from app.agents.base_agent import BaseAgent
from app.services.llm_service import LLMService

logger = logging.getLogger(__name__)


class OperationsAgent(BaseAgent):
    """Operations optimization and scaling agent"""
    
    def __init__(self):
        super().__init__(
            name="Operations Agent",
            description="Handles operational optimization, scaling strategies, and process management"
        )
        self.llm_service = LLMService()
    
    async def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze operational efficiency and provide optimization recommendations"""
        logger.info(f"{self.name} analyzing operations")
        
        try:
            team_size = data.get("team_size", 1)
            stage = data.get("stage", "seed")
            monthly_burn = data.get("monthly_burn", 5000)
            
            org_structure = self._recommend_org_structure(team_size, stage)
            process_recommendations = self._recommend_processes(stage)
            scaling_strategy = self._develop_scaling_strategy(team_size, stage, monthly_burn)
            kpi_framework = self._define_kpi_framework(stage)
            hiring_roadmap = self._create_hiring_roadmap(stage, team_size)
            
            self.store_memory("org_structure", org_structure)
            self.store_memory("scaling_strategy", scaling_strategy)
            
            return {
                "agent": self.name,
                "timestamp": datetime.now().isoformat(),
                "organizational_structure": org_structure,
                "process_recommendations": process_recommendations,
                "scaling_strategy": scaling_strategy,
                "kpi_framework": kpi_framework,
                "hiring_roadmap": hiring_roadmap,
                "recommendations": self._extract_operational_recommendations(stage, team_size),
            }
        
        except Exception as e:
            logger.error(f"Error in operations analysis: {e}")
            return {"error": str(e), "agent": self.name}
    
    async def recommend(self, context: Dict[str, Any]) -> List[str]:
        """Generate operational recommendations"""
        return [
            "Build lean organizational structure",
            "Establish clear roles and accountability",
            "Implement efficient communication processes",
            "Automate repetitive tasks",
        ]
    
    def _recommend_org_structure(self, team_size: int, stage: str) -> Dict[str, Any]:
        """Recommend organizational structure"""
        if team_size <= 5:
            return {
                "structure_type": "Flat/Functional",
                "key_roles": ["CEO", "CTO", "Head of Sales"],
            }
        else:
            return {
                "structure_type": "Functional with specialization",
                "departments": ["Engineering", "Product", "Sales", "Operations"],
            }
    
    def _recommend_processes(self, stage: str) -> Dict[str, Any]:
        """Recommend processes"""
        return {
            "core_processes": ["Product Development", "Customer Success", "Financial Management"],
            "communication_cadence": {"daily": "Standups", "weekly": "Team syncs", "monthly": "All-hands"},
        }
    
    def _develop_scaling_strategy(self, team_size: int, stage: str, monthly_burn: float) -> Dict[str, Any]:
        """Develop scaling strategy"""
        return {
            "phase_1": {"timeline": "Months 1-3", "focus": "Validate product-market fit"},
            "phase_2": {"timeline": "Months 4-9", "focus": "Scale revenue and team"},
            "phase_3": {"timeline": "Months 10+", "focus": "Achieve scale and efficiency"},
        }
    
    def _define_kpi_framework(self, stage: str) -> Dict[str, List[str]]:
        """Define KPI framework"""
        return {
            "product_metrics": ["DAU", "MAU", "Retention Rate", "NPS"],
            "business_metrics": ["MRR", "ARR", "CAC", "LTV", "Churn Rate"],
            "operational_metrics": ["Team Productivity", "Time to Hire", "Cost per Employee"],
        }
    
    def _create_hiring_roadmap(self, stage: str, team_size: int) -> List[Dict[str, Any]]:
        """Create hiring roadmap"""
        return [
            {"priority": 1, "role": "VP Sales", "timeline": "Q1-Q2"},
            {"priority": 2, "role": "Senior Engineer", "timeline": "Q1-Q2"},
            {"priority": 3, "role": "Head of Product", "timeline": "Q2-Q3"},
        ]
    
    def _extract_operational_recommendations(self, stage: str, team_size: int) -> List[str]:
        """Extract operational recommendations"""
        return [
            "Establish clear communication channels",
            "Create process documentation",
            "Implement project management tools",
            "Build metrics dashboard",
        ]
