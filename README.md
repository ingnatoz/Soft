<p align="center"><img src="https://miro.medium.com/max/724/1*lAMsvtB6afHwTQYCNM1xvw.png" width="600"></p>

# Parrot Soft

## Stack de Tecnologías de Desarrollo

- python >= 3.9 https://www.python.org/downloads, https://hub.docker.com/_/python/
- Django == 3.2.8    https://www.djangoproject.com
- Django Rest Framework == 3.12.4   https://www.django-rest-framework.org
- MySQL 5.7   https://registry.hub.docker.com/_/mysql


# 
## Intalación Docker
<p align="center"><img src="https://docs.docker.com/images/docker-docs-logo.svg" width="200"></p>

- Intrucciones
- 1.- Instalar https://docs.docker.com/desktop
- 2.- Instalar https://docs.microsoft.com/en-us/windows/wsl/install-win10
- 3.- Ejecutar en Consola: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
- En la aplicacion de Docker configurar el Resource ->Advance (subir recursos)  ->File Sharing  (poner la raiz de donde se encuentre el proyecto C:\ )

## Ejecución de Arquitectura local
- Ejecucion Arquitectura local: -$ docker-compose build --no-cache && docker-compose up -d && docker-compose restart -t 10 back && docker-compose exec back python manage.py makemigrations && docker-compose exec back python manage.py migrate && docker-compose restart back && docker-compose exec back python manage.py createsuperuser
- Acceder al contenedor Backend: -$ docker-compose exec back bash
- Ver los logs del Server con hora: -$ docker logs back  -f -t

## Pruebas Pytest
- docker-compose exec back pytest

## Administración de Django &&  Documentación && Redoc
- http://localhost/admin
- http://localhost/swagger
- http://localhost/redoc