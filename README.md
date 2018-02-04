## impulsive
# Django Based project 

### How to start

- git clone https://github.com/Sonatrix/impulsive.git
- cd backend && pip3 install -r requirements.txt
- python3 manage.py runserver

### setup db conection postgresql
- sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common

### run command to create database
1. sudo -u postgres createdb creditunited psql
2. CREATE ROLE django WITH LOGIN PASSWORD '12345';
3. GRANT ALL PRIVILEGES ON DATABASE creditunited TO django;
4. ALTER ROLE django SET client_encoding TO 'utf8';
5. ALTER ROLE django SET default_transaction_isolation TO 'read committed';
6. ALTER ROLE django SET timezone TO 'UTC';



Application will start at localhost:8000
