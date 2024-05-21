CREATE DATABASE `firma`; 
USE `firma`;

-- Erstellung von Tabelle "Kunden"
CREATE TABLE Kunden (
    KundenID INT PRIMARY KEY,
    Name VARCHAR(255),
    Land VARCHAR(50)
);

-- Einfügen einigen Datensätze in die Tabelle "Kunden"
INSERT INTO Kunden VALUES (1, 'Max Mustermann', 'Deutschland');
INSERT INTO Kunden VALUES (2, 'Anna Mariposa', 'USA');
INSERT INTO Kunden VALUES (3, 'Jean Paul', 'Frankreich');
INSERT INTO Kunden VALUES (4, 'Ludwig Schmidt', 'Deutschland');


-- Erstellung von Tabelle "Bestellungen"
CREATE TABLE Bestellungen (
    BestellID INT PRIMARY KEY,
    KundenID INT,
    Produkt VARCHAR(50),
    Preis DECIMAL(10, 2),
    FOREIGN KEY (KundenID) REFERENCES Kunden(KundenID)
);

-- Einfügen einigen Datensätze in die Tabelle "Bestellungen"
INSERT INTO Bestellungen VALUES (101, 1, 'ProduktA', 50.00);
INSERT INTO Bestellungen VALUES (102, 2, 'ProduktB', 30.00);
INSERT INTO Bestellungen VALUES (103, 3, 'ProduktC', 80.00);
INSERT INTO Bestellungen VALUES (104, 4, 'ProduktD', 25.00);

-- Abfrage ausführen, um alle Kunden aus einem bestimmten Land anzuzeigen (Beispiel: DeutschlandBestellungen)
SELECT * FROM Kunden WHERE Land = 'Deutschland';
