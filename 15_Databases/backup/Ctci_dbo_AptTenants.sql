create table AptTenants
(
    TenantID int,
    AptID    int
)
go

INSERT INTO Ctci.dbo.AptTenants (TenantID, AptID) VALUES (1, 1);
INSERT INTO Ctci.dbo.AptTenants (TenantID, AptID) VALUES (1, 2);
INSERT INTO Ctci.dbo.AptTenants (TenantID, AptID) VALUES (2, 3);