-- Crea la tabla Unique_id con información id y name
-- id INT con el valor predeterminado 1 y debe ser único
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR (256));
