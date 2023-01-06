CREATE DATABASE dev_project;
CREATE USER gitpod WITH PASSWORD 'gitpod';
ALTER ROLE gitpod SET client_encoding TO 'utf8';
ALTER ROLE gitpod SET default_transaction_isolation TO 'read committed';
ALTER ROLE gitpod SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dev_project to gitpod;