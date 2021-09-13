# Image choisie
FROM python:3.9.6-alpine3.13

# Repertoire de travail
WORKDIR /app

# Update le container et recupere git
RUN apk update \
 && apk add git
 
# Optimisation
RUN apk add --no-cache gcc musl-dev linux-headers

# Copie du depot
RUN git clone https://github.com/Groupe2filRouge/AppFilRouge.git

# Copie des fichiers sources
RUN cp AppFilRouge/src/main/app.py .
RUN cp -r AppFilRouge/src/main/services .
RUN cp AppFilRouge/src/requirements.txt .

# Suppression des dossiers inutiles
RUN rm -r AppFilRouge/

# Installation des dependances
RUN pip install -r requirements.txt

# Copie du docker intermediaire vers le courant
COPY . .

# Suppression des fichiers inutiles
RUN rm requirements.txt

# Regle de "pare-feu" => on expose le port 5000 => - ports : - 5000:5000 dans le docker-compose
EXPOSE 5000

# Commande au run du container
CMD ["python3", "app.py"]
