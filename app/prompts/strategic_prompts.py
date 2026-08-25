"""Strategic Agent Prompts"""

STRATEGIC_ANALYSIS_PROMPT = """
Analyze the strategic positioning and opportunities for {company} in the {industry} industry.

Company Details:
- Company: {company}
- Industry: {industry}
- Current Stage: {stage}
- Team Size: {team_size}
- Target Market: {target_market}

Provide analysis on:
1. Market opportunity and potential
2. Competitive advantages
3. Key challenges and risks
4. Growth levers and expansion opportunities
5. 5-year vision and strategic direction

Be specific and actionable in your recommendations.
"""

OKR_GENERATION_PROMPT = """
Generate quarterly and annual OKRs (Objectives & Key Results) for {company}.

Context:
- Vision: {vision}
- Market Opportunity: {opportunities}

Create:
1. 3-4 key objectives for the next quarter
2. 3 measurable key results for each objective
3. Annual objectives aligned with 5-year vision
4. Success metrics and tracking approach

Make OKRs ambitious yet achievable, measurable, and aligned with company stage.
"""

COMPETITIVE_ANALYSIS_PROMPT = """
Conduct competitive analysis for {company} against main competitors.

Competitors: {competitors}

Analyze:
1. Competitive positioning matrix
2. Strengths and weaknesses vs competitors
3. Market share and growth rates
4. Differentiation opportunities
5. Defensive strategies
"""
