--MIDTERM PROJECT in BDM 1034 - Application Design for Big Data
--STUDENT DATA MANAGEMENT- Submitted by : GROUP B

--1.	Create a database called “LMT_University”.
CREATE DATABASE LMT_University;
GO
USE LMT_University;
GO
--2.	Create an “enrol” schema under “LMT_University”.
CREATE SCHEMA enrol;
GO
--3.	Use “enrol” Schema for creating the project.
--5.	Create an “Address” table under “enrol” schema with the given a) Attributes and b) Contraints:
CREATE TABLE enrol.Address
(
	AddressID int identity(1,1) NOT NULL,
	StreetAddress varchar(50),
	City nvarchar(50) NOT NULL,
	State nvarchar(30),
	PostalCode varchar(30),
	Country varchar(30),
	InsertedOn datetime NOT NULL,
	CONSTRAINT PK_Address PRIMARY KEY CLUSTERED(AddressID ASC)
);
GO
--5. c)	Insert the Records in Address based on the given specifications:
Insert into enrol.Address values('5 Schurz Lane','Grybów',NULL,'33-330','Poland',SYSDATETIME())
Insert into enrol.Address values('628 Waubesa Drive','Jinsheng',NULL,NULL,'China',SYSDATETIME())
Insert into enrol.Address values('44135 Northfield Way','Nowy Dwór Mazowiecki',NULL,'05-160','Poland',SYSDATETIME())
Insert into enrol.Address values('335 Bellgrove Road','Gaoqiao',NULL,NULL,'China',SYSDATETIME())
Insert into enrol.Address values('28 Victoria Junction','Bukovec',NULL,'739 84','Czech Republic',SYSDATETIME())
Insert into enrol.Address values('6 Stuart Road','Wushan',NULL,NULL,'China',SYSDATETIME())
Insert into enrol.Address values('730 Barby Street','Zhengchang',NULL,NULL,'China',SYSDATETIME())
Insert into enrol.Address values('22742 Schiller Street','Sumurwaru',NULL,NULL,'Indonesia',SYSDATETIME())
Insert into enrol.Address values('31 Elka Junction','Cigembong',NULL,NULL,'Indonesia',SYSDATETIME())
Insert into enrol.Address values('5 Kenwood Circle','Davao',NULL,'8000','Philippines',SYSDATETIME())
Insert into enrol.Address values('99 Bunker Hill Crossing','Zarasai',NULL,'32001','Lithuania',SYSDATETIME())
Insert into enrol.Address values('5 Farragut Center','Jaromerice',NULL,'569 44','Czech Republic',SYSDATETIME())
Insert into enrol.Address values('25 Lerdahl Street','Nanshi',NULL,NULL,'China',SYSDATETIME())
Insert into enrol.Address values('918 Bonner Way','Phayakkhaphum Phisai',NULL,'44110','Thailand',SYSDATETIME())
Insert into enrol.Address values('9 West Alley','Sempu',NULL,NULL,'Indonesia',SYSDATETIME())
Insert into enrol.Address values('234 Hagan Lane','Rennes','Bretagne','35033','France',SYSDATETIME())
Insert into enrol.Address values('33942 Eagle Crest Trail','Oliveiras','Porto','4745-235','Portugal',SYSDATETIME())
Insert into enrol.Address values('20791 Hermina Way','B?o L?c',NULL,NULL,'Vietnam',SYSDATETIME())
Insert into enrol.Address values('86 Lake View Way','Marsa Alam',NULL,NULL,'Egypt',SYSDATETIME())
Insert into enrol.Address values('19732 Burning Wood Parkway','Piteå','Norrbotten','944 73','Sweden',SYSDATETIME())
Insert into enrol.Address values('9320 Oak Valley Road','Rathangani',NULL,'A45','Ireland',SYSDATETIME())
Insert into enrol.Address values('2638 Waubesa Circle','Honda',NULL,'732048','Colombia',SYSDATETIME())
Insert into enrol.Address values('6999 Monument Center','Cortes',NULL,'6341','Philippines',SYSDATETIME())
Insert into enrol.Address values('1 Warbler Hill','Proletar',NULL,NULL,'Tajikistan',SYSDATETIME())
Insert into enrol.Address values('1311 Crowley Street','Baghlan',NULL,NULL,'Afghanistan',SYSDATETIME())
Insert into enrol.Address values('19 Walton Way','Öldziyt',NULL,NULL,'Mongolia',SYSDATETIME())
Insert into enrol.Address values('1 Glacier Hill','Cergy-Pontoise','Île-de-France','95304','France',SYSDATETIME())
Insert into enrol.Address values('5094 Gateway Way','Živinice',NULL,NULL,'Bosnia and Herzegovina',SYSDATETIME())
Insert into enrol.Address values('2 Roth Pass','Tuatuka',NULL,NULL,'Indonesia',SYSDATETIME())
Insert into enrol.Address values('89531 Northview Road','Ganyi',NULL,NULL,'China',SYSDATETIME())
GO

