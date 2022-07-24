FROM python:3.8.8
LABEL Davi Segundo
COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
ENTRYPOINT python src/processor.py