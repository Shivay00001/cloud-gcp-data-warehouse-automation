FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir google-cloud-bigquery python-dotenv

COPY . .

ENTRYPOINT ["python", "src/main.py"]