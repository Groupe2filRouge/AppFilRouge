FROM python:3.9.6-alpine3.13

WORKDIR /app

# Update et recupere git
RUN apk update \
 && apk add git

# Copie du depot
RUN git clone https://github.com/Groupe2filRouge/AppFilRouge.git

# Copie du fichier main.py

Run cp -r ./AppFilRouge/src/main/* .
Run cp  ./AppFilRouge/src/requirements.txt ./requirements.txt
Run rm -r AppFilRouge

# Installation des dependances
RUN pip install -r requirements.txt

# Copie du docker intermediaire vers le courant
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python3", "app.py"]