--6. Create a “Department” table under “enrol” schema with the given a) Attributes and b) Contraints:
CREATE TABLE enrol.Department
(
DepartmentID int identity(1,1) NOT NULL,
DepartmentName varchar(30) NOT NULL,
DepartmentDescription varchar(MAX),
DepartmentCapacity int NOT NULL,
InsertedOn datetime NOT NULL,
CONSTRAINT PK_Department PRIMARY KEY CLUSTERED(DepartmentID ASC)
);
GO
--6. c)	Insert the Records in Department table based on the given specifications:
Insert into enrol.Department values('IT','Information Technology','60',SYSDATETIME())
Insert into enrol.Department values('EE','Electrical Engineering','120',SYSDATETIME())
Insert into enrol.Department values('CSE','Computer Science Engineering','140',SYSDATETIME())
Insert into enrol.Department values('ME','Mechanical Engineering','110',SYSDATETIME())
Insert into enrol.Department values('ECE','Electronic and Communication Engineering','80',SYSDATETIME())
Insert into enrol.Department values('AEIE','Applied Electronics and Instrumentation Engineering','50',SYSDATETIME())
GO

--7. Create a “Lecturer” table under “enrol” schema with the given a) Attributes and b) Contraints:
CREATE TABLE enrol.Lecturer
(
LecturerID int identity(1,1) NOT NULL,
LecturerName varchar(50) NOT NULL,
LecturerHighestQualification varchar(30),
LecturerAge date NOT NULL,
DepartmentID int NOT NULL FOREIGN KEY REFERENCES enrol.Department(DepartmentID),
InsertedOn datetime,
CONSTRAINT PK_Lecturer PRIMARY KEY CLUSTERED(LecturerID ASC),
);
GO
--7. c)	Insert the Records in Lecturer table based on the given specifications:
Insert into enrol.Lecturer values('Peder Bernaldez','M.Tech','2010-10-10','6',SYSDATETIME())
Insert into enrol.Lecturer values('Emile Adolthine','PhD','2010-04-04','5',SYSDATETIME())
Insert into enrol.Lecturer values('Titos Iorizzi','M.Tech','2012-04-09','4',SYSDATETIME())
Insert into enrol.Lecturer values('Ferris Falck','MSC','2011-05-05','3',SYSDATETIME())
Insert into enrol.Lecturer values('Georgie McIlwraith','M.Tech','2017-05-08','2',SYSDATETIME())
Insert into enrol.Lecturer values('Karlen Kearn','MSC','2019-03-03','1',SYSDATETIME())
Insert into enrol.Lecturer values('Axe Whistlecroft','MCA','2019-03-03','6',SYSDATETIME())
Insert into enrol.Lecturer values('Drucie Bazek','PhD','2019-04-01','5',SYSDATETIME())
Insert into enrol.Lecturer values('Antony Gamlin','M.Tech','2019-04-01','4',SYSDATETIME())
Insert into enrol.Lecturer values('Alexina Moncaster','MBA','2019-04-01','3',SYSDATETIME())
Insert into enrol.Lecturer values('Milzie Kabos','MCA','2019-03-03','2',SYSDATETIME())
Insert into enrol.Lecturer values('Arlene Glendza','MS','2019-03-03','1',SYSDATETIME())
Insert into enrol.Lecturer values('Kirby Kabisch','M.Tech','2019-04-01','1',SYSDATETIME())
Insert into enrol.Lecturer values('Selma Eliyahu','PhD','2019-04-01','2',SYSDATETIME())
Insert into enrol.Lecturer values('Ilysa Chooter','M.Tech','2019-04-01','3',SYSDATETIME())
Insert into enrol.Lecturer values('Rozalie Pennycord','MSC','2010-10-10','4',SYSDATETIME())
Insert into enrol.Lecturer values('Dacey Glidder','M.Tech','2010-04-04','5',SYSDATETIME())
Insert into enrol.Lecturer values('Claretta Diaper','MSC','2012-04-09','6',SYSDATETIME())
Insert into enrol.Lecturer values('Kalil Pendleton','MCA','2011-05-05','6',SYSDATETIME())
Insert into enrol.Lecturer values('Trudey Brech','PhD','2011-10-05','5',SYSDATETIME())
Insert into enrol.Lecturer values('Gypsy Ambrosini','M.Tech','2011-03-30','4',SYSDATETIME())
Insert into enrol.Lecturer values('Lauree Ribbon','MBA','2013-04-04','3',SYSDATETIME())
Insert into enrol.Lecturer values('Hugo Valois','MCA','2012-04-29','2',SYSDATETIME())
Insert into enrol.Lecturer values('Perren Chetter','MS','2018-05-03','1',SYSDATETIME())
Insert into enrol.Lecturer values('Fawn Coffelt','M.Tech','2020-02-26','1',SYSDATETIME())
Insert into enrol.Lecturer values('Terrie Golby','PhD','2020-02-26','2',SYSDATETIME())
Insert into enrol.Lecturer values('Jeanette Ciraldo','M.Tech','2020-03-26','3',SYSDATETIME())
Insert into enrol.Lecturer values('Elfrieda Elijahu','MSC','2020-03-26','4',SYSDATETIME())
Insert into enrol.Lecturer values('Guthry Blaes','M.Tech','2020-03-26','5',SYSDATETIME())
Insert into enrol.Lecturer values('Richy Saice','MSC','2020-02-26','6',SYSDATETIME())
GO

