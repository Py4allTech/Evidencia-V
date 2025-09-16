INSERT INTO role (id, name) VALUES 
(1, 'Administrador'),
(2, 'Usuario'),
(3, "Visita");

-- Consulta simple para role: Muestra todos los roles disponibles en el sistema
SELECT * FROM role;


INSERT INTO state (id, name) VALUES
(1, 'Encendido'),
(2, 'Apagado'),
(3, 'En Mantenimiento'),
(4, 'Error'),
(5, 'Standby'),
(6, 'Configurando');

-- Consulta simple para state: Busca todos los estados que contengan "En" en su nombre
SELECT * FROM state WHERE name LIKE '%En%';


INSERT INTO location (id, name) VALUES
(1, 'Sala de Estar'),
(2, 'Cocina'),
(3, 'Dormitorio Principal'),
(4, 'Dormitorio Secundario'),
(5, 'Baño'),
(6, 'Garaje'),
(7, 'Jardín'),
(8, 'Oficina');

-- Consulta simple para location: Filtra ubicaciones que contengan "Dormitorio" en el nombre
SELECT id, name FROM location WHERE name LIKE '%Dormitorio%';


INSERT INTO device_type (id, name, characteristic) VALUES
(1, 'Luz Inteligente', 'Iluminación LED controlable'),
(2, 'Termostato', 'Control de temperatura'),
(3, 'Ventilador', 'Circulación de aire'),
(4, 'Cerradura Inteligente', 'Control de acceso'),
(5, 'Cámara de Seguridad', 'Vigilancia remota'),
(6, 'Sensor de Movimiento', 'Detección de presencia');

-- Consulta simple para device_type: Busca tipos de dispositivos "Inteligentes" con sus características
SELECT name, characteristic FROM device_type WHERE name LIKE '%Inteligente%';


INSERT INTO home (id, name) VALUES
(1, 'Casa Principal'),
(2, 'Casa de Campo'),
(3, 'Departamento');

-- Consulta simple para home: Lista todos los hogares ordenados alfabéticamente por nombre
SELECT * FROM home ORDER BY name;


INSERT INTO user (email, password, name, role_id) VALUES
('fernandomoyano21@gmail.com', '$2b$12$hash1', 'Fernando Moyano', 1),
('santiagoortega@gmail.com', '$2b$12$hash2', 'Santiago Ortega', 2),
('rafaelperazzolo@gmail.com', '$2b$12$hash3', 'Rafael Perazzolo', 2),
('maria.garcia@ejemplo.com', '$2b$12$hash4', 'María García', 2),
('invitado@smarthome.com', '$2b$12$hash5', 'Usuario Invitado', 3);

-- Consulta simple para user: Muestra usuarios que tienen rol de "Usuario" (role_id = 2)
SELECT email, name, role_id FROM user WHERE role_id = 2;


INSERT INTO user_home (user_email, home_id) VALUES
('fernandomoyano21@gmail.com', 1),
('fernandomoyano21@gmail.com', 2),
('santiagoortega@gmail.com', 2),
('rafaelperazzolo@gmail.com', 3),
('maria.garcia@ejemplo.com', 1),
('invitado@smarthome.com', 1);

-- Consulta simple para user_home: Lista qué usuarios tienen acceso a la "Casa Principal" (home_id = 1)
SELECT user_email, home_id FROM user_home WHERE home_id = 1;


INSERT INTO device (name, state_id, device_type_id, location_id, home_id) VALUES
-- Casa Principal
('Luz Principal Sala', 1, 1, 1, 1),
('Termostato Central', 2, 2, 1, 1),
('Ventilador Techo Sala', 1, 3, 1, 1),
('Luz Cocina Principal', 1, 1, 2, 1),
('Luz Bajo Muebles', 2, 1, 2, 1),
('Cerradura Principal', 1, 4, 1, 1),
('Cámara Entrada', 1, 5, 1, 1),
('Luz Dormitorio', 2, 1, 3, 1),
('Ventilador Dormitorio', 2, 3, 3, 1),
('Sensor Movimiento', 1, 6, 3, 1),
-- Casa de Campo
('Luz Oficina Campo', 2, 1, 8, 2),
('Termostato Campo', 1, 2, 1, 2),
('Cámara Jardín', 1, 5, 7, 2),
('Luz Jardín', 1, 1, 7, 2),
('Sensor Garaje', 1, 6, 6, 2),
('Ventilador Garaje', 2, 3, 6, 2),
('Luz Baño Campo', 2, 1, 5, 2),
('Cerradura Garaje', 1, 4, 6, 2),
('Cámara Entrada Campo', 1, 5, 1, 2),
('Luz Dormitorio Campo', 2, 1, 4, 2),
-- Departamento
('Luz Principal Depto', 1, 1, 1, 3),
('Termostato Mini', 2, 2, 1, 3),
('Cámara Seguridad', 1, 5, 1, 3),
('Cerradura Depto', 1, 4, 1, 3),
('Sensor Ventana', 1, 6, 1, 3);

