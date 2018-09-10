docker volume create --name=db_data
docker-compose build web
docker-compose up -d
docker exec -i -t flota_web_1 /bin/bash