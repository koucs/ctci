create table NonCalorieDrinks
(
    Name        nvarchar(50),
    ProductCode nvarchar(50)
)
go

INSERT INTO Ctci.dbo.NonCalorieDrinks (Name, ProductCode) VALUES (N'Diet Coca-Cola', N'COCACOLA');
INSERT INTO Ctci.dbo.NonCalorieDrinks (Name, ProductCode) VALUES (N'Fresca', N'FRESCA');
INSERT INTO Ctci.dbo.NonCalorieDrinks (Name, ProductCode) VALUES (N'Diet Pepsi', N'PEPSI');
INSERT INTO Ctci.dbo.NonCalorieDrinks (Name, ProductCode) VALUES (N'Pepsi Light', N'PEPSI');
INSERT INTO Ctci.dbo.NonCalorieDrinks (Name, ProductCode) VALUES (N'Purified Water', N'Water');