#!/bin/bash

# Usage: ./run.sh NUM_INSERTS

# Variáveis de Ambiente
USER=buffet
DATABASE=buffet
INSERT_OUT=inserts.sql
SCHEMA_PATH=schema.sql
ROLE_CHECK=`sudo su -- postgres -c "psql -c \"\du\""`
DATABASE_CHECK=`sudo su -- postgres -c "psql -c \"\l\""`
UBUNTU_VERSION=xenial # or bionic or trusty

# Dependências
sudo apt-get update && apt-get install -y build-essential python3 python3-dev apt-utils gnupg gnupg2 gnupg1 python3-psycopg2

#apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``10``.
sudo add-apt-repository 'http://apt.postgresql.org/pub/repos/apt/xenial-pgdg main'

sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update && apt-get install -y postgresql-10

# Checa se o usuário tem os privilégios necessários
if echo "$ROLE_CHECK" | grep -q "$USER"; then
	echo "Usuário \"$USER\" OK. Criando o database $DATABASE..."
else
	echo "Definindo permissões para o usuário \"$USER\"..."
	sudo su -- postgres -c "psql -c \"CREATE ROLE $USER WITH PASSWORD 'buffet01';\"" && \
	sudo su -- postgres -c "psql -c \"ALTER ROLE $USER SUPERUSER;\"" && \
	sudo su -- postgres -c "psql -c \"ALTER ROLE $USER LOGIN;\"" && \
	echo "Criando o database $DATABASE..."
fi

# Checa se o database já existe na base de dados
if echo "$DATABASE_CHECK" | grep -q "$DATABASE"; then	
	sudo su -- postgres -c "psql -c \"DROP DATABASE $DATABASE;\""
fi

# Criando o database do zero
sudo su -- postgres -c "psql -c \"CREATE DATABASE $DATABASE OWNER $USER;\"" && \

# Criando a estrutura do banco de dados
echo "Criando a estrutura de $DATABASE..."
psql $DATABASE < $SCHEMA_PATH #&& \

# Alimentando o banco de dados com os inserts
echo "Alimentando $DATABASE com os inserts gerados..."
psql $DATABASE < $INSERT_OUT