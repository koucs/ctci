create table Buildings
(
    BuildingID   int,
    ComplexID    int,
    BuildingName nvarchar(50),
    Address      nvarchar(50)
)
go

INSERT INTO Ctci.dbo.Buildings (BuildingID, ComplexID, BuildingName, Address) VALUES (1, 1, N'Building1', N'Address1');
INSERT INTO Ctci.dbo.Buildings (BuildingID, ComplexID, BuildingName, Address) VALUES (2, 1, N'Building2', N'Address2');
INSERT INTO Ctci.dbo.Buildings (BuildingID, ComplexID, BuildingName, Address) VALUES (3, 2, N'Building3', N'Address3');
INSERT INTO Ctci.dbo.Buildings (BuildingID, ComplexID, BuildingName, Address) VALUES (4, 1, N'Building4', N'Address4');
INSERT INTO Ctci.dbo.Buildings (BuildingID, ComplexID, BuildingName, Address) VALUES (5, 2, N'#11', N'Address5');