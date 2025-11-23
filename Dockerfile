# Image Python minimale
FROM python:3.10-slim

# Dossier de travail
WORKDIR /app

# Copier fichiers dans le conteneur
COPY requirements.txt .
COPY app.py .

# Installer dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande exécutée au démarrage du conteneur
CMD ["python", "app.py"]
