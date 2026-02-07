import argparse
import os
from dotenv import load_dotenv
from google.cloud import bigquery
from src.dw_automation import BigQueryManager

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="GCP Data Warehouse Automation")
    parser.add_argument("action", choices=["create-dataset", "create-table", "run-query"], help="Action to perform")
    parser.add_argument("--project-id", default=os.getenv("GCP_PROJECT_ID"), help="GCP Project ID")
    parser.add_argument("--dataset-id", help="Dataset ID")
    parser.add_argument("--table-id", help="Table ID")
    
    args = parser.parse_args()
    
    if not args.project_id:
        print("Error: Project ID must be provided via argument or GCP_PROJECT_ID env var.")
        return

    manager = BigQueryManager(args.project_id)

    try:
        if args.action == "create-dataset":
            if not args.dataset_id:
                print("Error: --dataset-id is required.")
                return
            manager.create_dataset(args.dataset_id)

        elif args.action == "create-table":
            if not args.dataset_id or not args.table_id:
                print("Error: --dataset-id and --table-id are required.")
                return
            
            # Sample schema
            schema = [
                bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
                bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
            ]
            manager.create_table(args.dataset_id, args.table_id, schema)

        elif args.action == "run-query":
            print("Running sample query...")
            # Query needs a valid table, so this is just mocked for CLI structure
            print("Query execution result placeholder.")

    except Exception as e:
        print(f"Operation failed: {e}")

if __name__ == "__main__":
    main()
