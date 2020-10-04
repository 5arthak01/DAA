DROP DATABASE IF EXISTS Restaurant_rating;
CREATE SCHEMA Restaurant_rating;
USE Restaurant_rating;

--Creations 
CREATE TABLE Restaurant (cin_num VARCHAR,
	 name VARCHAR(20),
	 PRIMARY KEY(cin_num));

CREATE TABLE Branch (Res VARCHAR,
	Branch_id INT NOT NULL,
	PRIMARY KEY(Branch_id, Res),
	FOREIGN KEY(Res) REFERENCES Restaurant(cin_num));

CREATE TABLE Recipe (Recipe_name VARCHAR(20),
	Ingredients VARCHAR(255) NOT NULL,
	PRIMARY KEY(Recipe_name));

CREATE TABLE Dish (Dish_name VARCHAR(20) NOT NULL,
	Price INT NOT NULL,
	CHECK(Price>=0),
	PRIMARY KEY(Dish_name),
	FOREIGN KEY(Dish_name) REFERENCES Recipe(Recipe_name));

CREATE TABLE Dish_meal (Dish_name VARCHAR(20) NOT NULL,
	Meal VARCHAR(20) NOT NULL,
	CHECK(Meal='Breakfast' OR Meal='Lunch' OR Meal='Dinner' OR Meal='Snacks' OR Meal='Dessert'),
	PRIMARY KEY(Dish_name),
	FOREIGN KEY(Dish_name) REFERENCES Dish(Dish_name));

CREATE TABLE Employee (Employee_id VARCHAR(20) NOT NULL,
	Branch_id INT NOT NULL,
	Super_id VARCHAR(20) NOT NULL,
	Res VARCHAR NOT NULL,
	PRIMARY KEY(Employee_id),
	CHECK (SUBSTRING(Employee_id, 1, 2)='WA' OR SUBSTRING(Employee_id, 1, 2)='HC' OR SUBSTRING(Employee_id, 1, 2)='SC' OR SUBSTRING(Employee_id, 1, 2)='MA'),
	CHECK (SUBSTRING(Super_id, 1, 2)='WA' OR SUBSTRING(Super_id, 1, 2)='HC' OR SUBSTRING(Super_id, 1, 2)='SC' OR SUBSTRING(Super_id, 1, 2)='MA'),
	FOREIGN KEY(Branch_id) REFERENCES Branch(Branch_id),
	FOREIGN KEY(Res) REFERENCES Branch(Res));

--Check for existence of ID in Employee table before insertion
CREATE TABLE Manager(Manager_id VARCHAR(20) NOT NULL,
	PRIMARY KEY(Manager_id),
	FOREIGN KEY(Manager_id) REFERENCES Employee(Employee_id));

CREATE TABLE Waiter(Waiter_id VARCHAR(20) NOT NULL,
	PRIMARY KEY(Waiter_id),
	FOREIGN KEY(Waiter_id) REFERENCES Employee(Employee_id));

CREATE TABLE Chef(Chef_id VARCHAR(20) NOT NULL,
	Position VARCHAR(20) NOT NULL,
	PRIMARY KEY(Chef_id),
	FOREIGN KEY(Chef_id) REFERENCES Employee(Employee_id));
--check over 

CREATE TABLE Customers(Phone char(10) NOT NULL,
	CONSTRAINT Valid_number CHECK(LENGTH(Phone)=10 AND REGEXP_LIKE(Phone, '^[0-9]*$')),
	Entry_time DATETIME,
	PRIMARY KEY(Phone, Entry_time));

CREATE TABLE Feedback(Waiter_id VARCHAR(20),
	Chef_id VARCHAR(20),
	Dish_name VARCHAR(20),
	Phone char(10),
	Entry_time DATETIME,
	Suggestion VARCHAR(255),
	Rating INT NOT NULL,
	CHECK (Rating>= 0 and Rating <=10),
	PRIMARY KEY(Waiter_id, Chef_id, Dish_name, Phone, Entry_time),
	FOREIGN KEY(Waiter_id) REFERENCES Waiter(Waiter_id),
	FOREIGN KEY(Chef_id) REFERENCES Chef(Chef_id),
	FOREIGN KEY(Dish_name) REFERENCES Dish(Dish_name),
	FOREIGN KEY(Phone,Entry_time) REFERENCES Customers(Phone,Entry_time));

--Insertions
INSERT INTO Restaurant VALUES ("Pizza Hut 557623",	"Pizza Hut");

INSERT INTO Branch VALUES ("Pizza Hut 557623",	123),	("Pizza Hut 557623",	391);

INSERT INTO Recipe VALUES ("Steak",	"beef,	butter,	garlic,	oil,	salt"),	("Onion Rings",	"onion,	salt,	oil,	egg,	bread crumbs,	flour"),	("Veg fried Rice",	"rice,	cabbage,	peas,	beans,	carrot,	salt"),	("chicken biryani",	"rice,	chicken,	onion,	chillies,	mint,	salt"),	("Brownie",	"chocolate,	butter,	egg,	flour,	sugar,	baking powder,	ice cream");

INSERT INTO Dish VALUES ("Steak",	600),	("Onion Rings",	200),	("Veg fried Rice",	300),	("chicken biryani",	450),	("Brownie",	80);

INSERT INTO Dish_meal VALUES ("Steak",	"Lunch"),	("Steak",	"Dinner"),	("Onion Rings",	"Snack"),	("Veg Fried Rice",	"Lunch"),	("Veg Fried Rice",	"Dinner"),	("chicken biryani",	"Dinner"),	("Brownie",	"Dessert");

INSERT INTO  Customers VALUES (9999999999,	"2020-07-13 20:30:17"),	(8888888888,	"2020-06-21 13:45:56"),	(7777777777,	"2020-09-05 12:14:59"),	(6666666666,	"2020-10-1 21:50:00");

INSERT INTO Employee VALUES ("WA11111",	123,	"MA1111",	557623),	("WA11112",	123,	"MA1111",	557623),	("HC11111",	123,	"MA1111",	557623),	("SC11112",	123,	"MA1111",	557623),	("MA1111",	123,	"MA1111",	557623),	("WA33333",	391,	"MA3333",	557623),	("WA33334",	391,	"MA3333",	557623),	("HC33333",	391,	"MA3333",	557623),	("SC33334",	391,	"MA3333",	557623),	("MA3333",	391,	"MA3333",	557623);

INSERT INTO Waiter VALUES ("WA11111"),	("WA11112"),	("WA33333"),	("WA33334");

INSERT INTO Chef VALUES ("HC11111",	"Head Chef"),	("SC11112",	"Sous Chef"),	("HC33333",	"Head Chef"),	("SC33334",	"Sous Chef");

INSERT INTO Manager VALUES ("MA1111"),	("MA3333");
