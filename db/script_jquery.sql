CREATE TABLE pacientes(
	id_pac varchar(50) NOT NULL PRIMARY KEY,
	nombre varchar(50) NOT NULL,
	telefono varchar(50),
	edad integer,
	eps varchar(50)
);
--
CREATE TABLE triajes(
	cod_tri integer NOT NULL PRIMARY KEY,
	descripcion varchar(50),
	prioridad integer
);
--
CREATE TABLE urgencias(
	cod_urg integer NOT NULL PRIMARY KEY,
	paciente varchar(50) REFERENCES pacientes(id_pac),
	triaje integer REFERENCES triajes(cod_tri),
	observacion varchar(200),
	fecha varchar(50),
	estado boolean
);
--
-- Datos de la tabla pacientes
INSERT INTO pacientes VALUES('1083986725', 'DAVID SANTIAGO LASSO', '3145832497', 25, 'COMFAMILIAR');
INSERT INTO pacientes VALUES('21703489', 'MARIA DEL CARMEN DELGADO', '3122823988', 57, 'EMSSANAR');
INSERT INTO pacientes VALUES('83478653', 'LEONARDO GUERRERO', '3159873783', 36, 'COMFAMILIAR');
INSERT INTO pacientes VALUES('1086435898', 'NATALIA MARCELA TORO', '3167923401', 21, 'EMSSANAR');
INSERT INTO pacientes VALUES('976537237', 'LINA MARIA GOMEZ', '3217438217', 14, 'EMSSANAR');
INSERT INTO pacientes VALUES('5211317', 'FRANCISCO JAVIER MUÑOZ', '3208745632', 63, 'COMFAMILIAR');
INSERT INTO pacientes VALUES('1002345892', 'ANGELA MARIA CHAVEZ', '3128329195', 27, 'EMSSANAR');
INSERT INTO pacientes VALUES('1086550266', 'CARLOS ANDRES TORO', '315694567', 24, 'SANITAS');
INSERT INTO pacientes VALUES('67849003', 'EIDER JAVIER TORO', '3104158937', 48, 'COOMEVA'); 
--
-- Datos de la tabla triajes
INSERT INTO triajes VALUES(1, 'Presenta un riesgo vital', 1);
INSERT INTO triajes VALUES(2, 'Pérdida de un miembro u órgano', 2);
INSERT INTO triajes VALUES(3, 'Examen complementario o tratamiento rápido', 3);
INSERT INTO triajes VALUES(4, 'Posibles complicaciones si no recibe atención', 4);
INSERT INTO triajes VALUES(5, 'No representan un riesgo evidente', 5);
--
-- Datos de la tabla urgencias
INSERT INTO urgencias VALUES(1, '1083986725', 1, 'Desangrado por herida con arma de fuego en su brazo derecho.', '05/11/17 03:36:25', true);
INSERT INTO urgencias VALUES(2, '1083986725', 2, 'Infección en herida de bala, en brazo derecho.', '20/11/17 14:20:02', true);
INSERT INTO urgencias VALUES(3, '1002345892', 4, 'Dificultad para respirar, ademas presenta fuerte tos', '15/01/18 10:36:46', true);
INSERT INTO urgencias VALUES(4, '1086550266', 3, 'Quemadura grado 2 en la espalda, generado par derramamiento de agua hirviendo.', '23/03/18 12:37:08', true);
INSERT INTO urgencias VALUES(5, '1086550266', 4, 'Intoxicación por alicoramiento, el paciente llego consiente.', '12/04/18 04:06:08', true);

