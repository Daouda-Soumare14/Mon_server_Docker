# Projet DevOps - Serveur HTTP avec Docker

## Prérequis
- Docker installé
- Docker Compose installé

### Exécution sans Docker Compose
```sh
docker build -t mon_serveur : pour la creation de l'image

docker run -d -p 8000:8000 mon_serveur : pour lancer le 
    server -d pour eviter que le terminal se bloc
```

### Exécution avec Docker Compose
```sh
docker-compose up --build : demarrer avec docker compose

docker-compose down : arreter avec docker compose
```

## Déploiement sur DockerHub
```sh
docker login : pour se connecter a dockerhub

docker tag mon_serveur daoudasoumare/mon_serveur:v1.0 
    Le tag sert à identifier clairement mon image Docker et permet de :
    Différencier plusieurs versions d’une même application (ex: v1.0, latest, v2.1)
    Associer l’image à mon compte DockerHub
    Faciliter le téléchargement et la gestion des versions

docker push daoudasoumare/mon_serveur:v1.0 : Le push permet d’envoyer mon image Docker vers DockerHub pour qu’elle soit accessible depuis n’importe quelle machine.

docker pull daoudasoumare/mon_serveur:v1.0 : Cela me permet d'exécuter l'application sans avoir besoin de son code source.

docker run -p 8000:8000 daoudasoumare/mon_serveur:v1.0
    docker run → Démarre un conteneur à partir de l’image Docker
    -p 8000:8000 → Lie le port 8000 du conteneur au port 8000 de ma machine
    daoudasoumare/mon_serveur:v1.0 → Spécifie l’image à utiliser avec mon nom d’utilisateur DockerHub

