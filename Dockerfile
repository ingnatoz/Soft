# By: Mike

FROM python:3.9
RUN apt-get update \
    && apt-get install -y --no-install-recommends
# Evita que Python escriba archivos pyc en el disco (equivalente a la python -B opción )
ENV PYTHONDONTWRITEBYTECODE 1
# Evita que Python almacene en búfer stdout y stderr (equivalente a la python -u opción )
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
RUN echo "START BASH"
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
RUN echo "END BASH"
#CMD python manage.py runserver 0.0.0.0:8000