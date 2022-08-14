-- script that prepares a MySQL server --
-- Create DATABASE 'many_menu_db' --
CREATE DATABASE IF NOT EXISTS many_menu_db;

-- Add new user 'many_menu' in localhost --
-- User 'many_menu' password should be 'many_menu_pwd' --
CREATE USER IF NOT EXISTS 'many_menu'@'localhost' IDENTIFIED BY 'many_menu_pwd';

-- User 'many_menu' should have SELECT privileges on db 'performance_schema' --
GRANT SELECT ON performance_schema.* TO 'many_menu'@'localhost';

-- User 'many_menu' should have all privileges on db 'many_menu_db' --
GRANT ALL PRIVILEGES ON many_menu_db.* TO 'many_menu'@'localhost';
FLUSH PRIVILEGES;