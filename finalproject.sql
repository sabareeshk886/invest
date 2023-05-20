/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - final project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`final project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `final project`;

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `C_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `base_price` varchar(100) DEFAULT NULL,
  `c_graph` varchar(200) DEFAULT NULL,
  `logo` varchar(30) DEFAULT NULL,
  `c_name` varchar(30) DEFAULT NULL,
  `tax_id` varchar(30) DEFAULT NULL,
  `legal_status` varchar(30) DEFAULT NULL,
  `field_of_business` varchar(30) DEFAULT NULL,
  `registered_office` varchar(30) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `region` varchar(30) DEFAULT NULL,
  `muncipality` varchar(30) DEFAULT NULL,
  `postcode` int(11) DEFAULT NULL,
  `street` varchar(30) DEFAULT NULL,
  `phone_number` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `telephone` int(11) DEFAULT NULL,
  `fax` varchar(30) DEFAULT NULL,
  `postal_address` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `bank_name` varchar(30) DEFAULT NULL,
  `bank_number` bigint(30) DEFAULT NULL,
  `ifsc_code` varchar(30) DEFAULT NULL,
  `director_name` varchar(30) DEFAULT NULL,
  `director_title` varchar(30) DEFAULT NULL,
  `director_surname` varchar(30) DEFAULT NULL,
  `director_dob` varchar(30) DEFAULT NULL,
  `bankguarantee` varchar(30) DEFAULT NULL,
  `proof_of_financialeligibility` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`C_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`C_id`,`l_id`,`base_price`,`c_graph`,`logo`,`c_name`,`tax_id`,`legal_status`,`field_of_business`,`registered_office`,`state`,`region`,`muncipality`,`postcode`,`street`,`phone_number`,`email`,`telephone`,`fax`,`postal_address`,`city`,`country`,`bank_name`,`bank_number`,`ifsc_code`,`director_name`,`director_title`,`director_surname`,`director_dob`,`bankguarantee`,`proof_of_financialeligibility`,`status`) values 
(1,2,'200',NULL,'/static/company/LOGO/20230406-','abc','4565454','approved','it','kochi','kerala','india','kochi',676102,'kakkanad',2147483647,'abc@gmail.com',2147483647,'53654','abc,kakkanad,kochi','kochi','india','pnb',45632514125689,'punb01563','sabareesh','sabareesh','sabareesh','sabareesh','/static/company/BANK_PROOF/202','/static/company/PROOF/20230406','approved'),
(2,3,'300',NULL,'pending','xyz','654','approved','tax','tvm','kerala','india','tvm',652485,'tvm',2147483647,'xyz@gmail.com',564253552,'5698','xyz,tvm','tvm','india','sbi',5652365244563,'sbi564','sadeeed','ceo','m','06/05/2000',NULL,NULL,'approved'),
(3,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL,'\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"',0,'\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL),
(4,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL,'\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"',0,'\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL),
(5,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL,'\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"',0,'\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL),
(6,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"',0,'\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL),
(7,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"',0,'\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`date`,`user_id`,`complaint`,`reply`,`status`) values 
(1,'2023-02-01',1,'dfdgdgvdwkhv','','pending'),
(2,'2023-06-29',2,'kugyduygb','ok','replied');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `feedback` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`date`,`feedback`) values 
(1,1,'2023-01-02','hi hello dhdowfwdohwodhedwoi'),
(2,2,'2023-03-15','hhddgeifheivheievh');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'abc','123','company'),
(3,'xyz','123','company');

/*Table structure for table `newsfeed` */

DROP TABLE IF EXISTS `newsfeed`;

CREATE TABLE `newsfeed` (
  `newsfeed_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) DEFAULT NULL,
  `news_content` varchar(200) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`newsfeed_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `newsfeed` */

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` varchar(50) DEFAULT NULL,
  `available_lots` varchar(50) DEFAULT NULL,
  `total_price` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `orders` */

insert  into `orders`(`order_id`,`c_id`,`available_lots`,`total_price`,`quantity`) values 
(1,'1','5',200,10),
(2,'2','55',500,55),
(3,'3',NULL,NULL,NULL);

/*Table structure for table `trader` */

DROP TABLE IF EXISTS `trader`;

CREATE TABLE `trader` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `user_name` varchar(30) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `pan` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `marital_status` varchar(50) DEFAULT NULL,
  `annual_income` int(50) DEFAULT NULL,
  `trading_experience` varchar(50) DEFAULT NULL,
  `occuppation` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `accountholder_name` varchar(50) DEFAULT NULL,
  `ifsc_code` varchar(50) DEFAULT NULL,
  `account_number` int(11) DEFAULT NULL,
  `account_type` varchar(50) DEFAULT NULL,
  `signature` varchar(150) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `income_proof` varchar(200) DEFAULT NULL,
  `incomeproof_type` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `trader` */

insert  into `trader`(`user_id`,`l_id`,`user_name`,`address`,`pan`,`dob`,`contact`,`email`,`gender`,`marital_status`,`annual_income`,`trading_experience`,`occuppation`,`country`,`accountholder_name`,`ifsc_code`,`account_number`,`account_type`,`signature`,`photo`,`income_proof`,`incomeproof_type`,`location`) values 
(1,1,'sid',NULL,NULL,NULL,2147483647,'dfgf@gmail.com',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(2,2,'raj',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `watchlist` */

DROP TABLE IF EXISTS `watchlist`;

CREATE TABLE `watchlist` (
  `watch_id` int(11) DEFAULT NULL,
  `c_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `watchlist` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