--8. Create a “Student” table under “enrol” schema with the given a) Attributes and b) Contraints:
CREATE TABLE enrol.Student
(
	StudentID int identity(1,1) NOT NULL,
	StudentFirstName varchar(50) NOT NULL,
	StudentLastName varchar(50),
	StudentDOB date NOT NULL,
	StudentMobile varchar(30),
	StudentRollNo int NOT NULL,
	DepartmentID int NOT NULL FOREIGN KEY REFERENCES enrol.Department(DepartmentID),
	AddressID int NOT NULL FOREIGN KEY REFERENCES enrol.Address(AddressID),
	InsertedOn datetime NOT NULL,
	CONSTRAINT PK_Student PRIMARY KEY CLUSTERED(StudentID ASC)
);
GO
--8. c)	Insert the Records in Lecturer table based on the given specifications:
Insert into enrol.Student values('Joey','Ironside','1995-11-22','1276234258','1','3','1',SYSDATETIME())
,('Karlotta','Garraway','1997-07-06','2192431615','2','3','24',SYSDATETIME())
,('Jerry','Stutte','1996-12-18','4125425783','3','1','17',SYSDATETIME())
,('Yehudit','Rahill','1995-01-15','9939485406','4','2','29',SYSDATETIME())
,('Cele','Crosetto','1998-11-24','3622733725','5','3','16',SYSDATETIME())
,('Hazlett','Mowsdale','1995-04-09','1482883476','6','4','23',SYSDATETIME())
,('Carlyn','Marks','1996-12-27','6129154080','7','5','20',SYSDATETIME())
,('Ellis','Boatman','1997-04-29','8269707118','8','6','7',SYSDATETIME())
,('Florina','Boyack','1997-08-03','9623352863','9','3','14',SYSDATETIME())
,('Borg','Innett','1997-09-03','5256034960','10','1','19',SYSDATETIME())
,('Sayres','Jennings','1996-05-12','8675076454','11','4','27',SYSDATETIME())
,('Jarid','Sprull','1998-11-02','1391270091','12','2','6',SYSDATETIME())
,('Elvera','Bannard','1996-09-07','7897232539','13','4','24',SYSDATETIME())
,('Ody','Inggall','1995-03-05','6094734260','14','5','25',SYSDATETIME())
,('Curcio','McWhan','1996-07-29','2394865847','15','6','11',SYSDATETIME())
,('Connie','Sinnie','1995-07-19','1473936221','16','6','23',SYSDATETIME())
,('Auroora','Nel','1996-09-05','2216400391','17','3','14',SYSDATETIME())
,('Wendall','Rosendale','1999-12-30','1818120249','18','3','28',SYSDATETIME())
,('Hadley','Bradbury','1996-08-16','6518067697','19','1','10',SYSDATETIME())
,('Celine','Smales','1999-07-11','7106508130','20','2','10',SYSDATETIME())
,('Jesselyn','Stevenson','1998-05-16','9231672206','21','2','22',SYSDATETIME())
,('Corinna','Pinkney','1998-01-16','8323630067','22','5','29',SYSDATETIME())
,('Orelle','Adamthwaite','1997-07-26','2539126766','23','3','17',SYSDATETIME())
,('Howie','Seaman','1997-12-01','9888259627','24','2','4',SYSDATETIME())
,('Sibyl','Corey','1996-07-18','4493239590','25','5','11',SYSDATETIME())
,('Ruperta','Peaker','1999-05-22','5124781263','26','5','4',SYSDATETIME())
,('Delmer','Roughey','1995-04-21','4175314364','27','3','22',SYSDATETIME())
,('Gifford','O''Scannill','1996-10-31','3134783726','28','4','22',SYSDATETIME())
,('Hedy','O''Hone','1998-03-29','7316228047','29','2','17',SYSDATETIME())
,('Shalna','Hyde-Chambers','1999-11-23','7455116160','30','5','6',SYSDATETIME())
,('Ferdie','Di Napoli','1995-01-17','1905908693','31','4','30',SYSDATETIME())
,('Piper','Giacomuzzo','1998-09-14','5499340503','32','6','4',SYSDATETIME())
,('Gerhardt','Schruurs','1999-11-18','8197494894','33','3','1',SYSDATETIME())
,('Mellicent','Buncher','1996-10-03','4584525312','34','5','28',SYSDATETIME())
,('Corette','Demead','1997-09-17','4909862137','35','5','17',SYSDATETIME())
,('Jorgan','Barson','1997-05-01','6022309183','36','1','21',SYSDATETIME())
,('Koral','Bowen','1998-05-12','4198817454','37','4','3',SYSDATETIME())
,('Allissa','Kitter','1998-08-17','7328676920','38','5','7',SYSDATETIME())
,('Townsend','Doughtery','1998-04-13','2639777958','39','4','7',SYSDATETIME())
,('Yolane','Geratt','1998-06-10','2069585951','40','6','17',SYSDATETIME())
,('Chrystel','Allwood','1996-09-07','6958461692','41','3','25',SYSDATETIME())
,('Dyana','Clutterbuck','1997-09-22','5842483886','42','1','1',SYSDATETIME())
,('Nikki','Edy','1999-01-10','5096155315','43','6','25',SYSDATETIME())
,('Hendrik','Surr','1997-04-05','2021255732','44','5','11',SYSDATETIME())
,('Marta','Bosch','1998-09-28','4075136713','45','6','5',SYSDATETIME())
,('Garrik','Pell','1999-04-14','3071057649','46','6','7',SYSDATETIME())
,('Stormi','Colbron','1998-10-21','9968113654','47','3','28',SYSDATETIME())
,('Angelique','Iacivelli','1995-06-07','9518365081','48','5','7',SYSDATETIME())
,('Zack','Hefforde','1999-07-25','5455693035','49','1','29',SYSDATETIME())
,('Gusella','Pettiford','1999-08-23','2425172721','50','4','3',SYSDATETIME())
;
GO
--9.Write the following Query based on the above datasets.
-- a.	List all the Student information from the Student table.
SELECT * FROM enrol.Student;
GO
-- b.List all the Department information from the Department table.
SELECT * FROM enrol.Department;
GO
-- c.List all the Lecturer information from the Lecturer table.
SELECT * FROM enrol.Lecturer;
GO
-- d.List all the Address information from the Address table.
SELECT * FROM enrol.Address;
GO
-- e.List the StudentFullName, StudentDOB, StudentMobile from Student [StudentFullName=StudentFirstName + ‘  ‘ + StudentLastName]
SELECT enrol.Student.StudentFirstName + ' ' + enrol.Student.StudentLastName as 'StudentFullName', enrol.Student.StudentDOB, enrol.Student.StudentMobile
FROM enrol.Student;
GO
--f.List the StudentID, StudentFirstName, StudentLastName, StudentDOB, StudentMobile from Student in AddressID 7.
SELECT enrol.Student.StudentID, enrol.Student.StudentFirstName, enrol.Student.StudentLastName, enrol.Student.StudentDOB, enrol.Student.StudentMobile
FROM enrol.Student
WHERE enrol.student.AddressID = 7;
GO
--g.List all the student information whose first name is start with 'B'
SELECT * FROM enrol.Student 
WHERE enrol.Student.StudentFirstName LIKE 'B%';
GO
--h.List all the student information whose first name is start and end with 'A'
SELECT * FROM enrol.Student 
WHERE enrol.Student.StudentFirstName LIKE 'A%' AND enrol.Student.StudentFirstName LIKE '%A';
GO
--i.Count the number of Student from Student table whose DepartmentID 6.
SELECT COUNT(enrol.Student.StudentFirstName ) as DeptID6_No_of_Students
FROM enrol.Student
WHERE DepartmentID = 6;
GO
--j.List all the StudentFullName, StudentAge, StudentMobile from Student [StudentFullName= StudentFirstName + ‘  ‘ + StudentLastName]
--[StudentAge= Current date – DOB (in Years)]
SELECT enrol.Student.StudentFirstName + ' ' + enrol.Student.StudentLastName as 'StudentFullName', 
	   DATEDIFF(year, enrol.Student.StudentDOB, GETDATE()) as 'StudentAge', enrol.Student.StudentMobile
