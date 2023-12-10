-- Enumera la cantidad de registros en con mismo score en table second_table
SELECT score, COUNT (score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
