"""Dashboard Streamlit Application"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="AI Co-Founder Dashboard", layout="wide")

# Sidebar
st.sidebar.title("AI Co-Founder Platform")
page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Strategy", "Financials", "Market", "Operations", "Reports"]
)

company_id = st.sidebar.text_input("Company ID", value="comp_123")

# Main content
if page == "Overview":
    st.title("Company Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Monthly Revenue", "$5,000", "+10%")
    with col2:
        st.metric("Monthly Burn", "$25,000", "-5%")
    with col3:
        st.metric("Runway (months)", "10", "-1")
    with col4:
        st.metric("Health Score", "65%", "+5%")
    
    st.subheader("Key Metrics")
    data = {
        "Metric": ["MRR", "CAC", "Churn Rate", "NPS"],
        "Current": [5000, 500, 5, 45],
        "Target": [10000, 300, 3, 50],
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

elif page == "Strategy":
    st.title("Strategic Planning")
    
    st.subheader("Vision & Mission")
    st.write("""Define your company's long-term vision and strategic direction.""")
    
    if st.button("Generate Strategy"):
        st.success("Strategy generated successfully!")
        st.write("""**Vision**: Market leadership through innovation
**Mission**: Build the best product in the industry
**Strategy**: Focus on enterprise segment with premium positioning""")
    
    st.subheader("OKRs")
    okrs = [
        {"Objective": "Achieve Product-Market Fit", "Key Results": "100 users, 40% retention, NPS 50+"},
        {"Objective": "Build Strong Team", "Key Results": "Hire 2 engineers, 1 sales, establish culture"},
        {"Objective": "Establish Market Position", "Key Results": "5 customers, $10K MRR, thought leadership"},
    ]
    
    for okr in okrs:
        with st.expander(okr["Objective"]):
            st.write(f"**Key Results**: {okr['Key Results']}")

elif page == "Financials":
    st.title("Financial Analysis & Forecasting")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Metrics")
        st.metric("Monthly Revenue", "$5,000")
        st.metric("Monthly Burn", "$25,000")
        st.metric("Cash on Hand", "$100,000")
        st.metric("Runway", "4 months", delta="Critical")
    
    with col2:
        st.subheader("Burn Rate Analysis")
        fig = go.Figure()
        months = ['Month 1', 'Month 2', 'Month 3', 'Month 4']
        burn = [25000, 24000, 23000, 22000]
        fig.add_trace(go.Scatter(x=months, y=burn, mode='lines+markers', name='Burn Rate'))
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("24-Month Forecast")
    if st.button("Generate Forecast"):
        forecast_data = {
            "Month": [i for i in range(1, 25)],
            "Revenue": [5000 * (1.1 ** i) for i in range(24)],
            "Burn": [25000 * (0.98 ** i) for i in range(24)],
        }
        forecast_df = pd.DataFrame(forecast_data)
        st.line_chart(forecast_df.set_index('Month'))
    
    st.subheader("Fundraising Strategy")
    st.write("""
    **Recommended Round**: Series A
    **Target Raise**: $500K - $1M
    **Timeline**: Next 3-6 months
    **Key Metrics to Showcase**: MRR, Growth Rate, Unit Economics
    """)

elif page == "Market":
    st.title("Market Analysis")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("TAM", "$500B")
    with col2:
        st.metric("SAM", "$250B")
    with col3:
        st.metric("SOM", "$2.5B")
    
    st.subheader("Customer Segments")
    segments = pd.DataFrame({
        "Segment": ["Enterprise", "Mid-Market", "SMB"],
        "Size": ["10% of TAM", "35% of TAM", "55% of TAM"],
        "Willingness to Pay": ["High", "Medium-High", "Low-Medium"],
    })
    st.dataframe(segments, use_container_width=True)
    
    st.subheader("Competitive Analysis")
    competitors = pd.DataFrame({
        "Competitor": ["Competitor1", "Competitor2", "Competitor3"],
        "Market Position": ["Leader", "Challenger", "Emerging"],
        "Strengths": ["Brand", "Technology", "Agility"],
        "Weaknesses": ["Legacy tech", "Limited reach", "Small team"],
    })
    st.dataframe(competitors, use_container_width=True)

elif page == "Operations":
    st.title("Operations & Scaling")
    
    st.subheader("Organizational Structure")
    org_text = """
    ```
    CEO
    ├── CTO (Engineering)
    ├── Head of Sales (GTM)
    └── Operations
    ```
    """
    st.markdown(org_text)
    
    st.subheader("Scaling Roadmap")
    phases = {
        "Phase 1 (Months 1-3)": "Validate PMF, Establish core team, Build processes",
        "Phase 2 (Months 4-9)": "Scale revenue, Hire specialists, Optimize operations",
        "Phase 3 (Months 10+)": "Build departments, Establish governance, Prepare for funding",
    }
    
    for phase, description in phases.items():
        with st.expander(phase):
            st.write(description)
    
    st.subheader("KPI Framework")
    kpi_categories = {
        "Product Metrics": ["DAU", "MAU", "Retention Rate", "NPS"],
        "Business Metrics": ["MRR", "ARR", "CAC", "LTV", "Churn Rate"],
        "Operational Metrics": ["Team Productivity", "Time to Hire", "Cost per Employee"],
    }
    
    for category, kpis in kpi_categories.items():
        st.write(f"**{category}**: {', '.join(kpis)}")

elif page == "Reports":
    st.title("Reports & Insights")
    
    st.subheader("Generate Comprehensive Report")
    if st.button("Generate AI Analysis Report"):
        st.success("Report generated!")
        
        sections = [
            ("Executive Summary", "High-level overview of company status and recommendations"),
            ("Strategic Analysis", "Deep dive into strategy, positioning, and growth opportunities"),
            ("Financial Forecast", "24-month projections and fundraising strategy"),
            ("Market Analysis", "TAM/SAM/SOM, competitor analysis, and positioning"),
            ("Operational Plan", "Scaling roadmap, hiring plan, and process recommendations"),
            ("Action Items", "Prioritized recommendations for immediate action"),
        ]
        
        for title, description in sections:
            with st.expander(title):
                st.write(description)
    
    st.subheader("Previous Reports")
    reports = pd.DataFrame({
        "Date": ["2026-08-20", "2026-08-15", "2026-08-10"],
        "Type": ["Full Analysis", "Financial Review", "Market Update"],
        "Status": ["Completed", "Completed", "Completed"],
    })
    st.dataframe(reports, use_container_width=True)