FROM enrol.Student;
GO
--k.List all the StudentFullName, StudentAge, StudentMobile whose Age>23 from Student [StudentFullName= StudentFirstName + ‘  ‘ + StudentLastName]
--[StudentAge= Current date – DOB (in Years)]
SELECT enrol.Student.StudentFirstName + ' ' + enrol.Student.StudentLastName as 'StudentFullName', 
       DATEDIFF(year, enrol.Student.StudentDOB, GETDATE()) as 'StudentAge', enrol.Student.StudentMobile
FROM enrol.Student
WHERE DATEDIFF(year, enrol.Student.StudentDOB, GETDATE()) >23;
GO
--l.List all the StudentFullName, StudentAge, StudentMobile whose Age is either 21 or 23 from Student [StudentFullName= StudentFirstName + ‘  ‘ + StudentLastName]
--[StudentAge= Current date – DOB (in Years)]
SELECT enrol.Student.StudentFirstName + ' ' + enrol.Student.StudentLastName as 'StudentFullName', 
       DATEDIFF(year, enrol.Student.StudentDOB, GETDATE()) as 'StudentAge', enrol.Student.StudentMobile
FROM enrol.Student
WHERE DATEDIFF(year, enrol.Student.StudentDOB, GETDATE()) = 21 OR DATEDIFF(year, enrol.Student.StudentDOB, GETDATE()) = 23;
GO
--m. List all the LecturerID, LecturerName, LecturerHighestQualification, LecturerAge from Lecturer.
SELECT enrol.Lecturer.LecturerID, enrol.Lecturer.LecturerName, enrol.Lecturer.LecturerHighestQualification, enrol.Lecturer.LecturerAge 
FROM enrol.Lecturer;
GO
--n. List all the LecturerID, LecturerName, LecturerHighestQualification, LecturerAge from Lecturer whose HighestQualification is either “MS” or “PhD”.
SELECT enrol.Lecturer.LecturerID, enrol.Lecturer.LecturerName, enrol.Lecturer.LecturerHighestQualification, enrol.Lecturer.LecturerAge 
FROM enrol.Lecturer
WHERE enrol.Lecturer.LecturerHighestQualification = 'MS' OR enrol.Lecturer.LecturerHighestQualification = 'Phd';
GO
-- o. List all the lecturer information who belongs to DepartmentID 2.
SELECT * FROM enrol.Lecturer
WHERE enrol.Lecturer.DepartmentID = 2; 
GO
--p. List all the lecturer information whose name end with “R”.
SELECT * FROM enrol.Lecturer
WHERE enrol.Lecturer.LecturerName LIKE '%R';
GO
--q. List all the lecturer information whose name either start or end with “E”.
SELECT * FROM enrol.Lecturer
WHERE enrol.Lecturer.LecturerName LIKE 'E%' OR enrol.Lecturer.LecturerName LIKE '%E';
GO
--r. List all the lecturer name is in capital letter.
SELECT * FROM enrol.Lecturer
WHERE ASCII(LEFT(enrol.Lecturer.LecturerName, 1)) BETWEEN 65 AND 90;
GO
--s. Display 5 character from the lecturer name along with LecturerID and LecturerHighestQualification.
SELECT SUBSTRING(enrol.Lecturer.LecturerName, 1, 5), enrol.Lecturer.LecturerID, enrol.Lecturer.LecturerHighestQualification
FROM enrol.Lecturer;
GO
--t. List LecturerID, LecturerName, LecturerHighestQualification, LecturerAge(in year) [LecturerAge= Current Date – LecturerAge)] (in year).
SELECT enrol.Lecturer.LecturerID, enrol.Lecturer.LecturerName, enrol.Lecturer.LecturerHighestQualification,
	   DATEDIFF(year, enrol.Lecturer.LecturerAge, GETDATE()) as 'LecturerAge'
