# Deployment Guide

## Local Development Setup

### Prerequisites
- Python 3.10+
- PostgreSQL
- Redis
- Docker & Docker Compose (optional)

### Quick Start

```bash
# Clone repository
git clone https://github.com/aastikshariar-maker/ai-cofounder.git
cd ai-cofounder

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your settings

# Initialize database
python scripts/init_db.py

# Run migrations
alembic upgrade head

# Start API server
python -m uvicorn app.main:app --reload

# In another terminal, start Celery worker
celery -A app.celery_app worker --loglevel=info

# In another terminal, start dashboard
streamlit run dashboard/app.py
```

The application will be available at:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Dashboard: http://localhost:8501

## Docker Deployment

### Using Docker Compose

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down
```

Services will be available at:
- API: http://localhost:8000
- Dashboard: http://localhost:8501
- Database: localhost:5432
- Redis: localhost:6379

## Production Deployment

### Environment Setup

```bash
# Set environment to production
echo "ENVIRONMENT=production" >> .env
echo "DEBUG=False" >> .env

# Generate new secret key
python -c "import secrets; print(secrets.token_urlsafe(32))" >> .env
```

### Database Migration

```bash
# Create migration
alembic revision --autogenerate -m "Initial schema"

# Apply migration
alembic upgrade head
```

### AWS Deployment

#### Using EC2

```bash
# On EC2 instance
sudo yum update -y
sudo yum install python3 python3-venv postgresql postgresql-devel -y

# Clone and setup
git clone <repo-url>
cd ai-cofounder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

#### Using ECS

```bash
# Build Docker image
docker build -t ai-cofounder:latest -f docker/Dockerfile .

# Tag for ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com

docker tag ai-cofounder:latest <account>.dkr.ecr.us-east-1.amazonaws.com/ai-cofounder:latest

# Push to ECR
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/ai-cofounder:latest
```

#### Using RDS

```sql
-- Create database
CREATE DATABASE aicofounder;

-- Create user
CREATE USER aicofounder WITH PASSWORD 'secure_password';

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE aicofounder TO aicofounder;
```

### GCP Deployment

#### Using Cloud Run

```bash
# Build and deploy
gcloud run deploy ai-cofounder \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars DATABASE_URL=$DATABASE_URL,REDIS_URL=$REDIS_URL,OPENAI_API_KEY=$OPENAI_API_KEY
```

#### Using Cloud SQL

```bash
# Create Cloud SQL instance
gcloud sql instances create aicofounder \
  --database-version POSTGRES_15 \
  --tier db-f1-micro

# Create database
gcloud sql databases create aicofounder --instance=aicofounder
```

### Azure Deployment

#### Using App Service

```bash
# Create resource group
az group create --name aicofounder-rg --location eastus

# Create App Service plan
az appservice plan create --name aicofounder-plan --resource-group aicofounder-rg

# Create web app
az webapp create --resource-group aicofounder-rg --plan aicofounder-plan --name aicofounder
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-cofounder
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-cofounder
  template:
    metadata:
      labels:
        app: ai-cofounder
    spec:
      containers:
      - name: api
        image: ai-cofounder:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: ai-cofounder-secrets
              key: database-url
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: ai-cofounder-secrets
              key: openai-api-key
```

## Monitoring & Logging

### Application Metrics

```python
# Using Prometheus
from prometheus_client import Counter, Histogram

request_count = Counter('requests_total', 'Total requests')
request_duration = Histogram('request_duration_seconds', 'Request duration')
```

### Logging Setup

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
handler = RotatingFileHandler('logs/app.log', maxBytes=10485760, backupCount=5)
logger.addHandler(handler)
```

### Health Checks

```bash
# Check API health
curl http://localhost:8000/health

# Check database connection
curl http://localhost:8000/api/health/db

# Check Redis connection
curl http://localhost:8000/api/health/redis
```

## Scaling Considerations

### Horizontal Scaling

1. **Load Balancing**: Use load balancer (AWS ALB, Azure LB, GCP LB)
2. **Database**: Use managed database service with read replicas
3. **Caching**: Distribute Redis instances
4. **Workers**: Scale Celery workers independently

### Vertical Scaling

1. Increase server resources (CPU, RAM)
2. Optimize database queries
3. Implement caching strategies
4. Use connection pooling

## Backup & Recovery

```bash
# Database backup
pg_dump -h localhost -U aicofounder aicofounder > backup.sql

# Database restore
psql -h localhost -U aicofounder aicofounder < backup.sql

# Redis backup
redis-cli BGSAVE
```

## Security Best Practices

1. **Secrets Management**: Use environment variables or secret manager
2. **SSL/TLS**: Enable HTTPS
3. **Authentication**: Implement JWT-based authentication
4. **Rate Limiting**: Protect against abuse
5. **CORS**: Configure for allowed origins
6. **Database**: Use strong passwords, restrict access
7. **Monitoring**: Set up alerts for suspicious activity

## Troubleshooting

### Common Issues

#### Database Connection Error

```bash
# Check database status
pg_isready -h localhost -U aicofounder

# Verify connection string
echo $DATABASE_URL
```

#### Redis Connection Error

```bash
# Check Redis status
redis-cli ping

# Verify connection
redis-cli -h localhost -p 6379
```

#### API Not Starting

```bash
# Check logs
tail -f logs/app.log

# Verify environment
python -c "from app.config import settings; print(settings.dict())"
```

## Support

For issues and questions, please:
1. Check the documentation
2. Review logs
3. Create an issue on GitHub
4. Contact the team
