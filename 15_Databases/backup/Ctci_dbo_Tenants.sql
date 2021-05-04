create table Tenants
(
    TenantID   int,
    TenantName nvarchar(50)
)
go

INSERT INTO Ctci.dbo.Tenants (TenantID, TenantName) VALUES (1, N'Tenant1');
INSERT INTO Ctci.dbo.Tenants (TenantID, TenantName) VALUES (2, N'Tenant2');