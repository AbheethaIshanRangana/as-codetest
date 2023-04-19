# Wordpress Blog Development

|File Name|Description|Content|
|-|-|-|
|docker-compose.yml|Docker compose file to deploy wordpress website|docker-compose services. (database, wordpress, phpmyadmin)|
|.env|.env file to pass variables to docker-compose file|environment variables. (MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, WORDPRESS_DB_USER, WORDPRESS_DB_PASSWORD, WORDPRESS_DB_NAME)|

## Pre-requisites
* <b>Docker</b> <br> 
Docker is a platform for building, shipping, and running applications using containerization. You can download and install Docker for your operating system from the official Docker website: https://www.docker.com/get-started.
* <b>Docker Compose</b> <br>
Docker Compose is a tool for defining and running multi-container Docker applications. You can install Docker Compose using the instructions provided on the official Docker Compose documentation: https://docs.docker.com/compose/install/.

## How to deploy the stack
Set all the environment variables in .env file
```
MYSQL_ROOT_PASSWORD: Pass@M0rb
MYSQL_DATABASE: blog
MYSQL_USER: wpuser
MYSQL_PASSWORD: wppassword

WORDPRESS_DB_USER: wpuser
WORDPRESS_DB_PASSWORD: wppassword
WORDPRESS_DB_NAME: blog
```
Execute below command
```
# docker-compose up -d
```

## How to delete the stack
Execute below command
```
# docker-compose down
```