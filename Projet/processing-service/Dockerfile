FROM python:3.9-slim

WORKDIR /app

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