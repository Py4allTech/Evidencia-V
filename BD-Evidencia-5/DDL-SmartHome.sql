-- Crear base de datos
CREATE DATABASE IF NOT EXISTS smarthome; 

-- Usar la base de datos
USE smarthome;


-- Tabla: role
-- Almacena los roles disponibles en el sistema
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla: state
-- Estados posibles para los dispositivos
CREATE TABLE state (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE       
); 

-- Tabla: location
-- Ubicaciones/habitaciones en los hogares
CREATE TABLE location (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL  
);

-- Tabla: device_type
-- Tipos de dispositivos disponibles
CREATE TABLE device_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    characteristic TEXT
);
