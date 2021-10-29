# By: Mike
FROM python:3.9
# Evita que Python escriba archivos pyc en el disco (equivalente a la python -B opción )
ENV PYTHONDONTWRITEBYTECODE 1
# Evita que Python almacene en búfer stdout y stderr (equivalente a la python -u opción )
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app

#CMD python manage.py migrate
#CMD python manage.py makemigrations
#CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000