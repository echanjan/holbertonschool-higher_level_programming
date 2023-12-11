-- Crea usuerio user_0d_1
-- user_0d_1 debe tener todos los privilegios
-- La contraseña user_0d_1 debe establecerse en user_0d_1_pwd
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
