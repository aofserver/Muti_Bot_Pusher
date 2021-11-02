-- --------------------------------------------------------
-- Host:                         178.128.87.57
-- Server version:               5.7.33-0ubuntu0.16.04.1 - (Ubuntu)
-- Server OS:                    Linux
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for line_test
CREATE DATABASE IF NOT EXISTS `line_test` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `line_test`;

-- Dumping structure for table line_test.app_enpointbot
CREATE TABLE IF NOT EXISTS `app_enpointbot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `endpoint` varchar(50) DEFAULT NULL,
  `timestamp` datetime(6) DEFAULT NULL,
  `bot_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_enpointbot_bot_id_d17966c3_fk_app_profilebot_id` (`bot_id`),
  CONSTRAINT `app_enpointbot_bot_id_d17966c3_fk_app_profilebot_id` FOREIGN KEY (`bot_id`) REFERENCES `app_profilebot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table line_test.app_enpointbot: ~2 rows (approximately)
/*!40000 ALTER TABLE `app_enpointbot` DISABLE KEYS */;
REPLACE INTO `app_enpointbot` (`id`, `endpoint`, `timestamp`, `bot_id`) VALUES
	(1, 'http://localhost:8001', '2021-10-14 17:40:01.000000', 1),
	(2, 'http://localhost:8002', '2021-10-14 17:40:17.000000', 2);
/*!40000 ALTER TABLE `app_enpointbot` ENABLE KEYS */;

-- Dumping structure for table line_test.app_messagedata
CREATE TABLE IF NOT EXISTS `app_messagedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `send_from` varchar(50) DEFAULT NULL,
  `receive` varchar(50) DEFAULT NULL,
  `type_message` varchar(100) DEFAULT NULL,
  `message` json DEFAULT NULL,
  `bot_id` int(11) NOT NULL,
  `timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_messagedata_bot_id_cf03b422_fk_app_profilebot_id` (`bot_id`),
  CONSTRAINT `app_messagedata_bot_id_cf03b422_fk_app_profilebot_id` FOREIGN KEY (`bot_id`) REFERENCES `app_profilebot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=222 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table line_test.app_messagedata: ~23 rows (approximately)
/*!40000 ALTER TABLE `app_messagedata` DISABLE KEYS */;
REPLACE INTO `app_messagedata` (`id`, `send_from`, `receive`, `type_message`, `message`, `bot_id`, `timestamp`) VALUES
	(159, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'text', '{"data": "สวัสดีครับ สนใจซื้อสินค้า A ครับ"}', 1, '2021-10-12 06:09:01.937161'),
	(160, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "สวัสดีครับ ต้องการสั่งซื้อสินค้าชิ้นไหนสอบถามได้เลยครับ"}', 1, '2021-10-12 06:09:01.976291'),
	(161, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "สินค้า A ราคา 100 บาทครับ"}', 1, '2021-10-12 06:09:18.912709'),
	(162, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'text', '{"data": "เอา 1 ชิ้นครับ"}', 1, '2021-10-12 06:09:37.753429'),
	(163, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "ชำระเงินมาที่ธนาคาร AAA นะครับ"}', 1, '2021-10-12 06:09:56.548235'),
	(164, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'text', '{"data": "หวัดดีครับบ"}', 2, '2021-10-12 06:10:06.772665'),
	(165, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "สวัสดีครับ ต้องการสั่งซื้อสินค้าชิ้นไหนสอบถามได้เลยครับ"}', 2, '2021-10-12 06:10:06.855936'),
	(166, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'text', '{"data": "สนใจสินค้า B ครับ"}', 2, '2021-10-12 06:10:16.831894'),
	(167, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "สินค้า B 50 บาทครับ"}', 2, '2021-10-12 06:10:35.539896'),
	(168, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "ชำระเงินที่ธนาคาร AAA ได้เลยครับ"}', 2, '2021-10-12 06:11:01.345671'),
	(169, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'image', '{"data": "https://lineapibkk.obs.ap-southeast-2.myhuaweicloud.com/@678tbhfr/U12162f974ac7a21fc1887b172755cca1/U12162f974ac7a21fc1887b172755cca1_1634019067.9862053.png"}', 1, '2021-10-12 06:11:08.926065'),
	(170, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "ได้รับสลิปจากท่านแล้ว ทางเรากำลังอยู่ระะหว่างการดำเนินการตรวจสอบ"}', 1, '2021-10-12 06:11:08.955498'),
	(171, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'text', '{"data": "โอนแล้วครับ"}', 1, '2021-10-12 06:11:14.173134'),
	(172, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'image', '{"data": "https://lineapibkk.obs.ap-southeast-2.myhuaweicloud.com/@771ftsqt/U12162f974ac7a21fc1887b172755cca1/U12162f974ac7a21fc1887b172755cca1_1634019091.3923397.png"}', 2, '2021-10-12 06:11:32.410892'),
	(173, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "ได้รับสลิปจากท่านแล้ว ทางเรากำลังอยู่ระะหว่างการดำเนินการตรวจสอบ"}', 2, '2021-10-12 06:11:32.468415'),
	(174, 'U12162f974ac7a21fc1887b172755cca1', 'admin', 'text', '{"data": "โอนแล้วครับรับ 1 ชิ้นครับ"}', 2, '2021-10-12 06:11:42.277183'),
	(175, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "ขอบคุณครับ"}', 2, '2021-10-12 06:11:57.088756'),
	(216, 'admin', 'U12162f974ac7a21fc1887b172755cca1', 'text', '{"data": "hi"}', 1, '2021-10-21 10:34:01.691468'),
	(217, 'U4afc69c818cb8946948d8afd7ed75f2e', 'admin', 'text', '{"data": "Test"}', 1, '2021-11-02 08:15:18.174761'),
	(218, 'U4afc69c818cb8946948d8afd7ed75f2e', 'admin', 'text', '{"data": "Hello"}', 1, '2021-11-02 08:16:09.520650'),
	(219, 'admin', 'U4afc69c818cb8946948d8afd7ed75f2e', 'text', '{"data": "send"}', 1, '2021-11-02 08:16:17.576579'),
	(220, 'admin', 'U4afc69c818cb8946948d8afd7ed75f2e', 'text', '{"data": "test"}', 1, '2021-11-02 08:16:50.328913'),
	(221, 'admin', 'U4afc69c818cb8946948d8afd7ed75f2e', 'text', '{"data": "yes"}', 1, '2021-11-02 08:18:30.393088');
