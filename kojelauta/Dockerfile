FROM mariadb:latest

ADD sql/ /docker-entrypoint-initdb.d

ENV MYSQL_ROOT_PASSWORD test
ENV MYSQL_USER tballs
ENV MYSQL_PASSWORD big
ENV MYSQL_DATABASE tballs

EXPOSE 3306

CMD ["mysqld"]

