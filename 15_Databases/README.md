### Setup a database.

[Use SQL Server on Docker for Windows, the easy way](https://tsql.tech/use-sql-server-on-docker-for-windows-the-easy-way/)

```shell
$ docker pull mcr.microsoft.com/mssql/server:2019-latest

$ docker run --name sql2019 -p 1433:1433 -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=passW0rd" -v `pwd`:/sql -d mcr.microsoft.com/mssql/server:2019-latest
```
[Quickstart: Run SQL Server container images with Docker](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker)