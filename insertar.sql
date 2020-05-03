--insertar estados en la tabla estados
INSERT INTO estados (id, nombreEstado) VALUES(1, 'conectado');
INSERT INTO estados (id, nombreEstado) VALUES(2, 'ocupado');
INSERT INTO estados (id, nombreEstado) VALUES(3, 'ausente');
INSERT INTO estados (id, nombreEstado) VALUES(4, 'no disponible');
INSERT INTO estados (id, nombreEstado) VALUES(5, 'desconectado');

--insertar sedes en la tabla sedes
INSERT INTO sedes (id, nombreSede) VALUES(1, 'Lima Centro');
INSERT INTO sedes (id, nombreSede) VALUES(2, 'San Juan de Miraflores');
INSERT INTO sedes (id, nombreSede) VALUES(3, 'Ate');
INSERT INTO sedes (id, nombreSede) VALUES(4, 'San Juan de Lurigancho');



--insertar usuarios
INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(1, 'ricardo', 'gonzales', 'ricardo2020', 'ricardo@correo.com', '+51987456321', '1990-01-02', 'https://fotosbackend.s3.amazonaws.com/person1.jpeg', 'Front-End', 1, 1);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(2, 'paula', 'rodriguez', 'paula2020', 'paula@correo.com', '+51914523674', '1991-01-01', 'https://fotosbackend.s3.amazonaws.com/person2.jpeg', 'Front-End', 1, 1);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(3, 'jorge', 'gomez', 'jorge2020', 'jorge@correo.com', '+51932154682', '1992-02-02', 'https://fotosbackend.s3.amazonaws.com/person3.jpeg', 'Front-End', 5, 2);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(4, 'jose', 'vargaz', 'jose2020', 'jose@correo.com', '+51945672104', '1993-03-03', 'https://fotosbackend.s3.amazonaws.com/person4.jpeg', 'Back-End', 1, 2);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(5, 'luis', 'torres', 'luis2020', 'luis@correo.com', '+51999774512', '1994-04-04', 'https://fotosbackend.s3.amazonaws.com/person5.jpeg', 'Back-End', 1, 3);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(6, 'maria', 'ferrert', 'maria2020', 'maria@correo.com', '+51944521160', '1995-05-05', 'https://fotosbackend.s3.amazonaws.com/person6.jpeg', 'Front-End', 5, 3);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(7, 'lucas', 'torres', 'lucas2020', 'lucass@correo.com', '+51988451472', '1996-06-06', 'https://fotosbackend.s3.amazonaws.com/person7.jpeg', 'Front-End', 5, 4);



INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(8, 'carlos', 'rodas', 'carlos2020', 'carlos@correo.com', '+51933445168', '1997-07-07', 'https://fotosbackend.s3.amazonaws.com/person8.jpg', 'Front-End', 1, 1);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(9, 'juan miguel', 'garcia', 'juan2020', 'juan@correo.com', '+51966552184', '1998-08-08', 'https://fotosbackend.s3.amazonaws.com/person9.jpg', 'Diseño UX', 2, 2);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(10, 'alonso', 'ruiz', 'alonso2020', 'alonso@correo.com', '+51988445512', '1999-09-09', 'https://fotosbackend.s3.amazonaws.com/person10.jpg', 'Desarrollo de APPS', 3, 3);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(11, 'maicol', 'romero', 'maicol2020', 'maicol@correo.com', '+51933226641', '1995-10-10', 'https://fotosbackend.s3.amazonaws.com/person11.jpg', 'Back-end', 4, 4);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(12, 'felipe', 'aguilar', 'felipe2020', 'felipe@correo.com', '+51955116890', '1996-11-11', 'https://fotosbackend.s3.amazonaws.com/person12.jpg', 'Back-end', 1, 1);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(13, 'cesar', 'vega', 'cesar2020', 'cesar@correo.com', '+51988774456', '1995-12-19', 'https://fotosbackend.s3.amazonaws.com/person13.jpg', 'Front-end', 2, 2);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(14, 'anthony', 'carmona', 'anthony2020', 'anthony@correo.com', '+51966001163', '1994-10-12', 'https://fotosbackend.s3.amazonaws.com/person14.jpg', 'Diseño UX', 3, 3);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(15, 'dario', 'fernandez', 'dario2020', 'dario@correo.com', '+51900124151', '1998-02-12', 'https://fotosbackend.s3.amazonaws.com/person15.jpg', 'Desarrollo de APPS', 4, 4);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(16, 'sergio', 'tapia', 'sergio2020', 'sergio@correo.com', '+51941412573', '1997-03-25', 'https://fotosbackend.s3.amazonaws.com/person16.jpg', 'Front-end', 5, 1);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(17, 'teresa', 'zapata', 'teresa2020', 'teresa@correo.com', '+51977774561', '1998-05-20', 'https://fotosbackend.s3.amazonaws.com/person17.jpg', 'Back-end', 5, 2);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(18, 'carmen', 'martinez', 'carmen2020', 'carmen@correo.com', '+51984576215', '1995-08-20', 'https://fotosbackend.s3.amazonaws.com/person18.jpg', 'Diseño UX', 1, 3);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(19, 'andrea', 'alcantara', 'andrea2020', 'andrea@correo.com', '+51912457814', '1993-07-23', 'https://fotosbackend.s3.amazonaws.com/person19.jpg', 'Desarrollo de APPS', 1, 4);

INSERT INTO users
(id, nombre, apellido, password, email, movil, fechaNacimiento, foto, description, estado_id, sede_id)
VALUES(20, 'rosa', 'molina', 'rosa', 'rosa@correo.com', '+51966332540', '1998-03-30', 'https://fotosbackend.s3.amazonaws.com/person20.jpg', 'Desarrollo de APPS', 2, 2);

