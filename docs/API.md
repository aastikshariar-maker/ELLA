# API Reference

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. Production deployments should implement JWT-based authentication.

## Endpoints

### Companies

#### Create Company

```http
POST /api/companies/
```

**Parameters:**
- `name` (string, required): Company name
- `industry` (string, required): Industry
- `stage` (string, optional): Company stage (default: "seed")
- `team_size` (integer, optional): Team size (default: 1)
- `monthly_revenue` (float, optional): Monthly revenue (default: 0)
- `monthly_burn` (float, optional): Monthly burn rate (default: 5000)

**Response:**
```json
{
  "success": true,
  "company_id": "uuid",
  "name": "Company Name",
  "industry": "SaaS",
  "stage": "seed"
}
```

#### Get Company

```http
GET /api/companies/{company_id}
```

**Response:**
```json
{
  "id": "uuid",
  "name": "Company Name",
  "industry": "SaaS",
  "stage": "seed",
  "team_size": 5,
  "monthly_revenue": 5000,
  "monthly_burn": 25000
}
```

#### Update Company

```http
PUT /api/companies/{company_id}
```

**Parameters:**
- `team_size` (integer, optional)
- `monthly_revenue` (float, optional)
- `monthly_burn` (float, optional)

**Response:**
```json
{
  "success": true,
  "company_id": "uuid"
}
```

### Strategy

#### Generate Strategy

```http
POST /api/strategy/generate
```

**Parameters:**
- `company_id` (string, required): Company ID

**Response:**
```json
{
  "success": true,
  "company_id": "uuid",
  "strategy": {
    "agent": "Strategic Agent",
    "timestamp": "2026-08-25T10:00:00",
    "strategic_analysis": {...},
    "okrs": {...},
    "competitive_position": {...},
    "recommendations": [...]
  }
}
```

#### Generate OKRs

```http
POST /api/strategy/{company_id}/okrs
```

**Response:**
```json
{
  "success": true,
  "company_id": "uuid",
  "okrs": {
    "quarterly_okrs": [...],
    "annual_objectives": [...]
  }
}
```

### Financial

#### Analyze Financials

```http
POST /api/financial/analyze
```

**Parameters:**
- `company_id` (string, required)

**Response:**
```json
{
  "success": true,
  "company_id": "uuid",
  "analysis": {
    "current_metrics": {...},
    "forecasts": {...},
    "burn_analysis": {...},
    "fundraising_strategy": {...},
    "recommendations": [...]
  }
}
```

#### Get Financial Forecast

```http
GET /api/financial/forecast/{company_id}?months=24
```

**Response:**
```json
{
  "company_id": "uuid",
  "months": 24,
  "forecast": {
    "24_month_revenue": 500000,
    "24_month_burn": 600000,
    "breakeven_month": 18
  }
}
```

#### Get Runway

```http
GET /api/financial/runway/{company_id}
```

**Response:**
```json
{
  "company_id": "uuid",
  "runway_months": 10,
  "health_status": "Caution",
  "recommendation": "Begin fundraising process"
}
```

### Market

#### Analyze Market

```http
POST /api/market/analyze
```

**Parameters:**
- `company_id` (string, required)

**Response:**
```json
{
  "success": true,
  "company_id": "uuid",
  "analysis": {
    "market_sizing": {...},
    "competitive_analysis": {...},
    "customer_segments": {...},
    "market_trends": {...},
    "pricing_strategy": {...}
  }
}
```

#### Get Market Sizing (TAM/SAM/SOM)

```http
GET /api/market/tam-sam-som/{company_id}
```

**Response:**
```json
{
  "company_id": "uuid",
  "tam": "$500B",
  "sam": "$250B",
  "som": "$2.5B"
}
```

#### Analyze Competitors

```http
GET /api/market/competitors/{company_id}
```

**Response:**
```json
{
  "company_id": "uuid",
  "competitors": [
    {"name": "Competitor1", "market_position": "Leader"},
    {"name": "Competitor2", "market_position": "Challenger"}
  ]
}
```

### Operations

#### Analyze Operations

```http
POST /api/operations/analyze
```

**Parameters:**
- `company_id` (string, required)

**Response:**
```json
{
  "success": true,
  "company_id": "uuid",
  "analysis": {
    "organizational_structure": {...},
    "process_recommendations": {...},
    "scaling_strategy": {...},
    "kpi_framework": {...},
    "hiring_roadmap": [...]
  }
}
```

#### Get Organizational Structure

```http
GET /api/operations/org-structure/{company_id}
```

#### Get Scaling Roadmap

```http
GET /api/operations/scaling-roadmap/{company_id}
```

### Analytics

#### Get Dashboard

```http
GET /api/analytics/dashboard/{company_id}
```

**Response:**
```json
{
  "company_id": "uuid",
  "metrics": {...},
  "health_score": 65
}
```

#### Get KPIs

```http
GET /api/analytics/kpis/{company_id}
```

#### Generate Report

```http
POST /api/analytics/report/{company_id}
```

## Error Handling

All errors return appropriate HTTP status codes with error messages:

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Status Codes

- `200`: Success
- `400`: Bad request
- `404`: Not found
- `422`: Validation error
- `500`: Server error

## Rate Limiting

Currently no rate limiting is implemented. Production deployments should implement rate limiting.

## Versioning

API is currently at v1. Future versions will use `/api/v2/` prefixes.

## Pagination

List endpoints support pagination with `page` and `per_page` query parameters.

## Filtering

List endpoints support filtering with query parameters specific to each endpoint.
