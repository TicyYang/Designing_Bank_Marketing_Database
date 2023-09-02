-- Create a Bank Marketing Database
DROP DATABASE IF EXISTS bank_marketing;
CREATE DATABASE bank_marketing
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;