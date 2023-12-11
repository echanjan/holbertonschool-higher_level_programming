-- Crea la base de datos hbtn_0d_2
-- La contraseña user_0d_2 debe establecerse en user_0d_2_pwd
-- user_0d_2 solo debe tener privilegio SELECT en la base de datos hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
