create table Apartments
(
    AptID      int,
    UnitNumber nvarchar(50),
    BuildingID int
)
go

INSERT INTO Ctci.dbo.Apartments (AptID, UnitNumber, BuildingID) VALUES (1, N'Apt1', 1);
INSERT INTO Ctci.dbo.Apartments (AptID, UnitNumber, BuildingID) VALUES (2, N'Apt2', 2);
INSERT INTO Ctci.dbo.Apartments (AptID, UnitNumber, BuildingID) VALUES (3, N'Apt3', 3);
INSERT INTO Ctci.dbo.Apartments (AptID, UnitNumber, BuildingID) VALUES (4, N'Apt4', 5);