/*!40000 ALTER TABLE `app_messagedata` ENABLE KEYS */;

-- Dumping structure for table line_test.app_profilebot
CREATE TABLE IF NOT EXISTS `app_profilebot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `botid` varchar(20) DEFAULT NULL,
  `botname` varchar(50) DEFAULT NULL,
  `botdetail` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table line_test.app_profilebot: ~2 rows (approximately)
/*!40000 ALTER TABLE `app_profilebot` DISABLE KEYS */;
REPLACE INTO `app_profilebot` (`id`, `botid`, `botname`, `botdetail`, `timestamp`) VALUES
	(1, '@678tbhfr', 'Bot test', NULL, '2021-10-11 19:22:53.000000'),
	(2, '@771ftsqt', 'Bot test2', NULL, '2021-10-12 11:06:02.000000');
/*!40000 ALTER TABLE `app_profilebot` ENABLE KEYS */;

-- Dumping structure for table line_test.app_profileuser
CREATE TABLE IF NOT EXISTS `app_profileuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(50) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `userdetail` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) DEFAULT NULL,
  `bot_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_profileuser_bot_id_ef3aeecd_fk_app_profilebot_id` (`bot_id`),
  CONSTRAINT `app_profileuser_bot_id_ef3aeecd_fk_app_profilebot_id` FOREIGN KEY (`bot_id`) REFERENCES `app_profilebot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table line_test.app_profileuser: ~3 rows (approximately)
/*!40000 ALTER TABLE `app_profileuser` DISABLE KEYS */;
REPLACE INTO `app_profileuser` (`id`, `userid`, `username`, `userdetail`, `timestamp`, `bot_id`) VALUES
	(1, 'U12162f974ac7a21fc1887b172755cca1', 'My name is aof', '', '2021-10-11 12:23:19.543856', 1),
	(2, 'U12162f974ac7a21fc1887b172755cca1', 'My name is aof', '', '2021-10-14 08:03:13.397621', 2),
	(3, 'U4afc69c818cb8946948d8afd7ed75f2e', 'ten', '', '2021-11-02 08:15:18.168663', 1);
/*!40000 ALTER TABLE `app_profileuser` ENABLE KEYS */;

-- Dumping structure for table line_test.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table line_test.django_migrations: ~3 rows (approximately)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
REPLACE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(20, 'app', '0001_initial', '2021-10-11 14:00:43.873685'),
	(21, 'app', '0002_auto_20211012_0150', '2021-10-11 18:50:24.282343'),
	(22, 'app', '0003_enpointbot', '2021-10-14 10:39:15.517950');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
