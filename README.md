# 📊 Bluestock Mutual Fund Capstone Project

## Overview
End-to-end data analytics project using Python, SQL, and Power BI.

## Project Workflow
1. Data ingestion from raw CSV files
2. Data cleaning and preprocessing
3. Data validation checks
4. Loading into SQLite database
5. Analysis using Python (Pandas, NumPy)
6. Visualization using Power BI

## Folder Structure
- data/ → raw & processed datasets
- scripts/ → ETL pipeline scripts
- notebooks/ → EDA analysis
- db/ → SQLite database
- dashboard/ → Power BI file
- reports/ → final report & PPT

## How to Run Project

### Step 1: Activate environment
```bash
venv\Scripts\activate
``` id="s1"

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
``` id="s2"

### Step 3: Run pipeline
```bash
python scripts/run_pipeline.py
``` id="s3"

## Output
- Clean datasets in data/processed/
- SQLite database in db/
- Power BI dashboard in dashboard/
- Reports in reports/

## Status
✔ ETL Pipeline Completed  
✔ Data Cleaning Completed  
✔ EDA Completed  
✔ Dashboard Ready  
✔ Ready for Submission