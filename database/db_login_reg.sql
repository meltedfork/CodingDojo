-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: users
-- ------------------------------------------------------
-- Server version	5.7.21

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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(16) NOT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(32) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idl_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Jack','Hyc','hi@jack.com','jackattack','2018-02-15 17:37:39',NULL),(2,'Vanessa','Esterbrook','hi@van.com','vavavoom','2018-02-15 17:37:39',NULL),(3,'Suzanne','Salerno','hi@suz.com','ssssss','2018-02-15 17:37:39',NULL),(4,'Michael','Werner','mmwerner92@gmail.com','stuff','2018-02-15 18:52:45','2018-02-15 12:52:45'),(5,'Lee','Werner','lmwerner92@gmail.com','stuff2','2018-02-15 18:55:13','2018-02-15 12:55:13'),(6,'cat','dog','woof@meow.com','cfa590c5b4c51852821cc9a7669cfcd1','2018-02-15 19:01:50','2018-02-15 13:01:50'),(7,'Man','Bearpig','mbp@gmail.com','9c1ab102bcbdf9398ab6e85710d6deed','2018-02-15 19:48:19','2018-02-15 13:48:19'),(8,'Kimberly','werner','kwerner@gmail.com','c13d88cb4cb02003daedb8a84e5d272a','2018-02-15 19:58:27','2018-02-15 13:58:27'),(10,'Diane','Hyc','dhyc@gmail.com','79370fb45e3573eac897e709c5728fea','2018-02-15 21:50:47','2018-02-15 15:50:47'),(11,'New','User','newuser@gmail.com','48cccca3bab2ad18832233ee8dff1b0b','2018-02-15 21:59:41','2018-02-15 15:59:41'),(12,'Newer','User','neweruser@gmail.com','e18ee67232545172093ce053ae9d2c73','2018-02-15 22:04:06','2018-02-15 16:04:06'),(13,'Newest','User','newestuser@gmail.com','e18ee67232545172093ce053ae9d2c73','2018-02-15 22:08:53','2018-02-15 16:08:53'),(14,'Newestest','User','nuser@gmail.com','25d55ad283aa400af464c76d713c07ad','2018-02-15 22:21:46','2018-02-15 16:21:46'),(15,'Userr','User','useruser@gmail.com','25d55ad283aa400af464c76d713c07ad','2018-02-15 22:24:52','2018-02-15 16:24:52'),(16,'Suzanne','Salerno','suzsalerno@gmail.com','25d55ad283aa400af464c76d713c07ad','2018-02-15 23:38:03','2018-02-15 17:38:03');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-15 20:50:24
