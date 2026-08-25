# AI Co-Founder Platform

An intelligent AI-powered co-founder system that serves as a strategic partner for companies, handling business planning, financial modeling, market analysis, operational decisions, and growth strategies.

## 🎯 Core Features

- **Strategic Planning** - Long-term vision, roadmap generation, goal setting
- **Financial Modeling** - Budget forecasting, unit economics, burn rate analysis
- **Market Analysis** - Competitive landscape, TAM/SAM/SOM calculations, market entry strategies
- **Operational Management** - Process optimization, KPI tracking, team structure recommendations
- **Investment Strategy** - Fundraising guidance, valuation modeling, investor relations
- **Product Strategy** - Feature prioritization, product-market fit analysis, roadmap planning
- **HR & Culture** - Hiring recommendations, org structure, culture frameworks
- **Real-time Analytics** - Dashboard, metrics tracking, performance monitoring

## 🏗️ Architecture

The system uses a multi-agent architecture:
- **Strategic Agent** - High-level business decisions and planning
- **Analytics Agent** - Data analysis and metrics
- **Financial Agent** - Budgeting and financial projections
- **Market Agent** - Market research and competitive analysis
- **Operations Agent** - Process and workflow optimization
- **Human Agent Coordinator** - Manages inter-agent communication and final decisions

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL (for persistence)
- Redis (for caching and task queues)
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/aastikshariar-maker/ai-cofounder.git
cd ai-cofounder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

```bash
# Start the API server
python -m uvicorn app.main:app --reload

# In another terminal, start the task worker
celery -A app.celery_app worker --loglevel=info

# Optional: Start the dashboard
streamlit run dashboard/app.py
```

## 📁 Project Structure

```
ai-cofounder/
├── app/                          # Main application
│   ├── main.py                   # FastAPI entry point
│   ├── config.py                 # Configuration management
│   ├── database.py               # Database setup
│   ├── celery_app.py             # Celery task queue
│   │
│   ├── agents/                   # Multi-agent system
│   │   ├── base_agent.py         # Base agent interface
│   │   ├── strategic_agent.py    # Strategic decision making
│   │   ├── analytics_agent.py    # Data analysis
│   │   ├── financial_agent.py    # Financial modeling
│   │   ├── market_agent.py       # Market research
│   │   ├── operations_agent.py   # Operations optimization
│   │   └── coordinator.py        # Agent orchestration
│   │
│   ├── models/                   # Data models
│   │   ├── company.py            # Company profile
│   │   ├── strategy.py           # Strategic plans
│   │   ├── financial.py          # Financial models
│   │   ├── market.py             # Market data
│   │   └── metrics.py            # KPIs and metrics
│   │
│   ├── services/                 # Business logic
│   │   ├── llm_service.py        # LLM interactions
│   │   ├── analysis_service.py   # Analysis engine
│   │   ├── planning_service.py   # Planning logic
│   │   ├── forecasting_service.py# Financial forecasting
│   │   └── reporting_service.py  # Report generation
│   │
│   ├── api/                      # API routes
│   │   ├── companies.py          # Company management
│   │   ├── strategy.py           # Strategy endpoints
│   │   ├── financial.py          # Financial endpoints
│   │   ├── market.py             # Market analysis
│   │   ├── operations.py         # Operations endpoints
│   │   └── analytics.py          # Analytics endpoints
│   │
│   ├── tools/                    # Tool definitions
│   │   ├── financial_tools.py    # Financial calculation tools
│   │   ├── market_tools.py       # Market research tools
│   │   ├── planning_tools.py     # Planning tools
│   │   └── analysis_tools.py     # Analysis tools
│   │
│   ├── utils/                    # Utilities
│   │   ├── validators.py         # Input validation
│   │   ├── formatting.py         # Output formatting
│   │   └── constants.py          # Constants
│   │
│   └── prompts/                  # LLM prompts
│       ├── strategic_prompts.py
│       ├── financial_prompts.py
│       ├── market_prompts.py
│       └── operations_prompts.py
│
├── dashboard/                    # Streamlit dashboard
│   ├── app.py                    # Main dashboard
│   ├── pages/
│   │   ├── overview.py
│   │   ├── strategy.py
│   │   ├── financials.py
│   │   ├── market.py
│   │   └── operations.py
│   └── components/               # Reusable UI components
│
├── tests/                        # Test suite
│   ├── test_agents.py
│   ├── test_services.py
│   ├── test_api.py
│   └── fixtures/
│
├── docs/                         # Documentation
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── PROMPTS.md
│   └── DEPLOYMENT.md
│
├── scripts/                      # Utility scripts
│   ├── seed_data.py              # Populate sample data
│   ├── init_db.py                # Database initialization
│   └── generate_report.py        # Report generation
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
├── .gitignore
└── pyproject.toml               # Poetry configuration
```

## 🤖 How It Works

1. **Company Profile** - Input your company details (stage, industry, team, etc.)
2. **Analysis** - AI analyzes current state and identifies key challenges
3. **Strategy Generation** - Agents collaboratively create strategies
4. **Financial Modeling** - Project financials, runway, growth scenarios
5. **Recommendations** - Get actionable insights and prioritized tasks
6. **Execution** - Implement recommendations with metrics tracking
7. **Iteration** - Continuous optimization based on real results

## 📊 Key Modules

### Strategic Agent
- 5-year vision development
- OKR (Objectives & Key Results) generation
- Competitive positioning
- Market entry strategies
- Pivot analysis

### Financial Agent
- Cash flow modeling
- Burn rate analysis
- Revenue projections
- Unit economics
- Fundraising scenarios
- Break-even analysis

### Market Agent
- TAM/SAM/SOM calculation
- Competitor analysis
- Market trends
- Customer segmentation
- Pricing strategy

### Operations Agent
- Process mapping
- Workflow optimization
- KPI definition
- Team structure recommendations
- Scaling strategies

## 🔧 Configuration

Edit `.env`:
```
OPENAI_API_KEY=sk-...
DATABASE_URL=postgresql://user:password@localhost/aicofounder
REDIS_URL=redis://localhost:6379
DEBUG=False
```

## 📈 API Examples

### Create Company
```bash
curl -X POST http://localhost:8000/api/companies \
  -H "Content-Type: application/json" \
  -d '{
    "name": "TechStartup",
    "industry": "SaaS",
    "stage": "seed",
    "team_size": 3,
    "monthly_revenue": 5000
  }'
```

### Generate Strategy
```bash
curl -X POST http://localhost:8000/api/strategy/generate \
  -H "Content-Type: application/json" \
  -d '{"company_id": "123"}'
```

### Get Financial Forecast
```bash
curl http://localhost:8000/api/financial/forecast/123?months=24
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_agents.py::test_strategic_agent
```

## 🐳 Docker

```bash
# Build and run
docker-compose up --build

# Run specific service
docker-compose up api
```

## 📚 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Prompt Engineering Guide](docs/PROMPTS.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🤝 Contributing

1. Create a feature branch
2. Implement changes
3. Add tests
4. Submit PR

## 📝 License

MIT License - see LICENSE file

## 🎓 Learn More

- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
- [Financial Modeling Basics](https://en.wikipedia.org/wiki/Financial_modeling)
- [Strategic Planning](https://en.wikipedia.org/wiki/Strategic_planning)

---

**Status**: Beta (Active Development)
**Last Updated**: 2025
**Maintainer**: @aastikshariar-maker