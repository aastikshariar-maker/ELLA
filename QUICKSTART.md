# Quick Start Guide

## 🚀 5-Minute Setup

### Option 1: Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/aastikshariar-maker/ai-cofounder.git
cd ai-cofounder

# Set up environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Start everything
docker-compose up --build
```

Then access:
- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs
- **Dashboard**: http://localhost:8501

### Option 2: Local Python

```bash
# Clone and setup
git clone https://github.com/aastikshariar-maker/ai-cofounder.git
cd ai-cofounder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Start PostgreSQL and Redis
# (Install and run locally or use Docker just for these)

# Initialize database
python scripts/init_db.py

# Seed sample data
python scripts/seed_data.py

# Start API server (Terminal 1)
python -m uvicorn app.main:app --reload

# Start Celery worker (Terminal 2)
celery -A app.celery_app worker --loglevel=info

# Start dashboard (Terminal 3)
streamlit run dashboard/app.py
```

## 📝 First Steps

### 1. Create a Company Profile

```bash
curl -X POST http://localhost:8000/api/companies/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "MyStartup",
    "industry": "SaaS",
    "stage": "seed",
    "team_size": 3,
    "monthly_revenue": 1000,
    "monthly_burn": 10000
  }'
```

Copy the `company_id` from the response.

### 2. Generate Comprehensive Analysis

```bash
python scripts/generate_report.py
```

This runs all AI agents and generates a complete report.

### 3. View Interactive Dashboard

Open http://localhost:8501 in your browser to access the Streamlit dashboard.

## 🎯 Key Features to Try

### Strategic Planning

```bash
curl -X POST http://localhost:8000/api/strategy/generate \
  -H "Content-Type: application/json" \
  -d '{"company_id": "YOUR_COMPANY_ID"}'
```

### Financial Analysis

```bash
# Get forecast
curl http://localhost:8000/api/financial/forecast/YOUR_COMPANY_ID?months=24

# Get runway
curl http://localhost:8000/api/financial/runway/YOUR_COMPANY_ID
```

### Market Analysis

```bash
# Get market sizing
curl http://localhost:8000/api/market/tam-sam-som/YOUR_COMPANY_ID

# Analyze competitors
curl http://localhost:8000/api/market/competitors/YOUR_COMPANY_ID
```

### Operations Optimization

```bash
# Get org structure recommendations
curl http://localhost:8000/api/operations/org-structure/YOUR_COMPANY_ID

# Get scaling roadmap
curl http://localhost:8000/api/operations/scaling-roadmap/YOUR_COMPANY_ID
```

## 📊 Dashboard Navigation

1. **Overview** - Key metrics and health score
2. **Strategy** - Strategic planning and OKRs
3. **Financials** - Burn rate, runway, forecasts
4. **Market** - TAM/SAM/SOM, competitors, segments
5. **Operations** - Org structure, scaling, hiring
6. **Reports** - Generate and view comprehensive reports

## 🔧 Environment Variables

Key variables in `.env`:

```bash
# OpenAI
OPENAI_API_KEY=sk-your-key
OPENAI_MODEL=gpt-4

# Database
DATABASE_URL=postgresql://user:password@localhost/aicofounder

# Redis
REDIS_URL=redis://localhost:6379

# Application
DEBUG=True
ENVIRONMENT=development
```

## 📚 Documentation

- **README.md** - Project overview
- **ARCHITECTURE.md** - System design and architecture
- **API.md** - Complete API reference
- **DEPLOYMENT.md** - Deployment guides for AWS, GCP, Azure
- **CONTRIBUTING.md** - Contributing guidelines

## 🧪 Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=app

# Specific test file
pytest tests/test_agents.py
```

## 🐛 Troubleshooting

### Database connection error

```bash
# Check PostgreSQL
pg_isready -h localhost -U aicofounder

# Create database manually if needed
psql -U postgres -c "CREATE DATABASE aicofounder;"
```

### Redis connection error

```bash
# Check Redis
redis-cli ping

# Should return: PONG
```

### API not starting

```bash
# Check environment variables
echo $DATABASE_URL
echo $OPENAI_API_KEY

# Check logs
tail -f logs/app.log
```

### OpenAI API errors

- Verify API key in `.env`
- Check OpenAI account has available credits
- Ensure model specified exists (default: gpt-4)

## 💡 Tips

1. **Start Small**: Begin with a single company profile
2. **Iterate**: Run analyses periodically to see how recommendations change
3. **Customize**: Edit prompts in `app/prompts/` for your domain
4. **Monitor**: Check dashboard regularly for key metrics
5. **Extend**: Add new agents by extending `BaseAgent` class

## 🚀 Next Steps

1. Read the [ARCHITECTURE.md](docs/ARCHITECTURE.md) to understand the system
2. Explore the [API.md](docs/API.md) for endpoint details
3. Check [DEPLOYMENT.md](docs/DEPLOYMENT.md) for production setup
4. Review [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute

## ❓ FAQ

**Q: Do I need OpenAI API key?**
A: Yes, for full AI capabilities. Without it, you'll get placeholder responses.

**Q: Can I use a different LLM?**
A: Yes! Modify `app/services/llm_service.py` to use your preferred LLM.

**Q: Is this production-ready?**
A: This is a beta platform. Review DEPLOYMENT.md before deploying to production.

**Q: How do I add new features?**
A: See CONTRIBUTING.md for guidelines.

## 📞 Support

- **Issues**: Open a GitHub issue
- **Discussions**: Start a GitHub discussion
- **Docs**: Check documentation folder
- **Email**: Contact the team

## 🎉 You're Ready!

You now have a fully functional AI Co-Founder platform. Start exploring and let your AI help guide your company to success!

For detailed information, see the full [README.md](README.md).
