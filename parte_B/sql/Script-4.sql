create database IF NOT exists bienestar;
use bienestar;
 
create table if not exists Pais(
PK_ID_PAIS SMALLINT(6) primary key,
Nombre_Pais varchar(30)
);

create table if not exists Region(
PK_ID_REGION SMALLINT(6) primary key,
NOMBRE_REGION varchar(100) ,
FK_ID_PAIS smallint (6),
foreign key (FK_ID_PAIS) references Pais(PK_ID_PAIS)
);

create table if not exists Comuna(
PK_ID_COMUNA smallint (6) primary key,
NOMBRE_COMUNA varchar(100),
POBLACION INT (32),
DMCS FLOAT (32),
FK_ID_REGION smallint (6),
foreign key (FK_ID_REGION) references Region(PK_ID_REGION)
);

create table if not exists Estadios(
	PK_ID_ESTADIO smallint unsigned auto_increment primary key,
    NOMBRE_ESTADIO varchar(200),
    FK_ID_COMUNA smallint (6),
    foreign key (FK_ID_COMUNA) references COMUNA(PK_ID_COMUNA)
);

create table if not exists CentrosMedicos(
	PK_ID_CENTRO smallint unsigned auto_increment primary key,
    NOMBRE_CENTRO varchar(200),
    FK_ID_COMUNA smallint (6),
    foreign key (FK_ID_COMUNA) references COMUNA(PK_ID_COMUNA)
);

create table if not exists Escuelas(
	PK_ID_ESCUELA smallint unsigned auto_increment primary key,
    NOMBRE_ESCUELA varchar(200),
    FK_ID_COMUNA smallint (6),
    foreign key (FK_ID_COMUNA) references COMUNA(PK_ID_COMUNA)
);

