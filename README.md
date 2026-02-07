# Cloud GCP Data Warehouse Automation

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-BigQuery-4285F4.svg)](https://cloud.google.com/bigquery)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade automation tool** for managing Google Cloud BigQuery data warehouses. This repository provides a Python-based interface for provisioning datasets, managing table schemas, and executing SQL jobs programmatically.

## 🚀 Features

- **Dataset Management**: Automated creation and configuration of BigQuery datasets.
- **Schema Enforcement**: definition of table schemas using JSON/Python objects.
- **Job Execution**: Programmatic execution of SQL queries and load jobs.
- **Access Control**: Management of dataset IAM policies (mock/wrapper).
- **Type Safety**: Fully typed Python codebase.

## 📁 Project Structure

```
cloud-gcp-data-warehouse-automation/
├── src/
│   ├── dw_automation.py  # BigQuery management logic
│   └── main.py           # CLI Entrypoint
├── tests/
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/cloud-gcp-data-warehouse-automation.git

# Install
pip install -r requirements.txt

# Run CLI (Requires GCP Auth)
gcloud auth application-default login
python src/main.py create-dataset --dataset-id my_analytics_ds
```

## 📄 License

MIT License
