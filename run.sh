#!/bin/bash

# Usage: ./run.sh NUM_INSERTS

# Variáveis de Ambiente
USER=buffet
DATABASE=buffet
INSERT_OUT=inserts.sql
SCHEMA_PATH=schema.sql
ROLE_CHECK=`sudo su -- postgres -c "psql -c \"\du\""`
DATABASE_CHECK=`sudo su -- postgres -c "psql -c \"\l\""`

# Dependências
#sudo apt-get update && apt-get install -y build-essential python3 python3-dev apt-utils gnupg gnupg2 gnupg1 python3-psycopg2

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postgresql-10

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