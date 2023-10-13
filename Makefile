# DOCKER
build:
	docker-compose build

up:
	docker-compose up -d

run:
	docker-compose up -d --build

down:
	docker-compose down -v

logs:
	docker-compose logs 

collectstatic:
	docker-compose exec web python manage.py collectstatic --no-input         

createsuperuser:
	docker-compose exec web python manage.py createsuperuser                                                                           

# GITHUB
push:
	git push -u origin master