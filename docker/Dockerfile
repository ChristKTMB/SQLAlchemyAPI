# Utilisation de l'image Python 3.12.3 basée sur Alpine Linux
FROM python:3.12.3-alpine

# Définition du répertoire de travail
WORKDIR /app

# Copie du fichier requirements.txt depuis le répertoire "src" vers /app/
COPY ../requirements.txt /app/

# Copie de tous les fichiers depuis le répertoire "src" vers /app/ dans le conteneur
COPY ../ /app/

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application écoute
EXPOSE 5000

# Commande d'exécution de l'application
CMD [ "python", "main.py" ]
