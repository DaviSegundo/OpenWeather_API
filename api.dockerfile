FROM python:3.8.8
LABEL Davi Segundo
EXPOSE 5000
COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
ENTRYPOINT python src/main.py