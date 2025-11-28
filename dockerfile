### Dockerfile ###

# Utiliser une image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y gcc musl-dev && rm -rf /var/lib/apt/lists/*


# Copier les fichiers nécessaires
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers après l'installation des dépendances
COPY . /app

# Exposer le port 5000
EXPOSE 5000

# Supprimer la base de données existante à chaque redémarrage et lancer l'application Flask en mode production
CMD ["/bin/sh", "-c", "flask run --host=0.0.0.0 --port=5000"]
