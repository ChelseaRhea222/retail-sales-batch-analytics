#  Retail Sales Batch Analytics

An end-to-end batch analytics pipeline that ingests raw retail sales data, cleans and standardizes it, computes business KPIs, and produces analysis-ready datasets for reporting and dashboards.

This project simulates how analytics and data teams process transactional sales data in production environments using Python and batch ETL workflows.

---

##  Project Summary

Retail transaction data is often messy, inconsistent, and spread across multiple files. Before meaningful insights can be generated, the data must be cleaned, validated, and aggregated.

This pipeline automatically:

* Reads raw CSV sales files
* Cleans inconsistent formats (dates, prices, missing values)
* Normalizes columns
* Calculates KPIs and summaries
* Outputs clean datasets ready for dashboards or SQL analysis

Result → structured, analytics-ready data that supports decision-making.

---

##  Tech Stack

* Python
* Pandas
* CSV batch processing
* Git + GitHub
* CLI execution

---

##  Project Structure

```
retail-sales-batch-analytics/
│
├── data/                # raw retail sales files
├── output/              # cleaned + aggregated results
├── retail_batch_analytics.py
├── requirements.txt
└── README.md
```

---

##  Pipeline Flow

```
Raw CSV files
      ↓
Python ETL (clean + transform)
      ↓
Aggregations + KPIs
      ↓
Output tables (analysis ready)
      ↓
Dashboards / Reports / SQL
```

---

##  Metrics Generated

Example KPIs calculated:

* Total revenue
* Units sold
* Average price
* Sales by product
* Sales by category
* Daily / monthly trends
* Store performance comparisons

---

##  Installation

### Clone repository

```
git clone https://github.com/ChelseaRhea222/retail-sales-batch-analytics.git
cd retail-sales-batch-analytics
```

### Create virtual environment

Windows:

```
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```
pip install -r requirements.txt
```

---

##  Run the pipeline

```
python retail_batch_analytics.py
```

The script will:

✅ load raw sales files
✅ clean + standardize
✅ compute KPIs
✅ export results to `/output`

---

##  Example Use Cases

This dataset can power:

* Looker Studio dashboards
* Excel or Sheets analysis
* SQL warehouse uploads
* Sales forecasting
* Trend analysis
* Category performance reporting

---

##  Skills Demonstrated

* Data cleaning & preprocessing
* Batch ETL workflows
* Aggregation logic
* KPI design for business metrics
* File-based pipelines
* Reproducible analytics processes
* Professional project structure


##  Author

Chelsea Rhea
Data Analytics & Engineering Portfolio


