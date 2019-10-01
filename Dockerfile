#FROM alpine
#COPY quickstart.sh /
#CMD ["/quickstart.sh"]
FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip
    #pip install mysql-connector

RUN pip install mysql-connector

EXPOSE 80


