FROM enrol.Lecturer;
GO
--u. List DepartmentID, DepartmentName, DepartmentDescription, DepartmentCapacity from Department.
SELECT enrol.Department.DepartmentID, enrol.Department.DepartmentName, enrol.Department.DepartmentDescription,
		enrol.Department.DepartmentCapacity
FROM enrol.Department;
GO
--v. List all the Department information who’s DepartmentName is “ECE”.
SELECT * FROM enrol.Department
WHERE enrol.Department.DepartmentName = 'ECE';
GO
--w. List all DepartmentName, DepartmentDescription, DepartmentCapacity from Department whose capacity is greater than 60.
SELECT enrol.Department.DepartmentName, enrol.Department.DepartmentDescription, enrol.Department.DepartmentCapacity
FROM enrol.Department
WHERE enrol.Department.DepartmentCapacity > 60; 
GO
--x. List all AddressID, StreetAddress, City, State, PostalCode, Country from Address.
SELECT enrol.Address.AddressID, enrol.Address.StreetAddress, enrol.Address.City, enrol.Address.State, enrol.Address.PostalCode,
		enrol.Address.Country
FROM enrol.Address;
GO
--y. List all AddressID, StreetAddress, City, State, PostalCode, Country from Address who belongs to “Poland” country.
SELECT enrol.Address.AddressID, enrol.Address.StreetAddress, enrol.Address.City, enrol.Address.State, enrol.Address.PostalCode,
		enrol.Address.Country
