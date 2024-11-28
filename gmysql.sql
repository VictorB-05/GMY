DROP DATABASE IF EXISTS gmy;
CREATE DATABASE gmy;
USE gmy;

CREATE TABLE usuario(
	dni VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(10),
    apellidos VARCHAR(15),
    pago BOOLEAN DEFAULT TRUE,
    moroso BOOLEAN DEFAULT FALSE,
    privilegios BOOLEAN DEFAULT FALSE);
    
CREATE TABLE aparato(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(25));
    
CREATE TABLE reservas(
	id INT PRIMARY KEY AUTO_INCREMENT,
	dni VARCHAR(10),
    id_aparato INT,
    dia INT(1),
    hora TIME,
    FOREIGN KEY (dni) REFERENCES usuario(dni) ON DELETE CASCADE,
    FOREIGN KEY (id_aparato) REFERENCES aparato(id) ON DELETE CASCADE);
    
INSERT INTO usuario (dni, nombre, apellidos, pago, moroso)
VALUES 
('123456789A', 'Juan', 'Pérez', TRUE, FALSE),
('987654321B', 'María', 'García', TRUE, FALSE),
('456123789C', 'Carlos', 'López', FALSE, TRUE),
('654987321D', 'Ana', 'Martínez', TRUE, FALSE),
('321654987E', 'Elena', 'Sánchez', FALSE, TRUE);

INSERT INTO aparato (nombre)
VALUES 
('Bicicleta Estática'),
('Cinta de Correr'),
('Máquina de Pesas'),
('Elíptica'),
('Remo');

INSERT INTO reservas (dni, id_aparato, dia, hora)
VALUES 
('123456789A', 1, 1, '09:00:00'),
('987654321B', 2, 1, '10:00:00'),
('456123789C', 3, 1, '11:00:00'),
('654987321D', 4, 1, '12:00:00'),
('321654987E', 5, 1, '13:00:00'),

('123456789A', 3, 2, '09:30:00'),
('987654321B', 1, 2, '10:30:00'),
('456123789C', 4, 2, '11:30:00'),
('654987321D', 2, 2, '12:30:00'),
('321654987E', 5, 2, '13:30:00'),

('123456789A', 2, 3, '09:00:00'),
('987654321B', 3, 3, '10:00:00'),
('456123789C', 5, 3, '11:00:00'),
('654987321D', 1, 3, '12:00:00'),
('321654987E', 4, 3, '13:00:00'),

('123456789A', 4, 4, '09:30:00'),
('987654321B', 5, 4, '10:30:00'),
('456123789C', 1, 4, '11:30:00'),
('654987321D', 3, 4, '12:30:00'),
('321654987E', 2, 4, '13:30:00'),

('123456789A', 5, 5, '09:00:00'),
('987654321B', 1, 5, '10:00:00'),
('456123789C', 2, 5, '11:00:00'),
('654987321D', 4, 5, '12:00:00'),
('321654987E', 3, 5, '13:00:00');

-- Admin
INSERT INTO usuario (dni, nombre, apellidos, pago, moroso,privilegios)
VALUES 
('39114963J', 'Pepe', 'Jimenez Ordoñez', TRUE, FALSE,TRUE);