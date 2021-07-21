FROM python:3.7-alpine

WORKDIR /app

# Update et recupere git
RUN apk update \
 && apk add git

# Copie du depot
RUN git clone https://github.com/Groupe2filRouge/ProjetFilRouge.git && cd ProjetFilRouge &&  git checkout  poc

# Copie du fichier main.py

Run cp  ./ProjetFilRouge/poc/shared/app.py ./app.py
# RUN cp  ProjetFilRouge/poc/shared/requirements.txt .
Run cp  ./ProjetFilRouge/poc/shared/requirements.txt ./requirements.txt

# Suppression des dossiers inutiles
#RUN rm -r example-python/

# Copie du fichier des dependances
COPY requirements.txt .

# Installation des dependances
RUN pip install -r requirements.txt

# Copie du docker intermediaire vers le courant
COPY . .

# Suppression des fichiers inutiles
RUN rm requirements.txt Dockerfile

CMD ["python3", "app.py"]
