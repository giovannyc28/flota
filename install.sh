docker volume create --name=db_data
docker-compose build web
docker-compose up -d
docker exec -i flota_web_1 python manage.py migrate auth
docker exec -i flota_web_1 python manage.py migrate
docker exec -i -t flota_web_1 python manage.py createsuperuser

		