create table Requests
(
    RequestID   int,
    Status      nvarchar(50),
    AptID       int,
    Description nvarchar(50)
)
go

INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (1, N'Open', 1, N'Request1');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (2, N'Close', 2, N'Request2');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (3, N'Open', 3, N'Request3');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (4, N'Open', 1, N'Request4');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (5, N'Open', 3, N'Request5');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (6, N'Close', 4, N'Request6');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (7, N'Removed', 4, N'Request7');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (8, N'Close', 4, N'Request8');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (9, N'Close', 4, N'Request9');
INSERT INTO Ctci.dbo.Requests (RequestID, Status, AptID, Description) VALUES (10, N'Close', 4, N'Request10');