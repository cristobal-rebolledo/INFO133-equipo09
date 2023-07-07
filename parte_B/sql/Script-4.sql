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
FK_ID_REGION smallint (6),
foreign key (FK_ID_REGION) references Region(PK_ID_REGION)
);

create table if not exists Bienestar(
PK_ID_INDICADOR smallint (6) primary key,
NOMBRE_INDICADOR varchar(100),
Descripcion varchar(300),
Categoria varchar(100),
FK_ID_COMUNA smallint (6),
foreign key (FK_ID_COMUNA) references Comuna(PK_ID_COMUNA)
);


create table if not exists Estadios(
    PK_NOMBRE_ESTADIO varchar(200),
    FK_COMUNA varchar(100),
    primary key (PK_NOMBRE_ESTADIO, FK_COMUNA),
    FK_ID_INDICADOR smallint(6),
    foreign key (FK_ID_INDICADOR) references Bienestar(PK_ID_INDICADOR)
);

create table if not exists CentrosMedicos(
    PK_NOMBRE_CENTRO varchar(200),
    FK_COMUNA varchar(100),
    PRIMARY KEY (PK_NOMBRE_CENTRO,FK_COMUNA),
    FK_ID_INDICADOR smallint(6),
    foreign key (FK_ID_INDICADOR) references Bienestar(PK_ID_INDICADOR)
);

create table if not exists Escuelas(
    PK_NOMBRE_ESCUELA varchar(200),
    FK_COMUNA varchar(100),
    primary key (PK_NOMBRE_ESCUELA, FK_COMUNA),
    FK_ID_INDICADOR smallint(6),
    foreign key (FK_ID_INDICADOR) references Bienestar(PK_ID_INDICADOR)
);
create table if not exists DMCS(
    PK_ID_COMUNA smallint (6) primary key,
    Tasa int,
    FK_ID_INDICADOR smallint (6),
    foreign key (FK_ID_INDICADOR) references Bienestar(PK_ID_INDICADOR),
    foreign key (PK_ID_COMUNA) references Comuna(PK_ID_COMUNA)
);

