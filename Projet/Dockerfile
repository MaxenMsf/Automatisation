FROM python:3.9-slim

WORKDIR /app

# Installer curl pour les health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copier le fichier principal app.py
COPY app.py .
COPY database.db .

EXPOSE 5001

CMD ["python", "app.py"]