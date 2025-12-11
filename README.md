# E-Commerce Data Pipeline (ELT)

A complete end-to-end data pipeline for e-commerce analytics using Python, SQLite, and Apache Airflow. This project demonstrates modern data engineering practices including ELT operations, data validation, and automated reporting with visualizations.


## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Data Visualizations](#data-visualizations)
- [SQL Transformations](#sql-transformations)

## 🎯 Overview

This project implements a production-ready data pipeline for analyzing e-commerce data from Olist, a Brazilian marketplace platform. The pipeline handles the complete data lifecycle from extraction through transformation and reporting, with both manual and automated execution modes.

### Key Capabilities

- **Extract**: Ingest CSV datasets and external API data (Brazil public holidays)
- **Load**: Persist data to SQLite with proper schema management
- **Transform**: Execute SQL-based transformations for business intelligence
- **Validate**: Automated data quality and pipeline integrity checks
- **Report**: Generate analytics reports with visualizations

## ✨ Features

-  Automated ELT pipeline orchestration with Apache Airflow
-  Comprehensive data visualizations and analytics
-  Built-in data validation and quality checks
-  Dockerized deployment for consistency
-  Business intelligence queries for revenue, delivery, and order analysis
-  Custom Airflow operators for reusable components
-  Detailed logging and error handling

## 🏗️ Architecture

```
┌─────────────┐     ┌──────────┐     ┌──────────────┐     ┌──────────┐
│   Extract   │────▶│   Load   │────▶│  Transform   │────▶│ Validate │
│  (CSV/API)  │     │ (SQLite) │     │ (SQL Queries)│     │ & Report │
└─────────────┘     └──────────┘     └──────────────┘     └──────────┘
```

The pipeline follows the ELT (Extract, Load, Transform) pattern, optimizing for performance by loading raw data first and transforming within the database.

## 📁 Project Structure

```
E-Commerce-Data-Pipeline-ELT/
│
├── airflow/
│   ├── dags/
│   │   ├── ecommerce_etl_dag.py          # Full production DAG
│   │   └── simple_ecommerce_dag.py       # Simplified demo DAG
│   ├── operators/
│   │   └── etl_operators.py              # Custom Airflow operators
│   └── docker-compose-simple.yml         # Simplified Airflow setup
│
├── dataset/                               # Source CSV files
├── queries/                               # SQL transformation queries
├── src/                                   # Core Python modules
│   ├── extract.py                        # Data extraction logic
│   ├── load.py                           # Database loading
│   ├── transform.py                      # SQL transformation runner
│   ├── plots.py                          # Visualization generators
│   └── config.py                         # Configuration management
│
├── images/                                # Generated visualizations
├── docker-compose.yml                     # Production Airflow with Postgres
├── requirements.txt                       # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/harshitha-giriraju/E-Commerce-Data-Pipeline-ELT.git
   cd E-Commerce-Data-Pipeline-ELT
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify dataset files**
   Ensure all CSV files are present in the `dataset/` folder.

## 💻 Usage

### Option 1: Manual Execution

Run the pipeline manually without orchestration:

```bash
# Step 1: Extract data from sources
python -m src.extract

# Step 2: Load data into SQLite
python -m src.load

# Step 3: Run SQL transformations
python -m src.transform

# Step 4: (Optional) Open Jupyter for analysis
jupyter notebook "AnyoneAI - Sprint Project 01.ipynb"
```

### Option 2: Automated with Airflow (Recommended)

#### Quick Start (Simplified Setup)

```bash
cd airflow
docker-compose -f docker-compose-simple.yml up -d
```

Access Airflow UI at **http://localhost:8081**

**Default credentials:**
- Username: `admin`
- Password: `admin`

#### Production Setup (with PostgreSQL)

For a production-grade setup with PostgreSQL backend:

```bash
docker-compose up -d
```

Access Airflow UI at **http://localhost:8080**

### Available DAGs

| DAG Name | Description | Schedule |
|----------|-------------|----------|
| `ecommerce_etl_pipeline` | Complete ELT pipeline with validation and reporting | Daily at 2:00 AM |
| `simple_ecommerce_etl` | Simplified demonstration pipeline | Daily |

**To trigger a DAG:**
1. Navigate to the Airflow UI
2. Find the desired DAG in the list
3. Toggle it to "On" (if paused)
4. Click the "Trigger DAG" button (▶️ icon)

## 📊 Data Visualizations

The pipeline generates insightful visualizations including:

- **Revenue Analysis**: Monthly trends and state-level distribution
- **Order Patterns**: Daily order volumes with holiday correlations
- **Delivery Performance**: Actual vs estimated delivery times
- **Product Insights**: Top and bottom performing categories
- **Logistics Analysis**: Freight value vs product weight relationships

Sample outputs are saved in the `images/` directory:

- `revenue_by_month_year.png`
- `orders_per_day_and_holidays.png`
- `freight_value_weight_relationship.png`
- `top_10_revenue_categories.png`
- And more...

## 🔍 SQL Transformations

The `queries/` folder contains business intelligence SQL queries:

| Query | Business Question |
|-------|------------------|
| `revenue_by_month_year.sql` | What are our monthly revenue trends? |
| `revenue_per_state.sql` | Which states generate the most revenue? |
| `orders_per_day_and_holidays_2017.sql` | How do holidays affect order volumes? |
| `top_10_revenue_categories.sql` | What are our best-selling product categories? |
| `top_10_sellers_by_revenue.sql` | Who are our top-performing sellers? |
| `real_vs_estimated_delivered_time.sql` | How accurate are our delivery estimates? |
| `delivery_date_difference.sql` | What is the delivery time variance? |
| `global_ammount_order_status.sql` | What is the distribution of order statuses? |

