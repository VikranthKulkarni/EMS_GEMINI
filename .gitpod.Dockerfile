FROM gitpod/workspace-full

USER root

# Install MySQL server
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server && \
    rm -rf /var/lib/apt/lists/*

# Set up MySQL root password and create database
RUN service mysql start && \
    mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'; FLUSH PRIVILEGES;" && \
    mysql -uroot -p123456 -e "CREATE DATABASE employee_db;"

# Expose port for MySQL
EXPOSE 3306
