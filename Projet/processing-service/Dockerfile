FROM python:3.9-slim

WORKDIR /app

# Installer curl pour les health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY *.py ./

# Exposer le port 5002
EXPOSE 5002

# Démarrer le serveur Flask
CMD ["python", "app.py"]