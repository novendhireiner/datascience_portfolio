
CREATE DATABASE `tpl2_maturbongs`; 
USE `tpl2_maturbongs`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;
-- Erstellung von Tabelle Abteilung
CREATE TABLE `Abteilung` (
  `ID` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
);
-- Einfügen von beispieldaten in die Tabelle 'Abteilung'
INSERT INTO `Abteilung` VALUES (1,'Vertrieb');
INSERT INTO `Abteilung` VALUES (2,'Marketing');
INSERT INTO `Abteilung` VALUES (3,'IT');

-- Erstellung von Tabelle Mitarbeiter
CREATE TABLE `Mitarbeiter` (
  `ID` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Abteilungs_ID` int NOT NULL,
  
  PRIMARY KEY (`ID`),
  FOREIGN KEY (`Abteilungs_ID`) REFERENCES `Abteilung`(`ID`)
);
-- Als Foreign Key in Tabelle Mitarbeiter wird `Abteilungs_ID`festgelegt, 
-- der auf die `ID`-Spalte der Tabelle `Abteilung` verweist.
-- Damit steht eine Beziehung zwischen beiden Tabellen

-- Einfügen von Beispieldaten in die Tabelle 'Mitarbeiter')
INSERT INTO `Mitarbeiter` VALUES (101,'Max Mustermann', 1);
INSERT INTO `Mitarbeiter` VALUES (102,'Anna Karenina', 2);
INSERT INTO `Mitarbeiter` VALUES (103,'Ludwig Schmidt', 3);





