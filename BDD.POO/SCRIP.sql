create table Lunes (
 id serial primary key,
 actividad varchar(255)not null
);
insert into Lunes (actividad) values ('Clase de base de datos');
select * from Lunes

create table Marte (
id serial primary key,
actividad varchar(255)not null
);
insert into Marte(actividad) values ('Clase de socioeconomica cultural y ambiental');

create table Miercoles(
id serial primary key,
actividad varchar(255)not null
);
insert into  Miercoles(actividad) values ('Clases de Metodologia de desarrollo de software');

create table Jueves (
id serial primary key,
actividad varchar(255)not null,
observacion text
);
insert into Jueves (Actividad,observacion) Values ('Clases de Estadistica','Revisar las notas de Estadistica');
select * from Lunes
