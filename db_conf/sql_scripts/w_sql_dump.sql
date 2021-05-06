-- MySQL dump 10.13  Distrib 5.7.33, for Linux (x86_64)
--
-- Host: localhost    Database: weather_api_db
-- ------------------------------------------------------
-- Server version       5.7.33

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add telegram',7,'add_telegram'),(26,'Can change telegram',7,'change_telegram'),(27,'Can delete telegram',7,'delete_telegram'),(28,'Can view telegram',7,'view_telegram'),(29,'Can add town',8,'add_town'),(30,'Can change town',8,'change_town'),(31,'Can delete town',8,'delete_town'),(32,'Can view town',8,'view_town'),(33,'Can add weather wb',9,'add_weatherwb'),(34,'Can change weather wb',9,'change_weatherwb'),(35,'Can delete weather wb',9,'delete_weatherwb'),(36,'Can view weather wb',9,'view_weatherwb'),(37,'Can add weather owm',10,'add_weatherowm'),(38,'Can change weather owm',10,'change_weatherowm'),(39,'Can delete weather owm',10,'delete_weatherowm'),(40,'Can view weather owm',10,'view_weatherowm'),(41,'Can add coord',11,'add_coord'),(42,'Can change coord',11,'change_coord'),(43,'Can delete coord',11,'delete_coord'),(44,'Can view coord',11,'view_coord');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coord`
--

DROP TABLE IF EXISTS `coord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` varchar(45) NOT NULL,
  `longitude` varchar(45) NOT NULL,
  `town_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `coord_town_id_6d3b80dd_fk_town_id` (`town_id`),
  CONSTRAINT `coord_town_id_6d3b80dd_fk_town_id` FOREIGN KEY (`town_id`) REFERENCES `town` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coord`
--

