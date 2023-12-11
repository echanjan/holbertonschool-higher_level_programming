-- Crea la base de datos hbtn_0d_usa y la tabla state con información id y name
-- id debe ser INT unique, auto generated, null y primary key
-- name VARCHAR(256) no puede ser null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(256) NOT NULL);
