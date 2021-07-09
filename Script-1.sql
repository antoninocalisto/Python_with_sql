CREATE TABLE table_temporaly
    (
     nomecampoA varchar(80),
     nomecampoB money
    )

CREATE PROCEDURE TesteTabelaTemporaria
as

create table #tmpTotalPage
    (mes smallint null,
     totalmes smallint null,
     mediames decimal(9, 3) null )

Insert into #tmpTotalPage ( mes, totalmes, media)
(select DATEPART(MONTH,data) as Mes, count(*) as TotalAcessos, null
 from Acessos  AS AC 
INNER JOIN CadastroTB AS C ON AC.idcad = C.idCad
group by DATEPART(MONTH,data))


select  mes, totalmes,
media = case
 when mes = 1 then  totalmes / 31
 when mes = 2 then  totalmes / 28
 when mes = 3 then  totalmes / 30
 when mes = 4 then  totalmes / 31
 when mes = 5 then  totalmes / 30
 when mes = 6 then  totalmes / 31
 when mes = 7 then  totalmes / 30
 when mes = 8 then  totalmes / 31
 when mes = 9 then  totalmes / 30
 when mes = 10 then  totalmes / 31
 when mes = 11 then  totalmes / 30
 when mes = 12 then  totalmes / 31 
end
from #tmpTotalPage