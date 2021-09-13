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
RUN cp -r ./AppFilRouge/src/main/* .
RUN cp  ./AppFilRouge/src/requirements.txt ./requirements.txt

# Suppression des fichiers devenus inutiles
RUN rm -r AppFilRouge

# Installation des dependances
RUN pip install -r requirements.txt

# Copie du docker intermediaire vers le courant
COPY . .

# Definition du path pour python
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Commande au run du container
CMD ["python3", "app.py"]
