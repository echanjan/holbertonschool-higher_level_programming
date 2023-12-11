-- Crea la base de datos hbtn_0d_usa y la tabla cities con información id, state_id y name
-- id debe ser INT unique, auto generated, null y primary key
-- name VARCHAR(256) no puede ser null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT NOT NULL FOREING KEY (state_id) REFERENCES states(states_id), name VARCHAR(256) NOT NULL);
