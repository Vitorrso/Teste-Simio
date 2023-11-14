CREATE DATABASE simian_db;
CREATE USER 'vitor'@'localhost' IDENTIFIED BY 'Vitor2807';
GRANT ALL PRIVILEGES ON simian_db.* TO 'vitor'@'localhost';
FLUSH PRIVILEGES;
