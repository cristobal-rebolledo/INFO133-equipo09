create database IF NOT exists bienestar;
use bienestar;
 
create table if not exists Pais(
PK_ID_PAIS smallint unsigned auto_increment primary key,
Nombre varchar(30)
);

create table if not exists Region(
PK_ID_REGION smallint unsigned auto_increment primary key,
Nombre varchar(100),
FK_ID_PAIS smallint unsigned,
foreign key (FK_ID_PAIS) references Pais(PK_ID_PAIS)
);

create table if not exists Comuna(
PK_ID_COMUNA smallint unsigned auto_increment primary key,
Nombre varchar(100),
FK_ID_REGION smallint unsigned,
foreign key (FK_ID_REGION) references Region(PK_ID_REGION)
);

create table if not exists Bienestar(
PK_NOMBRE_INDICADOR varchar(100) primary key,
Descripcion varchar(300),
Categoria varchar(100)
);


create table if not exists Tener(
PK_ID smallint unsigned auto_increment primary key,
Ano year(4),
Valor int,
FK_ID_COMUNA smallint unsigned,
FK_NOMBRE_INDICADOR varchar(100),
foreign key (FK_ID_COMUNA) references Comuna(PK_ID_COMUNA),
foreign key (FK_NOMBRE_INDICADOR) references Bienestar(PK_NOMBRE_INDICADOR)
);


