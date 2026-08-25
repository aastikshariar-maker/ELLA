#!/usr/bin/env python
"""CLI for AI Co-Founder Platform"""

import click
import asyncio
import json
from datetime import datetime

from scripts.generate_report import ReportGenerator
from app.config import settings


@click.group()
def cli():
    """AI Co-Founder Platform CLI"""
    pass


@cli.command()
@click.option('--name', prompt='Company name', help='Company name')
@click.option('--industry', prompt='Industry', help='Industry')
@click.option('--stage', default='seed', help='Company stage')
@click.option('--team-size', type=int, default=1, help='Team size')
@click.option('--revenue', type=float, default=0, help='Monthly revenue')
@click.option('--burn', type=float, default=5000, help='Monthly burn')
def analyze(name, industry, stage, team_size, revenue, burn):
    """Analyze a company"""
    click.echo(f"\n{'='*60}")
    click.echo(f"Analyzing {name}...")
    click.echo(f"{'='*60}\n")
    
    company_data = {
        "company_name": name,
        "industry": industry,
        "stage": stage,
        "team_size": team_size,
        "monthly_revenue": revenue,
        "monthly_burn": burn,
        "total_funding": burn * 12,
        "target_market": "Enterprise",
        "competitors": [],
    }
    
    async def run():
        generator = ReportGenerator()
        report = await generator.generate_report(company_data)
        generator.print_report(report)
        generator.save_report(report)
    
    asyncio.run(run())
    click.echo("\n✓ Analysis complete!")


@cli.command()
def init():
    """Initialize database"""
    click.echo("Initializing database...")
    
    async def run():
        from app.database import init_db
        await init_db()
    
    asyncio.run(run())
    click.echo("✓ Database initialized!")


@cli.command()
def seed():
    """Seed database with sample data"""
    click.echo("Seeding database...")
    
    import subprocess
    subprocess.run(["python", "scripts/seed_data.py"])
    click.echo("✓ Database seeded!")


@cli.command()
def config():
    """Show current configuration"""
    click.echo("\nCurrent Configuration:")
    click.echo(f"  Environment: {settings.ENVIRONMENT}")
    click.echo(f"  Debug: {settings.DEBUG}")
    click.echo(f"  Database: {settings.DATABASE_URL}")
    click.echo(f"  Redis: {settings.REDIS_URL}")
    click.echo(f"  API Host: {settings.API_HOST}:{settings.API_PORT}")
    click.echo(f"  OpenAI Model: {settings.OPENAI_MODEL}")


@cli.command()
def version():
    """Show version"""
    click.echo(f"AI Co-Founder Platform v{settings.APP_VERSION}")


if __name__ == "__main__":
    cli()