LOCK TABLES `coord` WRITE;
/*!40000 ALTER TABLE `coord` DISABLE KEYS */;
INSERT INTO `coord` VALUES (1,'55.7522','37.6156',1),(2,'59.8944','30.2642',2),(3,'55.0411','82.9344',3),(4,'56.8575','60.6125',4),(5,'55.7887','49.1221',5),(6,'55.1544','61.4297',6),(7,'48.7194','44.5018',7),(8,'53.4186','59.0472',8),(9,'55.3333','86.0833',9),(10,'56.1366','40.3966',10),(11,'55.7522','37.6156',1),(12,'59.8944','30.2642',2),(13,'55.0411','82.9344',3),(14,'56.8575','60.6125',4),(15,'55.7887','49.1221',5),(16,'55.1544','61.4297',6),(17,'48.7194','44.5018',7),(18,'53.4186','59.0472',8),(19,'55.3333','86.0833',9),(20,'56.1366','40.3966',10),(21,'55.7522','37.6156',1),(22,'59.8944','30.2642',2),(23,'55.0411','82.9344',3),(24,'56.8575','60.6125',4),(25,'55.7887','49.1221',5),(26,'55.1544','61.4297',6),(27,'48.7194','44.5018',7),(28,'53.4186','59.0472',8),(29,'55.3333','86.0833',9),(30,'56.1366','40.3966',10),(31,'55.7522','37.6156',1),(32,'59.8944','30.2642',2),(33,'55.0411','82.9344',3),(34,'56.8575','60.6125',4),(35,'55.7887','49.1221',5),(36,'55.1544','61.4297',6),(37,'48.7194','44.5018',7),(38,'53.4186','59.0472',8),(39,'55.3333','86.0833',9),(40,'56.1366','40.3966',10),(41,'55.7522','37.6156',1),(42,'55.7522','37.6156',1),(43,'59.8944','30.2642',2),(44,'55.0411','82.9344',3),(45,'56.8575','60.6125',4),(46,'55.7887','49.1221',5),(47,'55.1544','61.4297',6),(48,'48.7194','44.5018',7),(49,'53.4186','59.0472',8),(50,'55.3333','86.0833',9),(51,'56.1366','40.3966',10);
/*!40000 ALTER TABLE `coord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(11,'api','coord'),(7,'api','telegram'),(8,'api','town'),(10,'api','weatherowm'),(9,'api','weatherwb'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-05-05 11:04:34.062497'),(2,'auth','0001_initial','2021-05-05 11:04:34.187117'),(3,'admin','0001_initial','2021-05-05 11:04:34.476196'),(4,'admin','0002_logentry_remove_auto_add','2021-05-05 11:04:34.552713'),(5,'admin','0003_logentry_add_action_flag_choices','2021-05-05 11:04:34.566406'),(6,'api','0001_initial','2021-05-05 11:04:34.706535'),(7,'contenttypes','0002_remove_content_type_name','2021-05-05 11:04:34.903520'),(8,'auth','0002_alter_permission_name_max_length','2021-05-05 11:04:34.917165'),(9,'auth','0003_alter_user_email_max_length','2021-05-05 11:04:34.937328'),(10,'auth','0004_alter_user_username_opts','2021-05-05 11:04:34.950757'),(11,'auth','0005_alter_user_last_login_null','2021-05-05 11:04:34.992429'),(12,'auth','0006_require_contenttypes_0002','2021-05-05 11:04:34.996562'),(13,'auth','0007_alter_validators_add_error_messages','2021-05-05 11:04:35.006810'),(14,'auth','0008_alter_user_username_max_length','2021-05-05 11:04:35.025853'),(15,'auth','0009_alter_user_last_name_max_length','2021-05-05 11:04:35.044465'),(16,'auth','0010_alter_group_name_max_length','2021-05-05 11:04:35.063048'),(17,'auth','0011_update_proxy_permissions','2021-05-05 11:04:35.081956'),(18,'sessions','0001_initial','2021-05-05 11:04:35.111125'),(19,'api','0002_auto_20210505_1716','2021-05-05 17:16:24.357554');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telegram`
--

DROP TABLE IF EXISTS `telegram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `telegram` (
  `id` int(10) unsigned NOT NULL,
  `username` varchar(45) NOT NULL,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `create_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `delete_dt` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telegram`
--

LOCK TABLES `telegram` WRITE;
/*!40000 ALTER TABLE `telegram` DISABLE KEYS */;
/*!40000 ALTER TABLE `telegram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `town`
--

DROP TABLE IF EXISTS `town`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `town` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `town`
--

LOCK TABLES `town` WRITE;
/*!40000 ALTER TABLE `town` DISABLE KEYS */;
INSERT INTO `town` VALUES (6,'Chelyabinsk'),(5,'Kazan'),(9,'Kemerovo'),(8,'Magnitogorsk'),(1,'Moscow'),(3,'Novosibirsk'),(2,'Saint Petersburg'),(10,'Vladimir'),(7,'Volgograd'),(4,'Yekaterinburg');
/*!40000 ALTER TABLE `town` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weather_owm`
--

DROP TABLE IF EXISTS `weather_owm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weather_owm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_ts` datetime(6) NOT NULL,
  `temperature` decimal(4,2) NOT NULL,
  `create_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `delete_dt` datetime(6) DEFAULT NULL,
  `town_id` int(11) NOT NULL,
  `site` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `weather_owm_town_id_a91280e6_fk_town_id` (`town_id`),
  CONSTRAINT `weather_owm_town_id_a91280e6_fk_town_id` FOREIGN KEY (`town_id`) REFERENCES `town` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weather_owm`
--

LOCK TABLES `weather_owm` WRITE;
/*!40000 ALTER TABLE `weather_owm` DISABLE KEYS */;
INSERT INTO `weather_owm` VALUES (1,'2021-05-05 14:44:29.425000',10.54,NULL,NULL,NULL,1,'weatherowm'),(2,'2021-05-05 14:44:29.425000',5.31,NULL,NULL,NULL,2,'weatherowm'),(3,'2021-05-05 14:44:29.425000',16.00,NULL,NULL,NULL,3,'weatherowm'),(4,'2021-05-05 14:44:29.425000',18.00,NULL,NULL,NULL,4,'weatherowm'),(5,'2021-05-05 14:44:29.425000',10.00,NULL,NULL,NULL,5,'weatherowm'),(6,'2021-05-05 14:44:29.425000',20.00,NULL,NULL,NULL,6,'weatherowm'),(7,'2021-05-05 14:44:29.425000',16.83,NULL,NULL,NULL,7,'weatherowm'),(8,'2021-05-05 14:44:29.425000',12.00,NULL,NULL,NULL,8,'weatherowm'),(9,'2021-05-05 14:44:29.425000',14.00,NULL,NULL,NULL,9,'weatherowm'),(10,'2021-05-05 14:44:29.425000',10.46,NULL,NULL,NULL,10,'weatherowm'),(11,'2021-05-05 14:59:52.611000',10.53,NULL,NULL,NULL,1,'weatherowm'),(12,'2021-05-05 14:59:52.611000',5.00,NULL,NULL,NULL,2,'weatherowm'),(13,'2021-05-05 14:59:52.611000',16.00,NULL,NULL,NULL,3,'weatherowm'),(14,'2021-05-05 14:59:52.611000',17.00,NULL,NULL,NULL,4,'weatherowm'),(15,'2021-05-05 14:59:52.611000',9.00,NULL,NULL,NULL,5,'weatherowm'),(16,'2021-05-05 14:59:52.611000',20.00,NULL,NULL,NULL,6,'weatherowm'),(17,'2021-05-05 14:59:52.611000',16.84,NULL,NULL,NULL,7,'weatherowm'),(18,'2021-05-05 14:59:52.611000',12.00,NULL,NULL,NULL,8,'weatherowm'),(19,'2021-05-05 14:59:52.611000',13.00,NULL,NULL,NULL,9,'weatherowm'),(20,'2021-05-05 14:59:52.611000',10.46,NULL,NULL,NULL,10,'weatherowm'),(21,'2021-05-05 15:02:37.511000',10.53,NULL,NULL,NULL,1,'weatherowm'),(22,'2021-05-05 15:02:37.511000',5.00,NULL,NULL,NULL,2,'weatherowm'),(23,'2021-05-05 15:02:37.511000',16.00,NULL,NULL,NULL,3,'weatherowm'),(24,'2021-05-05 15:02:37.511000',17.00,NULL,NULL,NULL,4,'weatherowm'),(25,'2021-05-05 15:02:37.511000',9.00,NULL,NULL,NULL,5,'weatherowm'),(26,'2021-05-05 15:02:37.511000',20.00,NULL,NULL,NULL,6,'weatherowm'),(27,'2021-05-05 15:02:37.511000',16.84,NULL,NULL,NULL,7,'weatherowm'),(28,'2021-05-05 15:02:37.511000',12.00,NULL,NULL,NULL,8,'weatherowm'),(29,'2021-05-05 15:02:37.511000',13.00,NULL,NULL,NULL,9,'weatherowm'),(30,'2021-05-05 15:02:37.511000',10.46,NULL,NULL,NULL,10,'weatherowm'),(31,'2021-05-05 15:06:10.615000',10.53,NULL,NULL,NULL,1,'weatherowm'),(32,'2021-05-05 15:06:10.615000',5.00,NULL,NULL,NULL,2,'weatherowm'),(33,'2021-05-05 15:06:10.615000',16.00,NULL,NULL,NULL,3,'weatherowm'),(34,'2021-05-05 15:06:10.615000',17.00,NULL,NULL,NULL,4,'weatherowm'),(35,'2021-05-05 15:06:10.615000',9.00,NULL,NULL,NULL,5,'weatherowm'),(36,'2021-05-05 15:06:10.615000',20.00,NULL,NULL,NULL,6,'weatherowm'),(37,'2021-05-05 15:06:10.615000',16.84,NULL,NULL,NULL,7,'weatherowm'),(38,'2021-05-05 15:06:10.615000',12.00,NULL,NULL,NULL,8,'weatherowm'),(39,'2021-05-05 15:06:10.615000',13.00,NULL,NULL,NULL,9,'weatherowm'),(40,'2021-05-05 15:06:10.615000',10.46,NULL,NULL,NULL,10,'weatherowm'),(41,'2021-05-05 15:09:51.211563',10.53,NULL,NULL,NULL,1,'weatherowm'),(42,'2021-05-05 15:09:51.211563',5.00,NULL,NULL,NULL,2,'weatherowm'),(43,'2021-05-05 15:09:51.211563',16.00,NULL,NULL,NULL,3,'weatherowm'),(44,'2021-05-05 15:09:51.211563',17.00,NULL,NULL,NULL,4,'weatherowm'),(45,'2021-05-05 15:09:51.211563',9.00,NULL,NULL,NULL,5,'weatherowm'),(46,'2021-05-05 15:09:51.211563',20.00,NULL,NULL,NULL,6,'weatherowm'),(47,'2021-05-05 15:09:51.211563',16.84,NULL,NULL,NULL,7,'weatherowm'),(48,'2021-05-05 15:09:51.211563',12.00,NULL,NULL,NULL,8,'weatherowm'),(49,'2021-05-05 15:09:51.211563',13.00,NULL,NULL,NULL,9,'weatherowm'),(50,'2021-05-05 15:09:51.211563',10.46,NULL,NULL,NULL,10,'weatherowm'),(51,'2021-05-05 15:14:13.809542',10.33,NULL,NULL,NULL,1,'weatherowm'),(52,'2021-05-05 15:14:13.809542',4.85,NULL,NULL,NULL,2,'weatherowm'),(53,'2021-05-05 15:14:13.809542',16.00,NULL,NULL,NULL,3,'weatherowm'),(54,'2021-05-05 15:14:13.809542',17.00,NULL,NULL,NULL,4,'weatherowm'),(55,'2021-05-05 15:14:13.809542',9.00,NULL,NULL,NULL,5,'weatherowm'),(56,'2021-05-05 15:14:13.809542',20.00,NULL,NULL,NULL,6,'weatherowm'),(57,'2021-05-05 15:14:13.809542',16.84,NULL,NULL,NULL,7,'weatherowm'),(58,'2021-05-05 15:14:13.809542',12.00,NULL,NULL,NULL,8,'weatherowm'),(59,'2021-05-05 15:14:13.809542',13.00,NULL,NULL,NULL,9,'weatherowm'),(60,'2021-05-05 15:14:13.809542',10.46,NULL,NULL,NULL,10,'weatherowm'),(61,'2021-05-05 16:58:44.581000',10.30,NULL,NULL,NULL,1,'weatherowm'),(62,'2021-05-05 16:58:44.884000',4.65,NULL,NULL,NULL,2,'weatherowm'),(63,'2021-05-05 16:58:45.100000',13.00,NULL,NULL,NULL,3,'weatherowm'),(64,'2021-05-05 16:58:45.324000',12.00,NULL,NULL,NULL,4,'weatherowm'),(65,'2021-05-05 16:58:45.531000',8.00,NULL,NULL,NULL,5,'weatherowm'),(66,'2021-05-05 16:58:45.770000',16.00,NULL,NULL,NULL,6,'weatherowm'),(67,'2021-05-05 16:58:45.992000',13.95,NULL,NULL,NULL,7,'weatherowm'),(68,'2021-05-05 16:58:46.400000',10.00,NULL,NULL,NULL,8,'weatherowm'),(69,'2021-05-05 16:58:46.759000',12.00,NULL,NULL,NULL,9,'weatherowm'),(70,'2021-05-05 16:58:46.989000',7.41,NULL,NULL,NULL,10,'weatherowm');
/*!40000 ALTER TABLE `weather_owm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weather_wb`
--

DROP TABLE IF EXISTS `weather_wb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weather_wb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_ts` datetime(6) NOT NULL,
  `temperature` decimal(4,2) NOT NULL,
  `create_dt` datetime(6) DEFAULT NULL,
  `update_dt` datetime(6) DEFAULT NULL,
  `delete_dt` datetime(6) DEFAULT NULL,
  `town_id` int(11) NOT NULL,
  `site` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `weather_wb_town_id_5ef56b4b_fk_town_id` (`town_id`),
  CONSTRAINT `weather_wb_town_id_5ef56b4b_fk_town_id` FOREIGN KEY (`town_id`) REFERENCES `town` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weather_wb`
--

LOCK TABLES `weather_wb` WRITE;
/*!40000 ALTER TABLE `weather_wb` DISABLE KEYS */;
INSERT INTO `weather_wb` VALUES (1,'2021-05-05 16:58:50.430000',12.00,NULL,NULL,NULL,1,'weatherwb'),(2,'2021-05-05 16:58:50.745000',5.00,NULL,NULL,NULL,2,'weatherwb'),(3,'2021-05-05 16:58:51.058000',13.00,NULL,NULL,NULL,3,'weatherwb'),(4,'2021-05-05 16:58:51.353000',13.00,NULL,NULL,NULL,4,'weatherwb'),(5,'2021-05-05 16:58:51.660000',8.00,NULL,NULL,NULL,5,'weatherwb'),(6,'2021-05-05 16:58:51.971000',16.00,NULL,NULL,NULL,6,'weatherwb'),(7,'2021-05-05 16:58:52.265000',14.00,NULL,NULL,NULL,7,'weatherwb'),(8,'2021-05-05 16:58:52.562000',10.00,NULL,NULL,NULL,8,'weatherwb'),(9,'2021-05-05 16:58:52.862000',12.00,NULL,NULL,NULL,9,'weatherwb'),(10,'2021-05-05 16:58:53.202000',6.80,NULL,NULL,NULL,10,'weatherwb');
/*!40000 ALTER TABLE `weather_wb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-05 18:16:42
