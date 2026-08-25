#!/usr/bin/env python
"""Generate comprehensive company report"""

import asyncio
import json
from datetime import datetime
from typing import Dict, Any

from app.agents.coordinator import AgentCoordinator
from app.agents.strategic_agent import StrategicAgent
from app.agents.financial_agent import FinancialAgent
from app.agents.market_agent import MarketAgent
from app.agents.operations_agent import OperationsAgent


class ReportGenerator:
    """Generate comprehensive AI Co-Founder reports"""
    
    def __init__(self):
        self.coordinator = AgentCoordinator()
        self.setup_agents()
    
    def setup_agents(self):
        """Register all agents with coordinator"""
        self.coordinator.register_agent("strategic", StrategicAgent())
        self.coordinator.register_agent("financial", FinancialAgent())
        self.coordinator.register_agent("market", MarketAgent())
        self.coordinator.register_agent("operations", OperationsAgent())
    
    async def generate_report(self, company_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive report for company"""
        print(f"\n{'='*60}")
        print(f"Generating AI Co-Founder Report for {company_data.get('company_name', 'Company')}")
        print(f"{'='*60}\n")
        
        # Run orchestration
        result = await self.coordinator.orchestrate("comprehensive_analysis", company_data)
        
        # Format report
        report = {
            "timestamp": datetime.now().isoformat(),
            "company": company_data.get("company_name"),
            "executive_summary": self._generate_executive_summary(result),
            "analyses": result,
            "recommendations": self._synthesize_recommendations(result),
        }
        
        return report
    
    def _generate_executive_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate executive summary"""
        return """
AI Co-Founder Analysis Summary:

This comprehensive analysis evaluates your company across four key dimensions:
1. Strategic positioning and growth opportunities
2. Financial health and runway
3. Market opportunity and competitive landscape
4. Operational efficiency and scaling

The recommendations below are prioritized by impact and urgency.
        """
    
    def _synthesize_recommendations(self, analysis: Dict[str, Any]) -> list:
        """Synthesize recommendations from all agents"""
        recommendations = []
        
        if "individual_results" in analysis:
            for agent_name, result in analysis["individual_results"].items():
                if "recommendations" in result:
                    recommendations.extend(result["recommendations"])
        
        return recommendations
    
    def save_report(self, report: Dict[str, Any], filename: str = None) -> str:
        """Save report to file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            company_name = report.get("company", "company").replace(" ", "_")
            filename = f"report_{company_name}_{timestamp}.json"
        
        with open(filename, "w") as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n✓ Report saved to: {filename}")
        return filename
    
    def print_report(self, report: Dict[str, Any]):
        """Print report to console"""
        print(f"\n{'='*60}")
        print("REPORT SUMMARY")
        print(f"{'='*60}")
        
        print(f"\nCompany: {report.get('company')}")
        print(f"Generated: {report.get('timestamp')}")
        
        print(f"\n{report.get('executive_summary')}")
        
        print(f"\n{'='*60}")
        print("KEY RECOMMENDATIONS")
        print(f"{'='*60}")
        
        for i, rec in enumerate(report.get("recommendations", [])[:10], 1):
            print(f"{i}. {rec}")
        
        print(f"\n{'='*60}\n")


async def main():
    """Generate sample report"""
    sample_company = {
        "company_name": "TechStartup AI",
        "industry": "SaaS",
        "stage": "seed",
        "team_size": 5,
        "monthly_revenue": 5000,
        "monthly_burn": 25000,
        "total_funding": 250000,
        "target_market": "Enterprise",
        "competitors": ["Competitor1", "Competitor2"],
    }
    
    generator = ReportGenerator()
    report = await generator.generate_report(sample_company)
    generator.print_report(report)
    generator.save_report(report)


if __name__ == "__main__":
    asyncio.run(main())
