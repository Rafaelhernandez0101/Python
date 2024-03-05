use RafaelPython;
create database RafaelAprendices; 

create table Aprendices
(
id int (10) primary key not null, 
nombre varchar (50) not null,
surfname varchar (50) not null,
phone int (10) not null,
clas ENUM ('M', 'F') not null,
mail varchar (50) not null
);
