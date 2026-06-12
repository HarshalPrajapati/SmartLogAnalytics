# SmartLogAnalytics

SmartLogAnalytics is a Python-based Log Analytics System that processes server logs, stores them in PostgreSQL, and generates meaningful insights through automated analytics.

The project is being developed as part of a structured Data Engineering and Analytics learning roadmap covering Linux, Python, SQL, PostgreSQL, Data Engineering, and Analytics concepts.

---

## Features

### Log Processing

* Read server log files
* Parse raw log entries into structured records
* Extract timestamps, log levels, and messages

### Analytics

* Count total log entries
* Count logs by severity level
* Extract error messages
* Generate keyword-based analytics
* Summarize log activity

### Database Integration

* PostgreSQL integration using psycopg2
* Store parsed logs in a relational database
* Retrieve logs directly from PostgreSQL
* Foundation for SQL-based analytics

---

## Tech Stack

### Languages

* Python 3.12

### Database

* PostgreSQL 16

### Libraries

* psycopg2-binary

### Tools

* Git
* GitHub
* Ubuntu (WSL2)

---

## Project Architecture

```text
server.log
    │
    ▼
parse_logs.py
    │
    ▼
Structured Log Records
    │
    ▼
PostgreSQL Database
    │
    ▼
Analytics Engine
    │
    ▼
Reports & Insights
```

---

## Project Structure

```text
SmartLogAnalytics/
│
├── backend/
│   ├── parse_logs.py
│   ├── test_db.py
│   │
│   └── modules/
│       ├── analytics_engine.py
│       ├── database.py
│       └── reporting_engine.py
│
├── logs/
│   └── server.log
│
├── README.md
│
└── .gitignore
```

---

## Database Schema

### logs

| Column    | Type               |
| --------- | ------------------ |
| id        | SERIAL PRIMARY KEY |
| timestamp | TEXT               |
| level     | VARCHAR(20)        |
| message   | TEXT               |

---

## Implemented Milestones

### Day 1 – Linux & Git

* Linux fundamentals
* Git basics
* GitHub integration

### Day 2 – Log File Processing

* File handling
* Log file reading

### Day 3 – Python Foundations

* Functions
* Lists
* Dictionaries
* File processing

### Day 4 – Log Parsing Engine

* Log parser implementation
* Structured log records

### Day 5 – Analytics Engine

* Log counting
* Error extraction
* Keyword analytics

### Day 6 – Reporting Engine

* Summary generation
* Analytics reporting

### Day 7 – PostgreSQL Fundamentals

* Database creation
* Table creation
* SQL basics

### Day 8 – Database Integration

* PostgreSQL setup
* Python database connectivity
* Log storage pipeline
* ETL workflow

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/HarshalPrajapati/SmartLogAnalytics.git
cd SmartLogAnalytics
```

### Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install psycopg2-binary
```

### Start PostgreSQL

```bash
sudo service postgresql start
```

### Run the Parser

```bash
cd backend
python parse_logs.py
```

---

## Sample Output

```text
===== LOG ANALYTICS SUMMARY =====

Total Logs: 100

Log Level Counts:
INFO: 60
WARNING: 25
ERROR: 15

Keyword Analytics:
Payment Logs: 20
Login Logs: 35
Database Logs: 10
```

---

## Future Enhancements

### SQL Analytics Engine

* SQL aggregation queries
* Database-driven reporting
* Trend analysis

### Dashboard Development

* Interactive analytics dashboard
* Data visualization

### Data Engineering Enhancements

* ETL automation
* Batch processing
* Data pipelines

### Machine Learning

* Log anomaly detection
* Failure prediction

### Deployment

* Docker containerization
* Cloud deployment

---

## Learning Objectives

This project demonstrates:

* Linux Fundamentals
* Git & GitHub
* Python Programming
* File Processing
* Data Parsing
* SQL & PostgreSQL
* Database Integration
* Analytics Engineering
* ETL Concepts

---

## Author

Harshal Prajapati


---

## License

This project is intended for educational, learning, and portfolio purposes.