-- Consulta simple para device: JOIN complejo que muestra dispositivos de tipo "Luz" en "Casa Principal" con todos sus detalles
SELECT d.name, s.name as estado, dt.name as tipo, l.name as ubicacion, h.name as hogar
FROM device d 
JOIN state s ON d.state_id = s.id
JOIN device_type dt ON d.device_type_id = dt.id
JOIN location l ON d.location_id = l.id
JOIN home h ON d.home_id = h.id
WHERE h.name = 'Casa Principal' AND dt.name LIKE '%Luz%';


INSERT INTO automation (name, description, active, home_id) VALUES
('Encender Luces Salón', 'Enciende luces del salón', TRUE, 1),
('Apagar Todas Luces', 'Apaga toda la iluminación', TRUE, 1),
('Modo Nocturno', 'Configuración nocturna', TRUE, 1),
('Seguridad Campo', 'Activa cámaras y sensores', TRUE, 2),
('Llegada a Casa', 'Luces de bienvenida', TRUE, 2),
('Ahorro Energía', 'Optimiza consumo', TRUE, 3),
('Ventilación Auto', 'Control automático', FALSE, 1);

-- Consulta simple para automation: Muestra todas las automatizaciones activas con el nombre del hogar donde están configuradas
SELECT a.name, a.description, a.active, h.name as hogar
FROM automation a
JOIN home h ON a.home_id = h.id
WHERE a.active = TRUE;


INSERT INTO device_automation (device_id, automation_id, action) VALUES
(1, 1, 'set_state'), (4, 1, 'set_state'),
(1, 2, 'set_state'), (4, 2, 'set_state'), (5, 2, 'set_state'), (8, 2, 'set_state'),
(1, 3, 'set_state'), (2, 3, 'set_state'), (8, 3, 'set_state'),
(13, 4, 'set_state'), (15, 4, 'set_state'), (19, 4, 'set_state'),
(14, 5, 'set_state'), (11, 5, 'set_state'), (18, 5, 'toggle');

-- Consulta simple para device_automation: Muestra qué dispositivos están asociados a la automatización "Modo Nocturno" y qué acción realizan
SELECT d.name as dispositivo, a.name as automatizacion, da.action
FROM device_automation da
JOIN device d ON da.device_id = d.id
JOIN automation a ON da.automation_id = a.id
WHERE a.name = 'Modo Nocturno';


INSERT INTO event (description, device_id, user_email, source) VALUES
('Login Fernando', NULL, 'fernandomoyano21@gmail.com', 'user_action'),
('Luz Sala cambió estado', 1, 'fernandomoyano21@gmail.com', 'user_action'),
('Automatización ejecutada', NULL, 'fernandomoyano21@gmail.com', 'automation'),
('Termostato ajustado', 2, 'santiagoortega@gmail.com', 'user_action'),
('Cámara activada', 7, 'fernandomoyano21@gmail.com', 'user_action'),
('Modo nocturno ejecutado', NULL, 'maria.garcia@ejemplo.com', 'automation'),
-- Nuevos eventos ficticios agregados
('Sensor de movimiento detectó actividad', 10, NULL, 'device_trigger'),
('Cerradura inteligente abierta remotamente', 6, 'rafaelperazzolo@gmail.com', 'user_action'),
('Sistema de seguridad activado automáticamente', 13, NULL, 'automation'),
('Ventilador de dormitorio programado para apagarse', 9, 'maria.garcia@ejemplo.com', 'user_action'),
('Error de conexión detectado en termostato', 22, NULL, 'system_error');

-- Consulta simple para event: Muestra eventos realizados por usuarios (user_action), incluyendo dispositivo involucrado, ordenados por fecha más reciente
SELECT e.description, e.date_time_value, d.name as dispositivo, e.user_email, e.source
FROM event e
LEFT JOIN device d ON e.device_id = d.id
WHERE e.source = 'user_action'
ORDER BY e.date_time_value DESC;
