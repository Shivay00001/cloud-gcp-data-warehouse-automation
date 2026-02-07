from google.cloud import bigquery
from google.api_core.exceptions import NotFound, Conflict
import logging

class BigQueryManager:
    def __init__(self, project_id: str):
        self.client = bigquery.Client(project=project_id)
        self.project_id = project_id

    def create_dataset(self, dataset_id: str, location: str = "US"):
        """Creates a new BigQuery dataset."""
        dataset_ref = f"{self.project_id}.{dataset_id}"
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = location
        
        try:
            dataset = self.client.create_dataset(dataset, timeout=30)
            print(f"Created dataset {self.project_id}.{dataset.dataset_id}")
            return dataset
        except Conflict:
            print(f"Dataset {dataset_id} already exists.")
            return self.client.get_dataset(dataset_ref)

    def create_table(self, dataset_id: str, table_id: str, schema: list):
        """Creates a table with a specific schema."""
        table_ref = f"{self.project_id}.{dataset_id}.{table_id}"
        table = bigquery.Table(table_ref, schema=schema)
        
        try:
            table = self.client.create_table(table)
            print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")
            return table
        except Conflict:
            print(f"Table {table_id} already exists.")
            return self.client.get_table(table_ref)

    def execute_query(self, query: str):
        """Executes a SQL query."""
        query_job = self.client.query(query)
        return query_job.result()
