-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: Restaurant_Ratings
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `Restaurant_Ratings`
--

DROP DATABASE IF EXISTS `Restaurant_Ratings`;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `Restaurant_Ratings` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `Restaurant_Ratings`;

--
-- Table structure for table `Branch`
--

DROP TABLE IF EXISTS `Branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Branch` (
  `Res` varchar(20) NOT NULL,
  `Branch_id` int NOT NULL,
  PRIMARY KEY (`Branch_id`,`Res`),
  KEY `Res` (`Res`),
  CONSTRAINT `Branch_ibfk_1` FOREIGN KEY (`Res`) REFERENCES `Restaurant` (`cin_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Branch`
--

LOCK TABLES `Branch` WRITE;
/*!40000 ALTER TABLE `Branch` DISABLE KEYS */;
INSERT INTO `Branch` VALUES ('Pizza Hut 557623',123),('Pizza Hut 557623',391);
/*!40000 ALTER TABLE `Branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Chef`
--

DROP TABLE IF EXISTS `Chef`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Chef` (
  `Chef_id` varchar(20) NOT NULL,
  `Position` varchar(20) NOT NULL,
  PRIMARY KEY (`Chef_id`),
  CONSTRAINT `Chef_ibfk_1` FOREIGN KEY (`Chef_id`) REFERENCES `Employee` (`Employee_id`),
  CONSTRAINT `Chef_chk_1` CHECK ((((substr(`Chef_id`,1,2) = _utf8mb3'HC') and (`Position` = _utf8mb3'Head Chef')) or ((substr(`Chef_id`,1,2) = _utf8mb3'SC') and (`Position` = _utf8mb3'Sous Chef'))))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Chef`
--

LOCK TABLES `Chef` WRITE;
/*!40000 ALTER TABLE `Chef` DISABLE KEYS */;
INSERT INTO `Chef` VALUES ('HC11111','Head Chef'),('HC33333','Head Chef'),('SC11112','Sous Chef'),('SC33334','Sous Chef');
/*!40000 ALTER TABLE `Chef` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customers` (
  `Phone` char(10) NOT NULL,
  `Entry_time` datetime NOT NULL,
  PRIMARY KEY (`Phone`,`Entry_time`),
  CONSTRAINT `Valid_number` CHECK (((length(`Phone`) = 10) and regexp_like(`Phone`,_utf8mb3'^[0-9]*$')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES ('6666666666','2020-10-01 21:50:00'),('7777777777','2020-09-05 12:14:59'),('8888888888','2020-06-21 13:45:56'),('9999999999','2020-07-13 20:30:17');
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dish`
--

DROP TABLE IF EXISTS `Dish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dish` (
  `Dish_name` varchar(20) NOT NULL,
  `Price` int NOT NULL,
  PRIMARY KEY (`Dish_name`),
  CONSTRAINT `Dish_ibfk_1` FOREIGN KEY (`Dish_name`) REFERENCES `Recipe` (`Recipe_name`),
  CONSTRAINT `Dish_chk_1` CHECK ((`Price` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dish`
--

LOCK TABLES `Dish` WRITE;
/*!40000 ALTER TABLE `Dish` DISABLE KEYS */;
INSERT INTO `Dish` VALUES ('Brownie',80),('chicken biryani',450),('Onion Rings',200),('Steak',600),('Veg fried Rice',300);
/*!40000 ALTER TABLE `Dish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dish_meal`
--

DROP TABLE IF EXISTS `Dish_meal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dish_meal` (
  `Dish_name` varchar(20) NOT NULL,
  `Meal` varchar(20) NOT NULL,
  PRIMARY KEY (`Dish_name`,`Meal`),
  CONSTRAINT `Dish_meal_ibfk_1` FOREIGN KEY (`Dish_name`) REFERENCES `Dish` (`Dish_name`),
  CONSTRAINT `Dish_meal_chk_1` CHECK (((`Meal` = _utf8mb3'Breakfast') or (`Meal` = _utf8mb3'Lunch') or (`Meal` = _utf8mb3'Dinner') or (`Meal` = _utf8mb3'Snacks') or (`Meal` = _utf8mb3'Dessert')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dish_meal`
--

LOCK TABLES `Dish_meal` WRITE;
/*!40000 ALTER TABLE `Dish_meal` DISABLE KEYS */;
INSERT INTO `Dish_meal` VALUES ('Brownie','Dessert'),('chicken biryani','Dinner'),('Onion Rings','Snacks'),('Steak','Dinner'),('Steak','Lunch'),('Veg Fried Rice','Dinner'),('Veg Fried Rice','Lunch');
/*!40000 ALTER TABLE `Dish_meal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Employee` (
  `Employee_id` varchar(20) NOT NULL,
  `Branch_id` int NOT NULL,
  `Super_id` varchar(20) NOT NULL,
  `Res` varchar(20) NOT NULL,
  PRIMARY KEY (`Employee_id`),
  KEY `Branch_id` (`Branch_id`),
  KEY `Res` (`Res`),
  CONSTRAINT `Employee_ibfk_1` FOREIGN KEY (`Branch_id`) REFERENCES `Branch` (`Branch_id`),
  CONSTRAINT `Employee_ibfk_2` FOREIGN KEY (`Res`) REFERENCES `Branch` (`Res`),
  CONSTRAINT `Employee_chk_1` CHECK (((substr(`Employee_id`,1,2) = _utf8mb4'WA') or (substr(`Employee_id`,1,2) = _utf8mb4'HC') or (substr(`Employee_id`,1,2) = _utf8mb4'SC') or (substr(`Employee_id`,1,2) = _utf8mb4'MA'))),
  CONSTRAINT `Employee_chk_3` CHECK ((substr(`Super_id`,1,2) = _utf8mb4'MA'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES ('HC11111',123,'MA1111','Pizza Hut 557623'),('HC33333',391,'MA3333','Pizza Hut 557623'),('MA1111',123,'MA1111','Pizza Hut 557623'),('MA3333',391,'MA3333','Pizza Hut 557623'),('SC11112',123,'MA1111','Pizza Hut 557623'),('SC33334',391,'MA3333','Pizza Hut 557623'),('WA11111',123,'MA1111','Pizza Hut 557623'),('WA11112',123,'MA1111','Pizza Hut 557623'),('WA33333',391,'MA3333','Pizza Hut 557623'),('WA33334',391,'MA3333','Pizza Hut 557623');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Feedback`
--

DROP TABLE IF EXISTS `Feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Feedback` (
  `Waiter_id` varchar(20) NOT NULL,
  `Chef_id` varchar(20) NOT NULL,
  `Dish_name` varchar(20) NOT NULL,
  `Phone` char(10) NOT NULL,
  `Entry_time` datetime NOT NULL,
  `Suggestion` varchar(255) DEFAULT NULL,
  `Rating` int NOT NULL,
  PRIMARY KEY (`Waiter_id`,`Chef_id`,`Dish_name`,`Phone`,`Entry_time`),
  KEY `Chef_id` (`Chef_id`),
  KEY `Dish_name` (`Dish_name`),
  KEY `Phone` (`Phone`,`Entry_time`),
  CONSTRAINT `Feedback_ibfk_1` FOREIGN KEY (`Waiter_id`) REFERENCES `Waiter` (`Waiter_id`),
  CONSTRAINT `Feedback_ibfk_2` FOREIGN KEY (`Chef_id`) REFERENCES `Chef` (`Chef_id`),
  CONSTRAINT `Feedback_ibfk_3` FOREIGN KEY (`Dish_name`) REFERENCES `Dish` (`Dish_name`),
  CONSTRAINT `Feedback_ibfk_4` FOREIGN KEY (`Phone`, `Entry_time`) REFERENCES `Customers` (`Phone`, `Entry_time`),
  CONSTRAINT `Feedback_chk_1` CHECK (((`Rating` >= 0) and (`Rating` <= 10)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Feedback`
--

LOCK TABLES `Feedback` WRITE;
/*!40000 ALTER TABLE `Feedback` DISABLE KEYS */;
INSERT INTO `Feedback` VALUES ('WA11111','HC11111','Brownie','6666666666','2020-10-01 21:50:00','Outstanding',10),('WA11112','SC11112','Onion Rings','8888888888','2020-06-21 13:45:56','Very tasty. Will return for these!',9);
/*!40000 ALTER TABLE `Feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager`
--

DROP TABLE IF EXISTS `Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Manager` (
  `Manager_id` varchar(20) NOT NULL,
  PRIMARY KEY (`Manager_id`),
  CONSTRAINT `Manager_ibfk_1` FOREIGN KEY (`Manager_id`) REFERENCES `Employee` (`Employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager`
--

LOCK TABLES `Manager` WRITE;
/*!40000 ALTER TABLE `Manager` DISABLE KEYS */;
INSERT INTO `Manager` VALUES ('MA1111'),('MA3333');
/*!40000 ALTER TABLE `Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recipe`
--

DROP TABLE IF EXISTS `Recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Recipe` (
  `Recipe_name` varchar(20) NOT NULL,
  `Ingredients` varchar(255) NOT NULL,
  PRIMARY KEY (`Recipe_name`,`Ingredients`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recipe`
--

LOCK TABLES `Recipe` WRITE;
/*!40000 ALTER TABLE `Recipe` DISABLE KEYS */;
INSERT INTO `Recipe` VALUES ('Brownie','baking powder'),('Brownie','butter'),('Brownie','chocolate'),('Brownie','egg'),('Brownie','flour'),('Brownie','ice cream'),('Brownie','sugar'),('chicken biryani','chicken'),('chicken biryani','chillies'),('chicken biryani','mint'),('chicken biryani','onion'),('chicken biryani','rice'),('chicken biryani','salt'),('Onion Rings','bread crumbs'),('Onion Rings','egg'),('Onion Rings','flour'),('Onion Rings','oil'),('Onion Rings','onion'),('Onion Rings','salt'),('Steak','beef'),('Steak','butter'),('Steak','garlic'),('Steak','oil'),('Steak','salt'),('Veg fried Rice','beans'),('Veg fried Rice','cabbage'),('Veg fried Rice','carrot'),('Veg fried Rice','peas'),('Veg fried Rice','rice'),('Veg fried Rice','salt');
/*!40000 ALTER TABLE `Recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Restaurant`
--

DROP TABLE IF EXISTS `Restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Restaurant` (
  `cin_num` varchar(20) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cin_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Restaurant`
--

LOCK TABLES `Restaurant` WRITE;
/*!40000 ALTER TABLE `Restaurant` DISABLE KEYS */;
INSERT INTO `Restaurant` VALUES ('Pizza Hut 557623','Pizza Hut');
/*!40000 ALTER TABLE `Restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Waiter`
--

DROP TABLE IF EXISTS `Waiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Waiter` (
  `Waiter_id` varchar(20) NOT NULL,
  PRIMARY KEY (`Waiter_id`),
  CONSTRAINT `Waiter_ibfk_1` FOREIGN KEY (`Waiter_id`) REFERENCES `Employee` (`Employee_id`),
  CONSTRAINT `Waiter_chk_1` CHECK ((substr(`Waiter_id`,1,2) = _utf8mb3'WA'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Waiter`
--

LOCK TABLES `Waiter` WRITE;
/*!40000 ALTER TABLE `Waiter` DISABLE KEYS */;
INSERT INTO `Waiter` VALUES ('WA11111'),('WA11112'),('WA33333'),('WA33334');
/*!40000 ALTER TABLE `Waiter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-04 20:35:47
