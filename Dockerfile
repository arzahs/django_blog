FROM python:3.8-slim-buster
RUN apt-get update \
   && apt-get -y install gcc 
RUN pip install --upgrade pip \
 && pip install django==1.8.4
COPY . /app
WORKDIR /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
