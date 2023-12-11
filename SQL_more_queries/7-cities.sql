-- Crea la base de datos hbtn_0d_usa y la tabla cities con información id, state_id y name
-- id debe ser INT unique, auto generated, null y primary key
-- name VARCHAR(256) no puede ser null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	    id INT AUTO_INCREMENT UNIQUE NOT NULL,
	    state_id INT NOT NULL,
	    name VARCHAR(256) NOT NULL,
	    PRIMARY KEY (id),
	    FOREIGN KEY (state_id) REFERENCES states(id)
	);
