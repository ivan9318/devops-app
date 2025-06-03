FROM python:latest
WORKDIR /myapp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Comando para iniciar Flask
CMD ["flask", "run"]