FROM enrol.Address
WHERE enrol.Address.Country = 'Poland';
GO
--z. List all the Address information whose state is null.
SELECT * FROM enrol.Address
WHERE enrol.Address.State IS NULL;
GO
--aa. List all the Address information whose PostalCode is not null.
SELECT * FROM enrol.Address
WHERE enrol.Address.PostalCode IS NOT NULL;
GO
--bb. List all the Address information whose City name is "Honda" and Country name is "Colombia"
SELECT * FROM enrol.Address
WHERE enrol.Address.City = 'Honda' AND enrol.Address.Country = 'Colombia';
GO

--10. Write the following Query based on the above datasets.
-- a. List unique DOB from Student.
select distinct [StudentDOB] from [enrol].[Student];
GO
--b.List unique DepartmentName from Department.
select distinct [DepartmentName] from [enrol].[Department];
GO
--c.List unique Country name from Address.
select distinct [Country] from [enrol].[Address];
GO
--d.List unique State name from Address.
select distinct [State] from [enrol].[Address];
GO
--e.List unique City name from Address.
select distinct [City] from [enrol].[Address];
GO
--f.List all the LecturerID, LecturerName, LecturerHighestQualification, LecturerYearService from Lecturer [LecturerYearService= Current Date – LecturerAge] (in year).
select [LecturerID],[LecturerName],[LecturerHighestQualification], datediff(year,[LecturerAge],convert(date,getdate()) ) as LecturerYearService from [enrol].[Lecturer] ;
GO
--g.List all the LecturerID, LecturerName, LecturerHighestQualification, LecturerType from Lecturer [LecturerType= if LecturerYearService< 5 then "Begining Level Experience" else if LecturerYearService>= 5 and LecturerYearService<10 then "Mid Level experience" else "Experienced".
GO
select [LecturerID],[LecturerName],[LecturerHighestQualification],
case When datediff(year,[LecturerAge],convert(date,getdate()) )<5 then 'Begining Level Experience'
 When datediff(year,[LecturerAge],convert(date,getdate()) )>=5 and datediff(year,[LecturerAge],convert(date,getdate()) )<10   then 'Mid Level Experience'
 else 'Experienced'
 End as 'LecturerType'
 from [enrol].[Lecturer];
GO

--11. Write the following Query based on the above datasets.
--a.Display all Student and their Department Information based on the relationship.
select * from [enrol].[Student] as s ,[enrol].[Department] as d
where s.[DepartmentID]=d.[DepartmentID];
GO
--b.Display all Student and their Address Information based on the relationship.
select * from [enrol].[Student] as s , [enrol].[Address] as a
where s.[AddressID]= a.[AddressID];
GO
--c.Display all Department and their Lecturer Information based on the relationship.
select * from [enrol].[Department] as d , [enrol].[Lecturer] as l
where d.[DepartmentID]=l.[DepartmentID];
GO
--d.Display all Student with their Department with Lecturer Information based on the relationship. 
select distinct * from [enrol].[Student] as s ,[enrol].[Department] as d, [enrol].[Lecturer] as l  
where d.[DepartmentID]=l.[DepartmentID] and s.[DepartmentID]=d.[DepartmentID];
GO
--e.Display all Student with their Address and Department Information based on the relationship.
select distinct * from [enrol].[Student] as s ,[enrol].[Department] as d, [enrol].[Address] as a 
where s.[AddressID]= a.[AddressID] and s.[DepartmentID]=d.[DepartmentID];
GO
--f. Display all Student with Address, Department and Lecturer Information based on the relationship.
select distinct * from [enrol].[Student] as s ,[enrol].[Department] as d, [enrol].[Address] as a, [enrol].[Lecturer] as l 
where s.[AddressID]= a.[AddressID] and s.[DepartmentID]=d.[DepartmentID] and d.[DepartmentID]=l.[DepartmentID];
GO
--g.Display all Student with Address, Department and Lecturer Information who belongs to either “ME” or “ECE” department.
select distinct * from [enrol].[Student] as s ,[enrol].[Department] as d, [enrol].[Address] as a, [enrol].[Lecturer] as l 
where s.[AddressID]= a.[AddressID] and s.[DepartmentID]=d.[DepartmentID] and d.[DepartmentID]=l.[DepartmentID]
and (d.[DepartmentName]='ME' or d.[DepartmentName]='ECE');
GO
--h.Display Student with Department and their Lecturer information based on the LecturerHighestQualification either “MS” or “PhD”.
select distinct * from [enrol].[Student] as s ,[enrol].[Department] as d, [enrol].[Lecturer] as l 
where  s.[DepartmentID]=d.[DepartmentID] and d.[DepartmentID]=l.[DepartmentID]
and (l.[LecturerHighestQualification]='MS' or l.[LecturerHighestQualification]='PhD');
GO
--i.Display Student with Department and Address Information, where student belongs to “Thailand” country.
select  * from [enrol].[Student] as s ,[enrol].[Department] as d, [enrol].[Address] as a
where s.[AddressID]= a.[AddressID] and s.[DepartmentID]=d.[DepartmentID]
and a.[Country]='Thailand';
GO
--j.Display Count of Student, Department wise.
select  [DepartmentName],count(*) as count_of_students from [enrol].[Student],[enrol].[Department]
where [enrol].[Department].[DepartmentID]=[enrol].[Student].[DepartmentID]
group by [enrol].[Department].[DepartmentName];
GO
--k.Display Count of Lecturer, Department wise.
select  [DepartmentName],count(*) as count_of_lecturer from [enrol].[Lecturer],[enrol].[Department]
where [enrol].[Department].[DepartmentID]=[enrol].[Lecturer].[DepartmentID]
group by [enrol].[Department].[DepartmentName];
GO
--l.Display Count of Student, Country wise.
select [Country], count(*) as Count_of_Students from [enrol].[Address],[enrol].[Student]
where [enrol].[Student].[AddressID]=[enrol].[Address].[AddressID]
group by [enrol].[Address].[Country];
GO

--12.	Write the following Query based on the above datasets. 
-- a.	Create new table StudCopy and copy all records from Student table.
select * into enrol.Studcopy from enrol.Student;
go
--b.	Create a new table DeptCopy and copy only the schema from Department table.
select Top 0 * into enrol.Deptcopy from enrol.Department;
go
--c.	Create a new table DepartmentCopy and copy all records from Department table.
select * into enrol.Departmentcopy from enrol.Department;
go
--d.	Create a new table AddrCopy and copy only the schema from Address table.
select top 0 * into enrol.Addrcopy from enrol.Address;
go
--e.	Create a new table AddressCopy and copy all the records from Address table.
select * into enrol.Addresscopy from enrol.Address;
go
--f.	Create a new table LecturerCopy and copy all the records from Lecturer table.
select * into enrol.Lecturercopy from enrol.Lecturer;
go

--13.	Write the following Query based on the above datasets.
--a.	Delete all the records from LecturerCopy table.
delete from enrol.Lecturercopy;
go

--b.	Delete all the student information for the students who belong to “IT” department.
delete enrol.Studcopy 
from enrol.Studcopy
join enrol.Departmentcopy on Departmentcopy.DepartmentID = Studcopy.DepartmentID
where Departmentcopy.Departmentname = 'IT';
go

--c.	Delete all the student information for the students who belong to “Indonesia” country.
delete enrol.Studcopy 
from enrol.Studcopy
join enrol.Addresscopy on Addresscopy.AddressID = Studcopy.AddressID
where Addresscopy.Country = 'Indonesia';
go

--d.	Delete all the student information for the student who belongs to “Nanshi” city.
delete enrol.Studcopy 
from enrol.Studcopy
join enrol.Addresscopy on Addresscopy.AddressID = Studcopy.AddressID
where Addresscopy.City = 'Nanshi';
go

--e.	Delete all the student information for the student who belongs to “Bretagne” state.
delete enrol.Studcopy 
from enrol.Studcopy
join enrol.Addresscopy on Addresscopy.AddressID = Studcopy.AddressID
where Addresscopy.State = 'Bretagne';
go

--14.	Write the following Query based on the above datasets.
--a.	Update StudentMobile for those students who belongs to Department “ME”.
update enrol.Student
set StudentMobile = 1234567890 
from enrol.Student join enrol.Department on Student.DepartmentID = Department.DepartmentID
where Department.DepartmentName = 'ME';
go

--b.	Update Student DepartmentID as 3, for the StudentID=42.
update enrol.Student
set DepartmentID = 3
from enrol.Student
where StudentID = 42;
go

--c.	Update LecturerHighestQualification as “PHd” for the Lecturer whose LecturerHighestQualification= “PhD”.
update enrol.Lecturer
set LecturerHighestQualification = 'PHd'
from enrol.Lecturer
where LecturerHighestQualification = 'PhD';
go

--d.	Update PostalCode as “00000” for the Address which contain NULL as a PostalCode.
update enrol.Address
set PostalCode = '00000'
from enrol.Address
where PostalCode IS NULL;
go

--e.	Update StudentLastName as “Paul” for the Student whose Name is “Jerry”.
update enrol.Student
set StudentLastName = 'Paul'
from enrol.Student
where StudentFirstName = 'Jerry';
go
