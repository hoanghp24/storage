## 1.  BUILD PROJECT:
Firstly, you need to install Docker on your local enviroment: `https://docs.docker.com/get-docker/`

At root of project, you folow below commands step by step:
```sh
$ docker-compose up -d --build
```
New terminal, and then:
```sh
$ docker-compose exec web python manage.py collectstatic --no-input
```
```sh
$ docker-compose exec web python manage.py createsuperuser
```

That's all !! You can access `http://localhost:8080` on browser to see the web view.

## 2.  If you need a shell, run:
```sh
$ docker-compose exec web python manage.py shell
```

## 3. Access to the container, run:
```sh
$ docker ps 
```
```sh
$ docker exec -it containerID sh
```

## 4. To check the logs out, run:
```sh
$ docker-compose logs
```

## 5. Restart app
```sh
docker-compose restart web db
```

## 6. Project structure
```sh
├── .envs
│    ├── .django
│    └── .postgres
├── nginx
│    ├── Dockerfile
│    └── nginx.conf
├── src
│   ├── app
│   │   ├── apis
│   │   ├── helpers
│   │   ├── migrations
│   │   ├── models
│   │   ├── routes
│   │   ├── serializers
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── querydb.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   └── urls.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── static
│   ├── templates
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── manage.py
│   └── requirements.txt
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Jenkinsfile
├── Makefile
└── README.md

```
