FROM gitpod/workspace-full

USER root

# Install MySQL server and client
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Fix socket directory issue
RUN mkdir -p /var/run/mysqld && \
    chown -R mysql:mysql /var/run/mysqld && \
    chmod 755 /var/run/mysqld

# Pre-create DB and password setup
RUN service mysql start && \
    mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'; FLUSH PRIVILEGES;" && \
    mysql -uroot -p123456 -e "CREATE DATABASE employee_db;"

EXPOSE 3306
