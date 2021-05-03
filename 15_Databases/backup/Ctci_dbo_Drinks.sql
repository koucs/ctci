create table Drinks
(
    Name        nvarchar(50),
    ProductCode nvarchar(50)
)
go

INSERT INTO Ctci.dbo.Drinks (Name, ProductCode) VALUES (N'Budweiser', N'BUDWEISER');
INSERT INTO Ctci.dbo.Drinks (Name, ProductCode) VALUES (N'Coca-Cola', N'COCACOLA');
INSERT INTO Ctci.dbo.Drinks (Name, ProductCode) VALUES (N'Pepsi', N'PEPSI');