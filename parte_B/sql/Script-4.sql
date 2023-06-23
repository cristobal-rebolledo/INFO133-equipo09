create database IF NOT exists bienestar;
use bienestar;
 
create table if not exists Pais(
PK_NOMBRE_PAIS varchar(30) primary key
);

create table if not exists Region(
PK_NOMBRE_REGION varchar(100) primary key,
FK_NOMBRE_PAIS varchar(30),
foreign key (FK_NOMBRE_PAIS) references Pais(PK_NOMBRE_PAIS)
);

create table if not exists Comuna(
PK_NOMBRE_COMUNA varchar(100) primary key,
FK_NOMBRE_REGION varchar(100),
foreign key (FK_NOMBRE_REGION) references Region(PK_NOMBRE_REGION)
);

create table if not exists Bienestar(
PK_NOMBRE_INDICADOR varchar(100) primary key,
Descripcion varchar(300),
Categoria varchar(100)
);


create table if not exists Tener(
PK_ID smallint unsigned auto_increment primary key,
Valor int,
FK_NOMBRE_COMUNA varchar(100),
FK_NOMBRE_INDICADOR varchar(100),
foreign key (FK_NOMBRE_COMUNA) references Comuna(PK_NOMBRE_COMUNA),
foreign key (FK_NOMBRE_INDICADOR) references Bienestar(PK_NOMBRE_INDICADOR)
);
create table if not exists Estadios(
    PK_NOMBRE_ESTADIO varchar(100),
    FK_COMUNA varchar(100),
    primary key (PK_NOMBRE_ESTADIO, FK_COMUNA),
    FK_NOMBRE_INDICADOR varchar(100),
    foreign key (FK_NOMBRE_INDICADOR) references Bienestar(PK_NOMBRE_INDICADOR)
);

create table if not exists CentrosMedicos(
    PK_NOMBRE_CENTRO varchar(100),
    FK_COMUNA varchar(100),
    PRIMARY KEY (PK_NOMBRE_CENTRO,FK_COMUNA),
    FK_NOMBRE_INDICADOR varchar(100),
    foreign key (FK_NOMBRE_INDICADOR) references Bienestar(PK_NOMBRE_INDICADOR)
);

create table if not exists Escuelas(
    PK_NOMBRE_ESCUELA varchar(100),
    FK_COMUNA varchar(100),
    primary key (PK_NOMBRE_ESCUELA, FK_COMUNA),
    FK_NOMBRE_INDICADOR varchar(100),
    foreign key (FK_NOMBRE_INDICADOR) references Bienestar(PK_NOMBRE_INDICADOR)
);
