

--insertar sedes en la tabla sedes
INSERT INTO sedes (id, nombreSede) VALUES(1, 'Lima Centro');
INSERT INTO sedes (id, nombreSede) VALUES(2, 'San Juan de Miraflores');
INSERT INTO sedes (id, nombreSede) VALUES(3, 'Ate');
INSERT INTO sedes (id, nombreSede) VALUES(4, 'San Juan de Lurigancho');

--insertar estados en la tabla estados
INSERT INTO estados (id, nombreEstado) VALUES(1, 'activo');
INSERT INTO estados (id, nombreEstado) VALUES(2, 'inactivo');

--insertar usuarios
INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(1, 'ricardo', 'gonzales', 'ricardo2020', 'ricardo@correo.com', '+51987456321', '1990-01-02', 'https://fotosbackend.s3.amazonaws.com/person1.jpeg', 'Front-End', 1, 1);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(2, 'paula', 'rodriguez', 'paula2020', 'paula@correo.com', '+51914523674', '1991-01-01', 'https://fotosbackend.s3.amazonaws.com/person2.jpeg', 'Front-End', 1, 1);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(3, 'jorge', 'gomez', 'jorge2020', 'jorge@correo.com', '+51932154682', '1992-02-02', 'https://fotosbackend.s3.amazonaws.com/person3.jpeg', 'Front-End', 1, 2);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(4, 'jose', 'vargaz', 'jose2020', 'jose@correo.com', '+51945672104', '1993-03-03', 'https://fotosbackend.s3.amazonaws.com/person4.jpeg', 'Back-End', 1, 2);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(5, 'luis', 'torres', 'luis2020', 'luis@correo.com', '+51999774512', '1994-04-04', 'https://fotosbackend.s3.amazonaws.com/person5.jpeg', 'Back-End', 1, 3);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(6, 'maria', 'ferrert', 'maria2020', 'maria@correo.com', '+51944521160', '1995-05-05', 'https://fotosbackend.s3.amazonaws.com/person6.jpeg', 'Front-End', 1, 3);
		
INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(7, 'lucas', 'torres', 'lucas2020', 'lucass@correo.com', '+51988451472', '1996-06-06', 'https://fotosbackend.s3.amazonaws.com/person7.jpeg', 'Front-End', 1, 4);
