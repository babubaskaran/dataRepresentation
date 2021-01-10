use datarepresentation

create table employees(
EMPID int PRIMARY KEY,
First_Name varchar(100),
Last_Name varchar(100),
DEPCODE int,
ADDR1 varchar(100),
CITY varchar(100),
STATE varchar(100),
ZIP varchar(100)
);

create table department(
DEPCODE int PRIMARY KEY,
DeptName varchar(100),
MGR_Name varchar(100)
);