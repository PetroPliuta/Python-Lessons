-- phpMyAdmin SQL Dump
-- version 3.2.3
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 04, 2012 at 09:56 AM
-- Server version: 5.1.40
-- PHP Version: 5.2.12

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `sql`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE IF NOT EXISTS `customers` (
  `cnum` smallint(5) unsigned NOT NULL,
  `cname` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `rating` smallint(5) unsigned NOT NULL,
  `snum` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`cnum`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`cnum`, `cname`, `city`, `rating`, `snum`) VALUES
(2001, 'Hoffman', 'London', 100, 1001),
(2002, 'Giovanni', 'New York', 200, 1003),
(2003, 'Liu', 'San Jose', 200, 1002),
(2004, 'Grass', 'San Jose', 300, 1002),
(2006, 'Clemens', 'London', 100, 1001),
(2008, 'Cisneros', 'Barcelona', 300, 1007),
(2007, 'Pereira', 'London', 100, 1004);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE IF NOT EXISTS `orders` (
  `onum` smallint(5) unsigned NOT NULL,
  `amt` decimal(6,2) unsigned NOT NULL,
  `odate` date NOT NULL,
  `cnum` smallint(5) unsigned NOT NULL,
  `snum` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`onum`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`onum`, `amt`, `odate`, `cnum`, `snum`) VALUES
(3001, 18.69, '1990-03-10', 2008, 1007),
(3003, 767.19, '1990-03-10', 2001, 1001),
(3002, 1900.10, '1990-03-10', 2007, 1004),
(3005, 5160.45, '1990-03-10', 2003, 1002),
(3006, 1098.16, '1990-03-10', 2008, 1007),
(3009, 1713.23, '1990-04-10', 2002, 1003),
(3007, 75.75, '1990-04-10', 2004, 1002),
(3008, 4723.00, '1990-05-10', 2006, 1001),
(3010, 1309.95, '1990-06-10', 2004, 1002),
(3011, 9891.88, '1990-06-10', 2006, 1001);

-- --------------------------------------------------------

--
-- Table structure for table `salers`
--

CREATE TABLE IF NOT EXISTS `salers` (
  `snum` smallint(5) unsigned NOT NULL,
  `sname` varchar(50) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `comm` decimal(3,2) NOT NULL,
  PRIMARY KEY (`snum`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `salers`
--

INSERT INTO `salers` (`snum`, `sname`, `city`, `comm`) VALUES
(1001, 'Peel', 'London', 0.12),
(1002, 'Serres', 'San Jose', 0.13),
(1004, 'Motika', 'London', 0.11),
(1007, 'Rifkin', 'Barcelona', 0.15),
(1003, 'Axelrod', 'New York', 0.10),
(1111, 'Иванов', 'Киев', 0.25),
(1112, NULL, 'Paris', 0.15),
(1115, 'd''Artanian', 'Paris', 0.10),
(1117, 'Sifkin', 'San Jose', 0.17);
