CREATE DATABASE `uni`; 
USE `uni`;

-- Erstellung von Tabelle "Studierende"
CREATE TABLE Studierende (
    Matrikelnummer INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255)
);
-- Datensätze einfügen
INSERT INTO Studierende (Matrikelnummer, Name, Email) VALUES
    (1, 'Max Mustermann', 'max.mustermann@uni.de'),
    (2, 'Anna Mariposa', 'anna.mariposa@uni.de'),
    (3, 'Jean Paul', 'jean.paul@uni.de'),
    (4, 'Ludwig Schmidt', 'ludwig.schmidt@uni.de');

-- Erstellung von Tabelle "Kurse"
CREATE TABLE Kurse (
    KursID INT PRIMARY KEY,
    Titel VARCHAR(255),
    Dozent VARCHAR(255)
);
-- Datensätze einfügen
INSERT INTO Kurse (KursID, Titel, Dozent) VALUES
    (101, 'Mathematik I', 'Prof. Müller'),
    (102, 'Informatik Grundlagen', 'Prof. Schmidt'),
    (103, 'Statistik I', 'Prof. Wazowski'),
    (104, 'Künstliche Intelligenz Grundlagen', 'Prof. Karenina');
    

-- Erstellung von Tabelle "Einschreibungen"
CREATE TABLE Einschreibungen (
    Matrikelnummer INT,
    KursID INT,
    Semester VARCHAR(50),
    PRIMARY KEY (Matrikelnummer, KursID),
    FOREIGN KEY (Matrikelnummer) REFERENCES Studierende(Matrikelnummer),
    FOREIGN KEY (KursID) REFERENCES Kurse(KursID)
);

-- Datensätze einfügen
INSERT INTO Einschreibungen (Matrikelnummer, KursID, Semester) VALUES
    (1, 101, 'Wintersemester 2023'),
    (1, 102, 'Wintersemester 2023'),
    (2, 102, 'Wintersemester 2023'),
    (2, 103, 'Wintersemester 2023'),
    (3, 103, 'Wintersemester 2023'),
    (3, 104, 'Wintersemester 2023'),
    (4, 101, 'Wintersemester 2023'),
    (4, 104, 'Wintersemester 2023');

-- SELECT-Anweisung
SELECT
    Studierende.Matrikelnummer,
    Studierende.Name,
    Kurse.Titel,
    Einschreibungen.Semester
FROM
    Studierende
JOIN Einschreibungen ON Studierende.Matrikelnummer = Einschreibungen.Matrikelnummer
JOIN Kurse ON Einschreibungen.KursID = Kurse.KursID;
